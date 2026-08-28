# Lab 4: Terraform-provisioned infrastructure with Python/Boto3 automation

**Week 4 — Saturday 26 September 2026**

## Objective

Replace all manual clicking with code. Write Terraform that provisions the app tier (EC2s, security groups, key pair, S3 bucket, remote state backend) and a Python/Boto3 tool that audits the account: lists running instances, flags untagged resources, and reports estimated monthly cost of what is running.

## Why this lab exists

Clicking in the console does not scale and cannot be reviewed. This is the lab where your infrastructure becomes something you can delete fearlessly, because you can recreate it in one command.

## Architecture

```
main.tf/variables.tf/outputs.tf -> terraform apply -> AWS (EC2, SG, S3)
S3 + DynamoDB backend for state
Python/Boto3 auditor -> reports what is actually running and what it costs
```

Draw your own version of this diagram before you start building. Save it to
`../../architecture/lab-04.png`. If you cannot draw it, you do not understand it yet.

## Prerequisites

- AWS CLI configured
- Terraform installed
- Python 3 with boto3
- Lectures 200-233 completed

## Acceptance criteria

- [ ] Remote state in S3 with a DynamoDB lock table
- [ ] Variables and outputs - no hard-coded AMIs or CIDRs
- [ ] A `terraform destroy` that leaves the account genuinely clean
- [ ] The Boto3 auditor script run before and after destroy, with output saved

## Steps

1. **Write `main.tf` for one EC2 instance.** Run `terraform init`, `plan`, `apply`.
   *What plan does:* shows exactly what will change before it changes. Read it every time.
   *Expected:* `Plan: 1 to add, 0 to change, 0 to destroy.`

2. **Split into `main.tf`, `variables.tf`, `outputs.tf`.** Nothing hard-coded.

3. **Create the S3 bucket and DynamoDB lock table**, then move state to the remote backend.
   *Why:* local state means only you can apply, and losing the file loses your infrastructure.

4. **Add the security groups and key pair** to the Terraform config.

5. **Write `scripts/aws_audit.py`** with Boto3: list running instances with name, type,
   launch time and tags; flag anything without an `Owner` tag; print an estimated monthly
   cost using a small hard-coded price map.

6. **Run the auditor, then `terraform destroy`, then run the auditor again.** Save both
   outputs — the empty second one is your proof of cleanup.

## Verification

- [ ] `terraform destroy` followed by `terraform apply` reproduces everything
- [ ] `terraform state list` after destroy returns nothing
- [ ] `terraform.tfvars` is in `.gitignore` and NOT committed
- [ ] The auditor flags an instance you deliberately left untagged
- [ ] A second person could run your code with only a README and their own AWS account

## Troubleshooting challenges

Work these out yourself before looking anything up. Hints only — no answers.

1. **`terraform apply` fails with a dependency cycle.**
   *Hint: Read the actual error, not the summary. Then ask: what changed?*
2. **State is locked and you cannot apply - the previous run crashed.**
   *Hint: Check the layer below the one you think is broken.*
3. **Boto3 raises NoCredentialsError inside a script that worked in the shell.**
   *Hint: Compare a working case with the broken one and list every difference.*

## Cleanup

```bash
terraform destroy -auto-approve
terraform state list   # expect empty
```
Then empty and delete the state bucket and the DynamoDB table, in that order — S3 will not delete a non-empty bucket.

## Interview questions

Answer these in writing in `answers.md` before you consider the lab finished.

1. What is Terraform state and why does it need to be remote?
2. What does the DynamoDB table do in this setup?
3. What is the difference between `terraform plan` and `terraform apply`?
4. Someone changed a resource in the console. What happens on your next apply?
5. What is idempotency and how does Terraform achieve it?
6. Why should `terraform.tfvars` never be committed?
