terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.69.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.7"
    }
  }
}

provider "aws" {
  # Configuration options
}

# CREATING A VPC
resource "aws_vpc" "tech365-vpc" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "tech365-vpc"
  }
}

resource "aws_subnet" "tech365-sub" {
  vpc_id            = aws_vpc.tech365-vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "tech365-sub"
  }
}

resource "aws_internet_gateway" "tech365-gw" {
  vpc_id = aws_vpc.tech365-vpc.id

  tags = {
    Name = "tech365-gw"
  }
}

resource "aws_security_group" "tech365-sg" {
  name        = "tech365-sg"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = aws_vpc.tech365-vpc.id

  tags = {
    Name = "tech365-sg"
  }
}

resource "aws_vpc_security_group_ingress_rule" "http" {
  security_group_id = aws_security_group.tech365-sg.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 80
  ip_protocol       = "tcp"
  to_port           = 80

}

resource "aws_vpc_security_group_ingress_rule" "ssh" {
  security_group_id = aws_security_group.tech365-sg.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22

}


resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.tech365-sg.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1" # semantically equivalent to all ports
}


# creating route table

resource "aws_route_table" "tech365-rt" {
  vpc_id = aws_vpc.tech365-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.tech365-gw.id
  }


  tags = {
    Name = "tech365-rt"
  }
}

# Route table association

resource "aws_route_table_association" "tech365-rt-association" {
  subnet_id      = aws_subnet.tech365-sub.id
  route_table_id = aws_route_table.tech365-rt.id
}


data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "ec2" {
  ami                         = data.aws_ami.ubuntu.id
  associate_public_ip_address = true
  instance_type               = var.instance_type
  user_data                   = file("./user_data.sh")
  subnet_id                   = aws_subnet.tech365-sub.id
  vpc_security_group_ids      = [aws_security_group.tech365-sg.id]
  key_name                    = var.key_name

  tags = {
    Name = "tech365-instance"
  }
}


output "public_ip" {
  value = aws_instance.ec2.public_ip
}

# PACKAGE THE LAMBDA WEB APP
# archive_file turns the Python source file into the ZIP package Lambda expects.
data "archive_file" "web_app" {
  type        = "zip"
  source_file = "${path.module}/lambda_app/app.py"
  output_path = "${path.module}/lambda_app.zip"
}

# Lambda assumes this role when the function runs. The trust policy lets the
# Lambda service use the role.
resource "aws_iam_role" "web_app" {
  name = "${var.lambda_function_name}-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# This AWS-managed policy lets Lambda write logs to CloudWatch.
resource "aws_iam_role_policy_attachment" "web_app_logs" {
  role       = aws_iam_role.web_app.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Upload and configure the Python function that returns the web page.
resource "aws_lambda_function" "web_app" {
  function_name    = var.lambda_function_name
  role             = aws_iam_role.web_app.arn
  runtime          = var.lambda_runtime
  handler          = "app.lambda_handler"
  filename         = data.archive_file.web_app.output_path
  source_code_hash = data.archive_file.web_app.output_base64sha256
  memory_size      = var.lambda_memory_size
  timeout          = var.lambda_timeout

  depends_on = [aws_iam_role_policy_attachment.web_app_logs]

  tags = {
    Name = var.lambda_function_name
  }
}

# The Function URL gives the Lambda function an HTTPS endpoint.
# NONE means anyone with the URL can open the app without AWS login.
resource "aws_lambda_function_url" "web_app" {
  function_name      = aws_lambda_function.web_app.function_name
  authorization_type = "NONE"
}

# Print the web app address after Terraform creates the Function URL.
output "lambda_web_app_url" {
  description = "Public HTTPS URL for the Lambda web app"
  value       = aws_lambda_function_url.web_app.function_url
}

# BEDROCK PLAYGROUND PERMISSIONS
# Terraform cannot open or operate the Bedrock console playground itself.
# This inline policy gives an existing IAM user the permissions needed to view
# models in the console and invoke foundation models in the selected Region.
# The policy does not deploy a model. Model inference can incur usage charges.
resource "aws_iam_user_policy" "bedrock_playground" {
  name = "bedrock-playground-access"
  user = var.bedrock_playground_user_name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "BedrockConsoleRead"
        Effect = "Allow"
        Action = [
          "bedrock:ListFoundationModels",
          "bedrock:ListInferenceProfiles",
          "bedrock:ListProvisionedModelThroughputs",
          "bedrock:ListCustomModels",
          "bedrock:ListGuardrails",
          "bedrock:ListFoundationModelAgreementOffers",
          "bedrock:ListMarketplaceModelEndpoints",
          "bedrock:ListImportedModels",
          "bedrock:ListPromptRouters",
          "bedrock:GetFoundationModel",
          "bedrock:GetFoundationModelAvailability",
          "bedrock:GetInferenceProfile",
          "bedrock:GetUseCaseForModelAccess",
          "bedrock:PutUseCaseForModelAccess"
        ]
        Resource = "*"
      },
      {
        Sid    = "InvokeFoundationModelsInSelectedRegion"
        Effect = "Allow"
        Action = ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"]
        Resource = [
          "arn:aws:bedrock:${var.bedrock_region}::foundation-model/*",
          "arn:aws:bedrock:${var.bedrock_region}:*:inference-profile/*"
        ]
      },
      {
        Sid      = "ReadPublicSageMakerHub"
        Effect   = "Allow"
        Action   = ["sagemaker:ListHubContents"]
        Resource = "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
      },
      {
        Sid      = "MarketplaceSubscriptionThroughBedrock"
        Effect   = "Allow"
        Action   = ["aws-marketplace:ViewSubscriptions", "aws-marketplace:Subscribe"]
        Resource = "*"
        Condition = {
          StringEquals = {
            "aws:CalledViaLast" = "bedrock.amazonaws.com"
          }
        }
      }
    ]
  })
}

# MONTHLY AWS COST BUDGET
# This budget tracks total account costs each month. It sends an email when
# actual spending reaches the configured percentage of the monthly limit.
# A budget is an alert; it does not stop resources or spending automatically.
resource "aws_budgets_budget" "monthly_cost" {
  name         = var.cost_budget_name
  budget_type  = "COST"
  time_unit    = "MONTHLY"
  limit_amount = var.cost_budget_limit
  limit_unit   = var.cost_budget_currency

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = var.cost_budget_alert_percent
    threshold_type             = "PERCENTAGE"
    notification_type          = "ACTUAL"
    subscriber_email_addresses = [var.cost_budget_alert_email]
  }
}
