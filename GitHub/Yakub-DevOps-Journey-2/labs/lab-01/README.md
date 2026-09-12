# Lab 1: Lift & Shift: multi-tier vProfile stack on AWS EC2

**Week 1 — Saturday 05 September 2026**

## Objective

Rebuild the Section 14 architecture from scratch WITHOUT replaying the videos: MySQL, Memcached and RabbitMQ on private EC2s, Tomcat app EC2, Nginx web EC2, an Application Load Balancer in front, a Route 53 record, and an Autoscaling Group for the app tier. Everything free-tier sized.

## Why this lab exists

Every managed service you will meet later is an abstraction over exactly this. If you have never wired a load balancer to an app server to a database by hand, the abstraction will hide things you needed to understand.

## Architecture

```
Internet -> ALB -> [Nginx web tier] -> [Tomcat app tier (ASG)] -> [MySQL | Memcached | RabbitMQ]
                                                    Route 53 private zone for backend names
```

Draw your own version of this diagram before you start building. Save it to
`../../architecture/lab-01.png`. If you cannot draw it, you do not understand it yet.

## Prerequisites

- AWS account with a billing alarm already configured
- Key pair created and the .pem stored OUTSIDE this repo
- Maven and JDK 11 locally
- Lectures 119-139 completed

## Acceptance criteria

- [ ] Security group chained rules (web -> app -> db) rather than 0.0.0.0/0 everywhere
- [ ] Artifact build with Maven and deploy to Tomcat
- [ ] Route 53 private hosted zone for backend service discovery
- [ ] Health checks that actually fail when the app is down

## Steps

1. **Create the security groups first, before any instance.**
   Three groups: `web-sg` (22 from your IP, 80/443 from ALB), `app-sg` (8080 from web-sg only),
   `backend-sg` (3306/11211/5672 from app-sg only, and from itself).
   *Why first:* if you create instances first you will end up opening 0.0.0.0/0 "temporarily"
   and never close it. Chained groups are the whole point of this lab.
   
2. **Launch the three backend instances** (MySQL, Memcached, RabbitMQ) in a private subnet,
   `t2.micro`, using `backend-sg`.

3. **Create a Route 53 private hosted zone** and add A records: `db01`, `mc01`, `rmq01`.
   *Why:* the app config references hostnames, not IPs. IPs change when instances restart.

4. **Build the artifact:** `mvn clean install` — check `target/` contains the `.war`.
   *Expect:* BUILD SUCCESS and a file roughly 20-30MB.

5. **Launch the app instance**, install Tomcat, deploy the war, start it.
   *Verify:* `curl localhost:8080` from inside the instance returns HTML.

6. **Launch the web instance**, install Nginx, configure it as a reverse proxy to the app tier.

7. **Create the ALB and target group**, register the web instance, set the health check path
   to something the app actually serves.

8. **Create a launch template and Autoscaling Group** for the app tier, min 1 / desired 1 / max 2.

9. **Point a Route 53 record at the ALB** and reach the app in a browser by name.

## Verification

- [ ] `curl http://<alb-dns>` returns the application page
- [ ] Target group shows all targets healthy
- [ ] `telnet db01 3306` succeeds from the app instance and FAILS from your laptop
- [ ] Terminating the app instance causes the ASG to replace it within a few minutes
- [ ] No security group anywhere has 0.0.0.0/0 on port 3306

## Troubleshooting challenges

Work these out yourself before looking anything up. Hints only — no answers.

1. **Your ALB target group shows 'unhealthy' but the app runs fine when you curl it from the instance itself.**
   *Hint: Read the actual error, not the summary. Then ask: what changed?*
2. **Tomcat starts but the app page returns 500 with a database connection error.**
   *Hint: Check the layer below the one you think is broken.*
3. **The Route 53 name resolves on one instance but not another.**
   *Hint: Compare a working case with the broken one and list every difference.*

## Cleanup

```bash
# Order matters: ASG before instances, or the ASG just recreates them.
aws autoscaling update-auto-scaling-group --auto-scaling-group-name vprofile-app-asg \
  --min-size 0 --desired-capacity 0
aws autoscaling delete-auto-scaling-group --auto-scaling-group-name vprofile-app-asg --force-delete
# Then: delete ALB, target group, terminate remaining instances, delete the hosted zone.
```
**What this does:** scales the ASG to zero before deleting it.
**Why:** deleting instances under a live ASG is pointless — it replaces them.
**Expected:** `aws ec2 describe-instances` shows nothing but terminated instances.

Finally run the standard sweep in `docs/cloud-cost-safety.md`.

## Interview questions

Answer these in writing in `answers.md` before you consider the lab finished.

1. Walk me through what happens when a user types your domain into a browser and the page loads.
2. Why did you put the database in a private subnet? What would break if it were public?
3. What is the difference between a security group and a NACL?
4. Your load balancer says a target is unhealthy but the app works. Where do you look first?
5. Why use Route 53 private records instead of just hard-coding IPs?
6. What would you change about this architecture before putting it in production?
