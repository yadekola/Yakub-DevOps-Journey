variable "key_name" {
  description = "Name of the key pair to use for the EC2 instance"
  type        = string
  default     = "server-tech365"
}

variable "instance_type" {
  description = "Type of the EC2 instance"
  type        = string
  default     = "t3.micro"
}

# Name shown for the Lambda function and its execution role.
variable "lambda_function_name" {
  description = "Name for the serverless web app function"
  type        = string
  default     = "tech365-web-app"
}

# Python runtime version used by AWS Lambda.
variable "lambda_runtime" {
  description = "Python runtime for the Lambda web app"
  type        = string
  default     = "python3.12"
}

# Amount of memory allocated to the function, in megabytes.
variable "lambda_memory_size" {
  description = "Memory allocated to the Lambda function in MB"
  type        = number
  default     = 128
}

# Maximum number of seconds one request is allowed to run.
variable "lambda_timeout" {
  description = "Maximum runtime per Lambda request in seconds"
  type        = number
  default     = 10
}

# Monthly account-wide cost limit. AWS Budgets expects this amount as text.
variable "cost_budget_limit" {
  description = "Monthly AWS cost budget limit"
  type        = string
  default     = "10"
}

# Currency used for the cost budget, for example USD.
variable "cost_budget_currency" {
  description = "Currency for the monthly AWS cost budget"
  type        = string
  default     = "USD"
}

# Threshold as a percentage of the budget at which the email alert is sent.
variable "cost_budget_alert_percent" {
  description = "Actual spending percentage that triggers the budget email"
  type        = number
  default     = 80
}

# Required: set this to the email address that should receive the alert.
variable "cost_budget_alert_email" {
  description = "Email address to notify when actual costs reach the threshold"
  type        = string
  sensitive   = true
}

# Name of the monthly account-wide cost budget.
variable "cost_budget_name" {
  description = "Name of the AWS monthly cost budget"
  type        = string
  default     = "tech365-monthly-cost-budget"
}

# Existing IAM user that you use to sign in to the AWS Console. Terraform adds
# Bedrock Playground permissions to this user; it does not create a new user.
variable "bedrock_playground_user_name" {
  description = "Name of the existing IAM user that will use the Bedrock Playground"
  type        = string
}

# Region where the Bedrock Playground model will be selected and invoked.
variable "bedrock_region" {
  description = "AWS Region where you will use a foundation model in Bedrock"
  type        = string
  default     = "us-east-1"
}
