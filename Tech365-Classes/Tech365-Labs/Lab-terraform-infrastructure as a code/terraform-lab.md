1. A small company wants to host a web application on AWS. Customers should be able to access the application through the internet, while the database remains protected.
You are the DevOps engineer responsible for designing, deploying, securing, and monitoring the environment.

Before creating resources, draw an architecture diagram showing:
- An AWS Region.
- A VPC.
- Two Availability Zones.
- Public and private subnets.
- An internet gateway.
- Route tables.
- An application server.
- A database.
- Security groups.

Explain:
1. What is the difference between a Region and an Availability Zone?
2. Why does this application need a VPC?
3. What makes a subnet public or private?
4. Why should the database remain private?
5. What happens if the application server fails?

2. Build the network

Create a VPC with:
VPC - Use a CIDR block of your choice 
Public subnets - Two, in different Availability Zones 
Private subnets - Two, in different Availability Zones 
Internet gateway - Attach it to the VPC 
Public route table - Add an internet route through the internet gateway 
Private route table - Keep database subnets without a direct internet route 

Associate each subnet with the appropriate route table.

Explain:
1. What does 0.0.0.0/0 mean in a route table?
2. Does placing an EC2 instance in a public subnet automatically make it accessible from the internet?
3. When would a private application server need a NAT gateway?
4. What is the difference between a security group and a network ACL?


3. Automate infrastructure with Terraform
Create Terraform configuration for:
- The VPC and subnets.
- The internet gateway and route tables.
- Security groups.
- The EC2 instance.

Also explain:
1. What is the purpose of Terraform state?
2. What is the difference between `terraform plan` and `terraform apply`?
3. What could happen if someone changes a Terraform-managed resource manually?
4. Why should Terraform state files be protected?
5. How would you remove the resources created by Terraform?