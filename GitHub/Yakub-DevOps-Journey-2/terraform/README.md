# Terraform

| Stack | Used in | Cost risk |
|---|---|---|
| `./` | Lab 4 | Low - one t2.micro |
| `vpc/` | Lab 6 | **NAT gateway bills hourly** |
| `eks/` | Lab 8 + capstone | **EKS control plane bills hourly** |

## Standard workflow

```bash
terraform init      # downloads providers, configures the backend
terraform fmt       # formats your code - run it before every commit
terraform validate  # catches syntax and type errors without touching AWS
terraform plan      # shows exactly what will change. READ IT.
terraform apply
# ... do the lab ...
terraform destroy
terraform state list   # must be empty
```

**Never commit:** `terraform.tfvars`, `*.tfstate`, `.terraform/`, `*.pem`.
All are already in the root `.gitignore`.
