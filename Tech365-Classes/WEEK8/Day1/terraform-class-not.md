# Terraform Class Notes: Building an AWS Web Server

## What we started with

We began by creating a **subnet**. A subnet is a smaller section of a network where we can place resources such as a virtual server. In this project, the subnet is inside an AWS VPC.

## What the Terraform files build

The `main.tf` file describes the AWS resources and how they connect. Terraform reads these instructions and creates the resources for us.

1. **AWS provider** — tells Terraform to use AWS. The provider uses the credentials and region configured for your AWS account.
2. **VPC** — creates our private network, with address range `10.0.0.0/16`. Think of it as the main network for this project.
3. **Subnet** — creates a smaller network inside the VPC, with range `10.0.1.0/24`, in availability zone `us-east-1a`. The EC2 server will live here.
4. **Internet gateway** — provides a connection between the VPC and the internet.
5. **Security group** — acts like a firewall for the server. The rules allow incoming web traffic on port 80 (HTTP) and remote login traffic on port 22 (SSH). Outgoing traffic is allowed.
6. **Route table and association** — the route table says that traffic for any outside address (`0.0.0.0/0`) should go through the internet gateway. The association attaches that route table to our subnet.
7. **Ubuntu AMI lookup** — finds the latest matching Ubuntu 22.04 image from Canonical. An AMI is the starting image used to launch an EC2 server.
8. **EC2 instance** — launches a `t3.micro` server in the subnet, gives it a public IP, attaches the security group, and uses the key pair named in `variables.tf`.
9. **Output** — prints the instance public IP after Terraform creates it.

References such as `aws_vpc.tech365-vpc.id` connect resources together. For example, the subnet refers to the VPC ID, so Terraform knows the subnet belongs inside that VPC.

## What the other files do

- **`variables.tf`** holds settings that can be changed, such as the EC2 key pair name and instance type. The current defaults are `server-tech365` and `t3.micro`.
- **`user_data.sh`** is a startup script that runs when the EC2 server starts. It updates Ubuntu, installs Nginx, starts it, and enables it to start after a reboot.
- **`terraform-class-not.md`** is where these learning notes are kept.

## Running the configuration

Open a terminal in this project folder and run:

```bash
terraform init
terraform plan
terraform apply
```

- `terraform init` prepares Terraform and downloads the AWS provider.
- `terraform plan` previews what Terraform intends to create.
- `terraform apply` asks for confirmation, then creates the resources. Type `yes` when prompted.

After it finishes, Terraform shows the `public_ip` output. You can enter that IP in a browser to check the web server. The network needs to route internet traffic to the subnet, and the security group needs to allow HTTP on port 80.

When you have finished using the resources, run `terraform destroy` and confirm with `yes` to remove the resources Terraform created.

## Simple summary

We made a network, divided off a subnet, connected it to the internet, added firewall rules, and launched an Ubuntu server in it. The startup script installs Nginx so the server can provide a basic web service.
