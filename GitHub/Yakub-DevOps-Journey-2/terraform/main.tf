# Lab 4 starter - single app instance with a security group.
# Run: terraform init && terraform plan && terraform apply
# ALWAYS finish with: terraform destroy

terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }

  # Uncomment AFTER creating the bucket and lock table (step 3 of Lab 4).
  # backend "s3" {
  #   bucket         = "yaco-devops-tfstate-CHANGEME"
  #   key            = "labs/app/terraform.tfstate"
  #   region         = "eu-west-1"
  #   dynamodb_table = "yaco-devops-tflock"
  #   encrypt        = true
  # }
}

provider "aws" {
  region = var.region
  # No credentials here. Ever.
  # Use `aws configure`, environment variables, or an IAM role.
}

resource "aws_security_group" "app" {
  name        = "${var.project}-app-sg"
  description = "App tier - SSH from admin CIDR only, HTTP from anywhere"

  ingress {
    description = "SSH from my IP only"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.admin_cidr] # never 0.0.0.0/0
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = local.tags
}

resource "aws_instance" "app" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.app.id]

  tags = merge(local.tags, { Name = "${var.project}-app" })
}

locals {
  tags = {
    Project     = var.project
    Owner       = var.owner # the audit script looks for this tag
    Environment = "learning"
    ManagedBy   = "terraform"
  }
}
