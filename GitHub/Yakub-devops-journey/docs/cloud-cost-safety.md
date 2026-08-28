# Cloud cost safety

You are learning. A forgotten NAT gateway costs more than the course did.

## Rules

1. **Set a billing alarm before anything else.** AWS Billing -> Budgets -> create a
   monthly budget with an email alert. Set it low, e.g. $5. Do this on day one.
2. **Free tier by default.** `t2.micro` / `t3.micro` for EC2, `db.t3.micro` for RDS,
   `gp3` volumes at 8-20GB. Never launch anything larger "just to be safe".
3. **Stop is not delete.** A stopped EC2 still bills for its EBS volume and its Elastic IP.
4. **Destroy at the end of every session, not the end of the week.**
5. **Check the console with your own eyes.** Billing -> Cost Explorer, and the EC2 console
   with the region filter set to "All regions" - forgotten resources hide in regions you
   only visited once.

## Resources that WILL cost money even on a new account

| Resource | Why | Mitigation |
|---|---|---|
| NAT Gateway | Hourly charge + data processing, no free tier | Delete the moment the lab ends. Use a NAT instance or public subnets for practice. |
| Elastic Load Balancer | Free tier is limited hours only | Delete after every lab. |
| Elastic IP not attached | Charged when idle | Release it. |
| EKS control plane | Flat hourly charge per cluster | Use Minikube where the lab allows. Destroy EKS same-day. |
| EBS snapshots | Storage charge accumulates silently | Delete old snapshots weekly. |
| RDS with Multi-AZ | Doubles cost, outside free tier | Single-AZ only. |
| CloudFront / Route 53 hosted zones | Small monthly charges | Delete the hosted zone when done. |
| GCP Cloud SQL / Global LB | Outside most free tiers | Run the Section 301 cleanup in full. |

## The standard end-of-lab cleanup

```bash
# Terraform-managed infrastructure
terraform destroy -auto-approve
terraform state list          # must return nothing

# Anything created by hand - check every service you touched
aws ec2 describe-instances --query \
  'Reservations[].Instances[?State.Name!=`terminated`].[InstanceId,State.Name,Tags]'
aws elbv2 describe-load-balancers --query 'LoadBalancers[].LoadBalancerName'
aws ec2 describe-nat-gateways --query 'NatGateways[?State==`available`].NatGatewayId'
aws ec2 describe-addresses --query 'Addresses[].PublicIp'
aws rds describe-db-instances --query 'DBInstances[].DBInstanceIdentifier'
aws s3 ls
```

**What this does:** asks AWS what is still alive in the current region.
**Why:** the console lies to you if the region dropdown is wrong; the CLI does not.
**Expected result:** empty lists. If anything comes back, delete it before you log off.

Add `--region <other-region>` and repeat for any region you experimented in.
