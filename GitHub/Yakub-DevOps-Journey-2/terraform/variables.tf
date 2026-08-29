variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "project" {
  description = "Name prefix for all resources"
  type        = string
  default     = "yaco-devops"
}

variable "owner" {
  description = "Owner tag - the audit script flags anything without it"
  type        = string
}

variable "ami_id" {
  description = "AMI ID - region specific, look it up, do not copy from a tutorial"
  type        = string
}

variable "instance_type" {
  description = "Keep this free tier eligible"
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "Existing EC2 key pair name (the .pem stays off this repo)"
  type        = string
}

variable "admin_cidr" {
  description = "Your public IP with /32, e.g. 102.89.x.x/32"
  type        = string
}
