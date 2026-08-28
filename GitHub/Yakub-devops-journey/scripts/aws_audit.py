#!/usr/bin/env python3
"""
Lab 4 - AWS account auditor.

WHAT IT DOES
  Lists every non-terminated EC2 instance, flags anything missing an Owner tag, and
  gives a rough monthly cost estimate for what is currently running.

WHY IT EXISTS
  The single most expensive habit in cloud learning is forgetting something is running.
  Run this before you log off. Run it again after `terraform destroy`.

USAGE
  python3 aws_audit.py                 # current default region
  python3 aws_audit.py --all-regions   # the ones you forgot about

CREDENTIALS
  Read from your normal AWS config (`aws configure`, env vars, or an IAM role).
  Nothing is hard-coded here and nothing should ever be.
"""
import argparse
import sys

try:
    import boto3
    from botocore.exceptions import NoCredentialsError, ClientError
except ImportError:
    sys.exit("boto3 is not installed. Run: pip install boto3")

# Rough on-demand USD/hour. Indicative only - not a billing source of truth.
PRICE_PER_HOUR = {
    "t2.micro": 0.0116, "t3.micro": 0.0104, "t2.small": 0.023,
    "t3.small": 0.0208, "t2.medium": 0.0464, "t3.medium": 0.0416,
    "t3.large": 0.0832, "m5.large": 0.096,
}
HOURS_PER_MONTH = 730


def audit_region(region):
    ec2 = boto3.client("ec2", region_name=region)
    rows, monthly, untagged = [], 0.0, []

    reservations = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name",
                  "Values": ["running", "stopped", "pending", "stopping"]}]
    )["Reservations"]

    for res in reservations:
        for inst in res["Instances"]:
            tags = {t["Key"]: t["Value"] for t in inst.get("Tags", [])}
            itype = inst["InstanceType"]
            state = inst["State"]["Name"]
            cost = PRICE_PER_HOUR.get(itype, 0.05) * HOURS_PER_MONTH if state == "running" else 0.0
            monthly += cost
            rows.append((inst["InstanceId"], itype, state,
                         tags.get("Name", "-"), tags.get("Owner", "MISSING"), cost))
            if "Owner" not in tags:
                untagged.append(inst["InstanceId"])

    # Things that quietly cost money even with no instances running
    extras = []
    try:
        nats = ec2.describe_nat_gateways(
            Filters=[{"Name": "state", "Values": ["available"]}])["NatGateways"]
        for n in nats:
            extras.append(("NAT Gateway", n["NatGatewayId"], 32.0))
            monthly += 32.0
    except ClientError:
        pass

    for addr in ec2.describe_addresses().get("Addresses", []):
        if "InstanceId" not in addr:
            extras.append(("Unattached Elastic IP", addr.get("PublicIp", "?"), 3.6))
            monthly += 3.6

    return rows, extras, monthly, untagged


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all-regions", action="store_true",
                    help="scan every enabled region - slower, but finds forgotten resources")
    args = ap.parse_args()

    try:
        session = boto3.session.Session()
        regions = ([r["RegionName"] for r in
                    boto3.client("ec2", region_name="eu-west-1").describe_regions()["Regions"]]
                   if args.all_regions else [session.region_name or "eu-west-1"])
    except NoCredentialsError:
        sys.exit("No AWS credentials found. Run `aws configure` first.")

    grand_total, all_untagged, found_anything = 0.0, [], False

    for region in regions:
        try:
            rows, extras, monthly, untagged = audit_region(region)
        except ClientError as e:
            print(f"  {region}: skipped ({e.response['Error']['Code']})")
            continue
        if not rows and not extras:
            continue
        found_anything = True
        print(f"\n=== {region} ===")
        if rows:
            print(f"{'INSTANCE ID':<21}{'TYPE':<12}{'STATE':<10}{'NAME':<18}{'OWNER':<12}{'$/MONTH':>9}")
            print("-" * 82)
            for r in rows:
                print(f"{r[0]:<21}{r[1]:<12}{r[2]:<10}{r[3]:<18}{r[4]:<12}{r[5]:>9.2f}")
        for kind, ident, cost in extras:
            print(f"  ! {kind}: {ident}  ~${cost:.2f}/month")
        grand_total += monthly
        all_untagged += untagged

    print("\n" + "=" * 82)
    if not found_anything:
        print("Nothing running. Account is clean.")
        return
    print(f"ESTIMATED MONTHLY COST: ${grand_total:.2f}")
    if all_untagged:
        print(f"UNTAGGED (no Owner tag): {', '.join(all_untagged)}")
        print("Tag them or destroy them. Untagged resources are how bills get forgotten.")


if __name__ == "__main__":
    main()
