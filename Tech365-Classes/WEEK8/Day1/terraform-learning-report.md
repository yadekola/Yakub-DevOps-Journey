# Terraform and AWS Learning Report

**Project:** Tech365 Classes — Week 8, Day 1  
**Subject:** Building an AWS network and web server with Terraform  
**Report date:** 20 October 2026

## Executive summary

This project uses Terraform to describe and manage a small AWS environment. The configuration starts with a VPC and subnet, adds internet routing and firewall rules, and launches an Ubuntu EC2 instance. A startup script installs Nginx. Terraform state in the project records one instance of each configured resource, including the VPC, subnet, gateway, routing, security group, and EC2 server.

The project files and Terraform state were available for review. A saved terminal history and error log were not found in the usual PowerShell history locations, so this report does not invent terminal commands or errors that cannot be verified.

## Learning objectives and concepts

### 1. Terraform and infrastructure as code

Terraform lets you describe cloud resources in configuration files. Rather than creating every item manually in the AWS console, you write the desired setup in HCL and let Terraform compare that configuration with its state and the infrastructure it manages.

Key commands to know:

- `terraform init` prepares the working folder and installs the required provider.
- `terraform plan` previews changes Terraform intends to make.
- `terraform apply` creates or updates resources after confirmation.
- `terraform destroy` removes resources managed by the configuration after confirmation.

These are standard commands for this kind of project. Because terminal history was unavailable, this report cannot confirm which commands were typed or the exact order used in the session.

### 2. VPC and subnet

The VPC (`10.0.0.0/16`) is the project’s AWS network. The subnet (`10.0.1.0/24`) is a smaller address range within that network and is placed in availability zone `us-east-1a`. The EC2 instance is configured to launch in this subnet.

A subnet gives resources a specific place in the VPC and a network address range. The VPC ID reference in the subnet resource connects it to the VPC.

### 3. Internet connectivity and routes

The internet gateway attaches to the VPC. The route table includes a default route for `0.0.0.0/0` through that gateway, and a route table association connects the table to the subnet. Together, these settings provide a path for internet traffic. The EC2 resource also requests a public IP address.

### 4. Security groups and traffic

The security group is attached to the EC2 instance. Its inbound rules allow HTTP on TCP port 80 and SSH on TCP port 22 from `0.0.0.0/0`. Its outbound rule allows all IPv4 traffic.

A security group is a virtual firewall. The source range `0.0.0.0/0` means the inbound rule accepts traffic from any IPv4 address. The SSH rule is therefore open broadly; for a real deployment, restrict SSH to the administrator’s trusted IP address.

### 5. AMI and EC2 instance

The `aws_ami.ubuntu` data source looks up a recent Canonical Ubuntu 22.04 image. A data source finds information about an existing item; it does not create the AMI. The `aws_instance.ec2` resource uses that image to launch a `t3.micro` EC2 server in the subnet.

The instance also uses the key pair named by `var.key_name`, attaches the security group, requests a public IP, and loads `user_data.sh` as startup instructions. The public IP is declared as a Terraform output.

### 6. Variables and startup script

`variables.tf` defines the EC2 key pair name (`server-tech365`) and instance type (`t3.micro`) as configurable variables with defaults. Variables make it easier to adjust settings without editing the resource definitions.

`user_data.sh` runs at startup. It updates Ubuntu’s package list, installs Nginx, starts the service, and enables it at boot. The script also runs `chmod 777` on the default Nginx index file.

## Resource flow

The resources fit together in this order:

1. Terraform configures the AWS provider.
2. It creates the VPC and its subnet.
3. It creates the internet gateway and route table, then associates the table with the subnet.
4. It creates the security group and its inbound and outbound rules.
5. It looks up an Ubuntu AMI and launches the EC2 instance in the subnet.
6. The instance startup script installs Nginx, and Terraform reports the public IP.

Terraform uses references such as `aws_vpc.tech365-vpc.id` to connect resources and determine dependencies.

## Evidence reviewed

- `main.tf`: provider, VPC, subnet, internet gateway, security group rules, route table, AMI lookup, EC2 instance, and public IP output.
- `variables.tf`: default key pair name and instance type.
- `user_data.sh`: Nginx installation and startup commands.
- `terraform.tfstate`: records Terraform-managed instances for the resources in this configuration and a `public_ip` output. The state file indicates Terraform has tracked these resources; it does not by itself prove that every resource is currently healthy or reachable.

## Errors and troubleshooting record

No terminal transcript, PowerShell history file, or saved Terraform error log was found in the project or the usual PowerShell history locations available during this review. As a result, specific past error messages, fixes, and the exact sequence of terminal commands cannot be reported reliably.

No error text has been added as if it were observed. For future troubleshooting, save the command and its full output when a failure occurs, then record the fix and whether `terraform plan` succeeds afterward.

## Review findings and recommended improvements

- **Limit SSH access:** change the SSH ingress CIDR from `0.0.0.0/0` to a trusted administrator IP range.
- **Tighten file permissions:** `chmod 777` gives every local user read, write, and execute permissions on the Nginx index file. Use narrower permissions appropriate to the file and web server instead.
- **Serve an intentional page:** the current `user_data.sh` installs Nginx but does not write the “Welcome to Tech365” page shown in earlier draft notes. If that page is desired, add an explicit command to create the page.
- **Keep state private:** Terraform state can contain infrastructure details and sometimes sensitive values. Do not commit `terraform.tfstate` or its backup to a public repository; check `.gitignore` and store state safely.
- **Confirm the AWS region:** the subnet is pinned to `us-east-1a`. Ensure the AWS provider is configured for the matching region, since the provider block currently has no explicit region setting.

These are review recommendations based on the current files, not confirmed terminal errors.

## Key takeaways

- A VPC is the main private network; a subnet is a smaller network inside it.
- A route table and internet gateway provide a network path; security group rules control allowed traffic.
- An AMI is the server image used to launch an EC2 instance.
- Variables make selected settings reusable and easier to change.
- User data automates setup when an instance first starts.
- Terraform references connect resources, while Terraform state records the resources it manages.
- Review security rules and permissions before using a configuration beyond a classroom exercise.

## Closing note

This project demonstrates the main steps for deploying a basic web server in AWS with Terraform: define the network, provide a route, set traffic rules, launch a server, and install a web service. The configuration provides a solid foundation for learning how cloud resources depend on one another.
