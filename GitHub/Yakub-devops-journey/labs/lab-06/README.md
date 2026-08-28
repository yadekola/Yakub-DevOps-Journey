# Lab 6: Production-style VPC + AWS-native CI/CD pipeline

**Week 6 — Saturday 10 October 2026**

## Objective

Build a proper three-tier VPC in Terraform (public/private subnets across two AZs, IGW, NAT gateway, route tables, bastion) and deploy the application into it through an AWS-native CodeCommit/CodeBuild/CodePipeline flow.

## Why this lab exists

Default VPCs are a training-wheels environment. Real workloads live in private subnets and only talk to the internet on purpose. This lab is where your architecture starts looking employable.

## Architecture

```
VPC 10.0.0.0/16
  public-1a, public-1b  -> IGW  -> ALB + bastion
  private-1a, private-1b -> NAT -> app + database tiers
CodeCommit -> CodeBuild -> CodePipeline -> Beanstalk/EC2
```

Draw your own version of this diagram before you start building. Save it to
`../../architecture/lab-06.png`. If you cannot draw it, you do not understand it yet.

## Prerequisites

- Terraform confident from Lab 4
- Lectures 263-301 completed

## Acceptance criteria

- [ ] Application and database tiers in PRIVATE subnets with no public IPs
- [ ] NAT gateway for egress only - note that this one DOES cost money hourly
- [ ] buildspec.yml committed to the repo
- [ ] A network diagram you drew yourself, committed as PNG

## Steps

1. **Draw it first.** CIDR blocks, subnets, route tables, gateways. On paper.
2. **Write the VPC in Terraform:** VPC, 2 public + 2 private subnets across two AZs,
   internet gateway, NAT gateway, and the two route tables.
   *Why two AZs:* a single-AZ design fails an interview question and a real outage.
3. **Launch a bastion in a public subnet** and app instances in private subnets with no public IP.
4. **Verify the private instances can reach the internet** (`sudo apt update`) but cannot be
   reached from it.
5. **Build the CodeCommit -> CodeBuild -> CodePipeline flow** with a `buildspec.yml`.
6. **Deploy through the pipeline** into the private subnets.

## Verification

- [ ] Private instances have no public IP and still install packages
- [ ] You can SSH bastion -> app, but not laptop -> app
- [ ] A commit triggers the pipeline automatically
- [ ] Route tables: public -> IGW, private -> NAT
- [ ] Your hand-drawn diagram matches what Terraform actually created

## Troubleshooting challenges

Work these out yourself before looking anything up. Hints only — no answers.

1. **Private instances cannot reach the internet to install packages.**
   *Hint: Read the actual error, not the summary. Then ask: what changed?*
2. **CodeBuild fails with 'no matching artifact' at the end of the build.**
   *Hint: Check the layer below the one you think is broken.*
3. **You can SSH to the bastion but not from the bastion to the app server.**
   *Hint: Compare a working case with the broken one and list every difference.*

## Cleanup

**The NAT gateway is the expensive thing here. Destroy it today.**
```bash
terraform destroy -auto-approve
aws ec2 describe-nat-gateways --query 'NatGateways[?State==`available`]'   # expect []
```
Also delete the CodePipeline, the CodeBuild project, and any Beanstalk environment.

## Interview questions

Answer these in writing in `answers.md` before you consider the lab finished.

1. Walk me through your VPC design and justify every subnet.
2. What is the difference between an internet gateway and a NAT gateway?
3. Why did you use two availability zones?
4. A private instance cannot reach the internet. What are the three things you check?
5. What does `buildspec.yml` do?
6. How much does this architecture cost per month if you left it running?
