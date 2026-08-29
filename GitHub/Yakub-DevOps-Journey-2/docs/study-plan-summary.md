# Study plan summary (day by day)

Total scheduled video: **46h 33m** across lectures 119-378 (260 lectures).

## Week 1 (Sep 1-6) - AWS compute, storage and the Lift & Shift deployment

*Milestone: A multi-tier application running on AWS that you built and can explain, plus a clean AWS account afterwards.*

### Tuesday 01 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): AWS storage & load balancing (Lectures 119–122)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Attach and snapshot an EBS volume on a t3.micro; put two EC2s behind a Classic/Application Load Balancer and prove traffic alternates.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 119. EBS Snapshots — 15 min
- 120. ELB Introduction — 6 min
- 121. ELB Hands On Part 1 — 10 min
- 122. ELB Hands On Part 2 — 19 min

### Wednesday 02 September 2026

- **09:00-10:30** — Udemy: CloudWatch, EFS, Autoscaling, S3 (Lectures 123–127)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: CloudWatch, EFS, Autoscaling, S3 (Lectures 128)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Build a CloudWatch alarm on CPU, mount an EFS share across two instances, create a launch template + ASG (min 1 / max 2), create your first S3 bucket.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 123. Cloudwatch Introduction — 5 min
- 124. Cloudwatch Hands On — 19 min
- 125. EFS — 18 min
- 126. Autoscaling Group Introduction — 4 min
- 127. Autoscaling Group Hands On — 25 min
- 128. S3 Introduction — 22 min

### Thursday 03 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): S3 static hosting & RDS (Lectures 129–131)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Host a one-page site on S3, then launch a free-tier db.t3.micro MySQL RDS instance and connect to it from an EC2 over a security group rule.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 129. S3 Website Hosting — 12 min
- 130. More in S3 — 11 min
- 131. RDS — 26 min

### Friday 04 September 2026

- **09:00-10:30** — Udemy: Lift & Shift project setup (Lectures 132–135)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Lift & Shift project setup (Lectures 136–139)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Walk the whole Section 14 stack once, following the lectures exactly. Take notes on every security group rule - you will rebuild it unaided tomorrow.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 132. Introduction — 11 min
- 133. Security Group & Keypairs — 10 min
- 134. EC2 Instances — 19 min
- 135. DNS Route 53 — 7 min
- 136. Build and Deploy Artifacts — 16 min
- 137. Load Balancer & DNS — 11 min
- 138. Autoscaling Group — 12 min
- 139. Validate & Summarize — 7 min

### Saturday 05 September 2026

- **09:00-11:00** — LAB 1: Lift & Shift: multi-tier vProfile stack on AWS EC2 - build phase  
  Rebuild the Section 14 architecture from scratch WITHOUT replaying the videos: MySQL, Memcached and RabbitMQ on private EC2s, Tomcat app EC2, Nginx web EC2, an Application Load Balancer in front, a Route 53 record, and an Autoscaling Group for the app tier. Everything free-tier sized.
- **11:00-11:15** — Break
- **11:15-13:00** — LAB 1: Lift & Shift: multi-tier vProfile stack on AWS EC2 - continue  
  Keep going. Note every error message you hit.
- **13:00-14:00** — Lunch
- **14:00-15:45** — LAB 1: verification & deliberate breakage  
  Verify against the acceptance criteria in the lab README, then work the troubleshooting challenges.
- **15:45-16:30** — Cleanup & cost check  
  Destroy or stop every billable resource. Check the AWS Billing dashboard before you stop.
- **16:30-17:00** — Commit + LinkedIn lab report  
  Today's post should describe what you BUILT, with a screenshot as evidence.

### Sunday 06 September 2026

- **10:00-12:00** — Finish, test and troubleshoot the week's lab  
  Finish and document Lab 1. Draw the lift-and-shift architecture by hand, photograph or redraw it digitally, and record a 5-minute walkthrough.
- **12:00-13:00** — Documentation: README, diagram, screenshots  
  Update the lab README: objective, architecture, steps, verification, troubleshooting, cleanup.
- **13:00-14:00** — Lunch / rest
- **14:00-15:00** — Explain the week's project out loud  
  Answer all six questions aloud and record it: What did I build? Why? How does it work? What broke? How did I troubleshoot it? What would I improve?
- **15:00-15:30** — Weekly reflection + LinkedIn summary post  
  One weekly post that ties the week together, with your best evidence attached.

## Week 2 (Sep 7-13) - Re-architecting on PAAS/SAAS, Maven, and Jenkins CI

*Milestone: A Jenkinsfile in your repo that builds, tests, analyses and publishes an artifact automatically.*

### Monday 07 September 2026

- **09:00-10:30** — Udemy: Re-architecting on PAAS/SAAS (Lectures 140–146)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Re-architecting on PAAS/SAAS (Lectures 147–150)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Deploy the app to Elastic Beanstalk backed by RDS, ElastiCache and Amazon MQ. Front it with CloudFront. DESTROY EVERYTHING before you close the laptop.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 140. Introduction — 13 min
- 141. Security Group And Keypairs — 4 min
- 142. RDS — 11 min
- 143. Elastic Cache — 5 min
- 144. Amazon MQ — 3 min
- 145. DB Initialization — 7 min
- 146. Beanstalk — 19 min
- 147. Update on Security Group & ELB — 2 min
- 148. Build & Deploy Artifact — 13 min
- 149. Cloud front — 9 min
- 150. Validate and Summarize — 8 min

### Tuesday 08 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): Build tools - Maven (Lectures 151–153)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Clone the vProfile source, run `mvn clean install`, find the produced .war in target/ and explain what each Maven lifecycle phase did.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 151. Introduction — 9 min
- 152. Maven Hands-on — 24 min
- 153. Maven, NodeJS & AI — 12 min

### Wednesday 09 September 2026

- **09:00-10:30** — Udemy: Jenkins install & first jobs (Lectures 154–158)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Jenkins install & first jobs (Lectures 159–161)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Install Jenkins on an Ubuntu EC2, add JDK + Maven as global tools, create a freestyle job that builds the vProfile war, then add a build agent.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 154. Introduction — 6 min
- 155. Installation — 13 min
- 156. Freestyle Vs Pipeline As A Code — 2 min
- 157. Installing tools in Jenkins — 7 min
- 158. First Job — 8 min
- 159. First Build Job — 11 min
- 160. Agents — 13 min
- 161. Plugins, Versioning & more — 12 min

### Thursday 10 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): CI flow, Nexus & SonarQube setup (Lectures 162–166)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Stand up Nexus and SonarQube servers. Keep them t3.small or smaller and STOP them when you finish.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 162. Disk Space Issue — 3 min
- 163. Flow of Continuous Integration Pipeline — 5 min
- 164. Steps for Continuous Integration Pipeline — 2 min
- 165. Jenkins, Nexus & Sonarqube Setup — 13 min
- 166. Plugins for CI — 1 min

### Friday 11 September 2026

- **09:00-10:30** — Udemy: Pipeline as code, quality gates, Slack (Lectures 167–169)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Pipeline as code, quality gates, Slack (Lectures 170–173)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Write your first Jenkinsfile: Build -> Test -> Code Analysis -> Quality Gate -> Upload artifact to Nexus -> Slack notification.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 167. Pipeline As A Code Introduction — 18 min
- 168. Code Analysis — 7 min
- 169. Code Analysis Demonstration — 14 min
- 170. Quality Gates — 7 min
- 171. Software Repositories Intro (Nexus) — 5 min
- 172. Nexus PAAC Demo — 9 min
- 173. Notification, Slack — 12 min

### Saturday 12 September 2026

- **09:00-11:00** — LAB 2: Jenkins Continuous Integration pipeline with quality gates - build phase  
  Build a complete CI pipeline as code for the vProfile app: checkout, Maven build, unit tests, Checkstyle, SonarQube analysis with a quality gate that can FAIL the build, artifact upload to Nexus, and a Slack notification on both success and failure.
- **11:00-11:15** — Break
- **11:15-13:00** — LAB 2: Jenkins Continuous Integration pipeline with quality gates - continue  
  Keep going. Note every error message you hit.
- **13:00-14:00** — Lunch
- **14:00-15:45** — LAB 2: verification & deliberate breakage  
  Verify against the acceptance criteria in the lab README, then work the troubleshooting challenges.
- **15:45-16:30** — Cleanup & cost check  
  Destroy or stop every billable resource. Check the AWS Billing dashboard before you stop.
- **16:30-17:00** — Commit + LinkedIn lab report  
  Today's post should describe what you BUILT, with a screenshot as evidence.

### Sunday 13 September 2026

- **10:00-12:00** — Finish, test and troubleshoot the week's lab  
  Finish and document Lab 2. Record a screen capture of the pipeline running green, and a second one of it failing the quality gate on purpose.
- **12:00-13:00** — Documentation: README, diagram, screenshots  
  Update the lab README: objective, architecture, steps, verification, troubleshooting, cleanup.
- **13:00-14:00** — Lunch / rest
- **14:00-15:00** — Explain the week's project out loud  
  Answer all six questions aloud and record it: What did I build? Why? How does it work? What broke? How did I troubleshoot it? What would I improve?
- **15:00-15:30** — Weekly reflection + LinkedIn summary post  
  One weekly post that ties the week together, with your best evidence attached.

## Week 3 (Sep 14-20) - Jenkins CD, GitHub Actions, GitLab CI, Python foundations

*Milestone: The same pipeline expressed three ways (Jenkins, GitHub Actions, GitLab) and a written comparison.*

### Monday 14 September 2026

- **09:00-10:30** — Udemy: Jenkins CI/CD to Docker & ECS (Lectures 174–180)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Jenkins CI/CD to Docker & ECS (Lectures 181–184)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Extend the Jenkinsfile to build a Docker image and push it, then deploy to ECS. Configure a webhook build trigger and lock the instance down with matrix authorisation.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 174. CI for Docker | Intro — 2 min
- 175. Docker PAAC Prereqs info — 9 min
- 176. Docker PAAC Demo — 15 min
- 177. Docker CICD Intro — 4 min
- 178. Docker CICD Code — 2 min
- 179. AWS ECS Setup — 13 min
- 180. Docker CICD Demonstration — 5 min
- 181. Cleanup — 2 min
- 182. Build Triggers Intro — 14 min
- 183. Build Triggers Demo — 18 min
- 184. Authentication & Authorization — 14 min

### Tuesday 15 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): GitHub Actions quickstart (Lectures 185–188)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Write .github/workflows/ci.yml that runs on push to a feature branch and on pull_request, and prove both triggers fire.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 185. Introduction — 5 min
- 186. Quickstart Part1 — 16 min
- 187. Quickstart Part2 — 9 min
- 188. Triggers and Inputs — 13 min

### Wednesday 16 September 2026

- **09:00-10:30** — Udemy: Actions artifacts/security + GitLab start (Lectures 189–192)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Actions artifacts/security + GitLab start (Lectures 193–195)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Add an artifact upload and a security scan job to the Actions workflow. Then create a GitLab account and run your first .gitlab-ci.yml.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 189. Artifacts, Conditions & Repo Permissions — 8 min
- 190. Security Scan — 7 min
- 191. Secrets & Docker — 7 min
- 192. Build & Publish Job — 13 min
- 193. Introduction — 5 min
- 194. Initial Setup — 13 min
- 195. First Pipeline — 10 min

### Thursday 17 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): GitLab variables, rules, Docker (Lectures 196–199)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Move a hard-coded value into a masked GitLab CI/CD variable, and add a rule so the deploy stage only runs on the main branch.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 196. Variables & More — 10 min
- 197. Triggers & Rules — 12 min
- 198. Security & Artifacts — 15 min
- 199. Build And Publish Docker — 11 min

### Friday 18 September 2026

- **09:00-10:30** — Udemy: Python foundations for DevOps (Lectures 200–203)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Python foundations for DevOps (Lectures 204–206)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Write and run five small scripts covering variables, string slicing, operators and conditions. Commit them to labs/python/.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 200. Introduction — 10 min
- 201. Python on Linux, Versions & Indentation — 10 min
- 202. Quotes and Comments — 4 min
- 203. Variables — 15 min
- 204. Print Format — 5 min
- 205. Slicing — 16 min
- 206. Operators — 17 min

### Saturday 19 September 2026

- **09:00-11:00** — LAB 3: GitHub Actions CI/CD with security scanning and secrets - build phase  
  Port the Jenkins pipeline to GitHub Actions, then reproduce the core of it a third time in GitLab CI. Build the app, scan it, build and publish a Docker image, and gate deployment behind a branch rule. Write a short comparison of the three tools.
- **11:00-11:15** — Break
- **11:15-13:00** — LAB 3: GitHub Actions CI/CD with security scanning and secrets - continue  
  Keep going. Note every error message you hit.
- **13:00-14:00** — Lunch
- **14:00-15:45** — LAB 3: verification & deliberate breakage  
  Verify against the acceptance criteria in the lab README, then work the troubleshooting challenges.
- **15:45-16:30** — Cleanup & cost check  
  Destroy or stop every billable resource. Check the AWS Billing dashboard before you stop.
- **16:30-17:00** — Commit + LinkedIn lab report  
  Today's post should describe what you BUILT, with a screenshot as evidence.

### Sunday 20 September 2026

- **10:00-12:00** — Finish, test and troubleshoot the week's lab  
  Finish and document Lab 3. Write the Jenkins vs GitHub Actions vs GitLab comparison properly - this is a common interview question.
- **12:00-13:00** — Documentation: README, diagram, screenshots  
  Update the lab README: objective, architecture, steps, verification, troubleshooting, cleanup.
- **13:00-14:00** — Lunch / rest
- **14:00-15:00** — Explain the week's project out loud  
  Answer all six questions aloud and record it: What did I build? Why? How does it work? What broke? How did I troubleshoot it? What would I improve?
- **15:00-15:30** — Weekly reflection + LinkedIn summary post  
  One weekly post that ties the week together, with your best evidence attached.

## Week 4 (Sep 21-27) - Python automation with Boto3, and Terraform

*Milestone: Infrastructure you can create and destroy with two commands, plus a Python tool that audits your own AWS account.*

### Monday 21 September 2026

- **09:00-10:30** — Udemy: Python control flow, functions, modules (Lectures 207–210)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Python control flow, functions, modules (Lectures 211–213)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Refactor yesterday's five scripts into one module with functions. No copy-paste duplication allowed.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 207. Conditions — 15 min
- 208. Loops — 14 min
- 209. Break & Continue — 12 min
- 210. Built-in Functions or Methods — 17 min
- 211. Functions part-1 — 17 min
- 212. Functions part-2 — 11 min
- 213. Modules — 7 min

### Tuesday 22 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): OS tasks & Python Fabric (Lectures 214–215)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Write a script that reads /var/log, filters error lines and writes a summary file. Then use Fabric to run `uptime` on a remote EC2.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 214. OS Tasks — 23 min
- 215. Python Fabric — 32 min

### Wednesday 23 September 2026

- **09:00-10:30** — Udemy: Boto3, AI-assisted automation, Terraform basics (Lectures 216–219)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Boto3, AI-assisted automation, Terraform basics (Lectures 220–223)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Write a Boto3 script that lists every running EC2 with its tags and flags any without an Owner tag. Then write your first main.tf.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 216. Exception Handling — 10 min
- 217. Cloud Interaction with Boto3 — 11 min
- 218. AI for Cloud Automation — 17 min
- 219. Copilot AI for Cloud Automation — 14 min
- 220. Python Scripts — 0 min
- 221. Introduction — 7 min
- 222. Basics of Terraform — 16 min
- 223. Code Structure — 17 min

### Thursday 24 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): Terraform code structure & variables (Lectures 224–226)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Split your main.tf into main.tf / variables.tf / outputs.tf and parameterise the AMI and instance type.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 224. Code Structure Part 2 — 6 min
- 225. Plan, Apply, Update & Destroy — 17 min
- 226. Variables — 13 min

### Friday 25 September 2026

- **09:00-10:30** — Udemy: Provisioners, outputs, backend + Ansible intro (Lectures 227–231)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Provisioners, outputs, backend + Ansible intro (Lectures 232–233)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Move Terraform state to an S3 backend. Then install Ansible and ping two Terraform-created EC2s from an inventory file.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 227. Provisioners — 10 min
- 228. Outputs — 5 min
- 229. Backend — 5 min
- 230. What Next? — 2 min
- 231. Introduction — 16 min
- 232. Setup Ansible & Infra — 11 min
- 233. Inventory & Ping Module — 14 min

### Saturday 26 September 2026

- **09:00-11:00** — LAB 4: Terraform-provisioned infrastructure with Python/Boto3 automation - build phase  
  Replace all manual clicking with code. Write Terraform that provisions the app tier (EC2s, security groups, key pair, S3 bucket, remote state backend) and a Python/Boto3 tool that audits the account: lists running instances, flags untagged resources, and reports estimated monthly cost of what is running.
- **11:00-11:15** — Break
- **11:15-13:00** — LAB 4: Terraform-provisioned infrastructure with Python/Boto3 automation - continue  
  Keep going. Note every error message you hit.
- **13:00-14:00** — Lunch
- **14:00-15:45** — LAB 4: verification & deliberate breakage  
  Verify against the acceptance criteria in the lab README, then work the troubleshooting challenges.
- **15:45-16:30** — Cleanup & cost check  
  Destroy or stop every billable resource. Check the AWS Billing dashboard before you stop.
- **16:30-17:00** — Commit + LinkedIn lab report  
  Today's post should describe what you BUILT, with a screenshot as evidence.

### Sunday 27 September 2026

- **10:00-12:00** — Finish, test and troubleshoot the week's lab  
  Finish and document Lab 4. Run `terraform destroy`, then run your Boto3 auditor and paste the empty output into the README as proof of cleanup.
- **12:00-13:00** — Documentation: README, diagram, screenshots  
  Update the lab README: objective, architecture, steps, verification, troubleshooting, cleanup.
- **13:00-14:00** — Lunch / rest
- **14:00-15:00** — Explain the week's project out loud  
  Answer all six questions aloud and record it: What did I build? Why? How does it work? What broke? How did I troubleshoot it? What would I improve?
- **15:00-15:30** — Weekly reflection + LinkedIn summary post  
  One weekly post that ties the week together, with your best evidence attached.

## Week 5 (Sep 28-Oct 4) - Ansible configuration management and observability

*Milestone: A server you never configured by hand, and a dashboard that tells you when it breaks.*

### Monday 28 September 2026

- **09:00-10:30** — Udemy: Ansible inventory, ad hoc, playbooks (Lectures 234–237)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Ansible inventory, ad hoc, playbooks (Lectures 238–239)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Write a playbook that installs Nginx, copies a custom index.html and starts the service on both hosts. Run it twice and explain idempotency.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 234. Inventory Part 2 — 19 min
- 235. YAML & JSON — 9 min
- 236. Ad Hoc Commands — 12 min
- 237. Playbook & Modules — 21 min
- 238. Modules - Find, Use, Troubleshoot & Repeat — 20 min
- 239. Ansible Configuration — 11 min

### Tuesday 29 September 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): Ansible variables & facts (Lectures 240–242)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Convert hard-coded values in your playbook into group_vars, then print three fact variables with the debug module.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 240. Variables & Debug — 14 min
- 241. Group & Host Variables — 15 min
- 242. Fact Variables — 11 min

### Wednesday 30 September 2026

- **09:00-10:30** — Udemy: Conditionals, loops, templates, roles, AWS (Lectures 243–247)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Conditionals, loops, templates, roles, AWS (Lectures 248)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Refactor the Nginx playbook into a proper role (tasks/handlers/templates/vars) and template the config file with Jinja2.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 243. Decision Making — 12 min
- 244. Loops — 6 min
- 245. File, copy & template modules — 20 min
- 246. Handlers — 7 min
- 247. Roles — 31 min
- 248. Ansible for AWS — 20 min

### Thursday 01 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): vProfile Ansible code + monitoring intro (Lectures 249–252)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Read the vProfile Ansible code and map each role to something you already built by hand in Week 1.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 249. Vprofile code — 0 min
- 250. Introduction to Monitoring — 15 min
- 251. Why Monitoring is Essential for DevOps — 3 min
- 252. Monitoring and Observability Tools — 13 min

### Friday 02 October 2026

- **09:00-10:30** — Udemy: Prometheus, node exporter, PromQL, Grafana (Lectures 253–255)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Prometheus, node exporter, PromQL, Grafana (Lectures 256–258)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Install Prometheus + node_exporter on one EC2 and Grafana alongside it. Query node_cpu_seconds_total in PromQL and connect Grafana.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 253. Setting Up the Monitoring Environment — 15 min
- 254. Loki and Web Server Setup — 20 min
- 255. Adding a Node to Prometheus — 16 min
- 256. Understanding PromQL (Prometheus Query Language) — 16 min
- 257. Connecting Grafana & Prometheus — 7 min
- 258. Integrating Slack for Notifications — 4 min

### Saturday 03 October 2026

- **09:00-10:00** — Udemy: Grafana dashboards, alerts, Loki (Lectures 259–262)  
  SATURDAY LECTURES (justified): these four are the dashboard/alerting build itself - watching them inside the lab is more effective than watching them a day early.
- **10:00-13:00** — LAB 5: Ansible configuration management + Prometheus/Grafana observability - build phase  
  Provision infrastructure with Terraform, configure it entirely with Ansible roles, and monitor it with Prometheus, Grafana, node_exporter and Loki. Build a real dashboard and a real alert that fires to Slack.
- **13:00-14:00** — Lunch
- **14:00-15:45** — LAB 5: verification & deliberate breakage  
  Verify against the acceptance criteria in the lab README, then work the troubleshooting challenges.
- **15:45-16:30** — Cleanup & cost check  
  Destroy or stop every billable resource. Check the AWS Billing dashboard before you stop.
- **16:30-17:00** — Commit + LinkedIn lab report  
  Today's post should describe what you BUILT, with a screenshot as evidence.

**Lectures:**

- 259. PromQL for Grafana Dashboards — 12 min
- 260. Building Grafana Panels and Dashboards — 17 min
- 261. Creating Alerts and Thresholds — 11 min
- 262. Integrating Loki and Alloy for Logs and Metrics — 13 min

### Sunday 04 October 2026

- **10:00-12:00** — Finish, test and troubleshoot the week's lab  
  Finish and document Lab 5. Export your Grafana dashboard JSON into the repo so anyone can import it. Mid-point review: are you on track?
- **12:00-13:00** — Documentation: README, diagram, screenshots  
  Update the lab README: objective, architecture, steps, verification, troubleshooting, cleanup.
- **13:00-14:00** — Lunch / rest
- **14:00-15:00** — Explain the week's project out loud  
  Answer all six questions aloud and record it: What did I build? Why? How does it work? What broke? How did I troubleshoot it? What would I improve?
- **15:00-15:30** — Weekly reflection + LinkedIn summary post  
  One weekly post that ties the week together, with your best evidence attached.

## Week 6 (Oct 5-11) - VPC networking, AWS-native CI/CD, and Google Cloud

*Milestone: A production-shaped private network, and an application deployed into it by a pipeline you did not touch.*

### Monday 05 October 2026

- **09:00-10:30** — Udemy: VPC design and components (Lectures 263–265)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: VPC design and components (Lectures 266–272)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Draw the target VPC on paper first: 2 public + 2 private subnets, IGW, NAT, route tables. Then build it in the console.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 263. VPC Introduction — 28 min
- 264. VPC Design & Components — 9 min
- 265. VPC Setup Details — 4 min
- 266. Default VPC — 7 min
- 267. Create VPC — 6 min
- 268. Subnets — 3 min
- 269. Internet Gateway — 2 min
- 270. Route Tables — 4 min
- 271. NAT Gateway — 6 min
- 272. [TITLE NOT READABLE IN SCREENSHOT] — 8 min

### Tuesday 06 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): Website in VPC, peering, Terraform VPC (Lectures 273–275)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Recreate today's VPC in Terraform. Compare the console version with the code version - which one could you rebuild in 5 minutes?
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 273. Website in VPC — 14 min
- 274. Peering — 11 min
- 275. Terraform for VPC Setup — 13 min

### Wednesday 07 October 2026

- **09:00-10:30** — Udemy: EC2 logs, Lambda, AWS CI/CD project (Lectures 276–284)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: EC2 logs, Lambda, AWS CI/CD project (Lectures 285–287)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Build the CodeCommit -> CodeBuild -> CodePipeline -> Beanstalk pipeline end to end. Delete the pipeline and Beanstalk env afterwards.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 276. Ec2 Logs — 31 min
- 277. AWS Lambda — 19 min
- 278. Links — 0 min
- 279. buildspec — 0 min
- 280. Links — 0 min
- 281. S3 policy — 0 min
- 282. Introduction — 4 min
- 283. Beanstalk — 7 min
- 284. RDS & App Setup on Beanstalk — 12 min
- 285. Code Commit — 14 min
- 286. Code build — 22 min
- 287. Build, Deploy & Code Pipeline — 14 min

### Thursday 08 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): GCP vProfile project intro (Lectures 288–291)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Create a GCP free-trial project, install gcloud, and set your project/region defaults. Do not enable billing-heavy APIs you do not need.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 288. Introduction to the GCP vProfile Project — 11 min
- 289. Project Architecture Overview — 7 min
- 290. Setting Up Your GCP Account & Project — 6 min
- 291. Commands in the Source Code — 6 min

### Friday 09 October 2026

- **09:00-10:30** — Udemy: GCP network, Cloud SQL, MIG, LB, DNS (Lectures 292–296)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: GCP network, Cloud SQL, MIG, LB, DNS (Lectures 297–301)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Complete the GCP deployment and then run the Section 301 cleanup in full. Verify in the billing console that nothing is still running.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 292. Configuring Project Variables — 7 min
- 293. VPC, Subnets & Network Setup — 9 min
- 294. Firewall Rules & VM Deployment — 14 min
- 295. Configuring Cloud SQL & Memorystore — 11 min
- 296. Setting Up Cloud DNS — 8 min
- 297. Creating a Custom VM Image — 11 min
- 298. Building a Managed Instance Group (MIG) — 5 min
- 299. Configuring the Global HTTP/HTTPS Load Balancer — 11 min
- 300. SSL Certificates, HTTPS & Final DNS Setup — 9 min
- 301. Summary and Cleanup — 8 min

### Saturday 10 October 2026

- **09:00-11:00** — LAB 6: Production-style VPC + AWS-native CI/CD pipeline - build phase  
  Build a proper three-tier VPC in Terraform (public/private subnets across two AZs, IGW, NAT gateway, route tables, bastion) and deploy the application into it through an AWS-native CodeCommit/CodeBuild/CodePipeline flow.
- **11:00-11:15** — Break
- **11:15-13:00** — LAB 6: Production-style VPC + AWS-native CI/CD pipeline - continue  
  Keep going. Note every error message you hit.
- **13:00-14:00** — Lunch
- **14:00-15:45** — LAB 6: verification & deliberate breakage  
  Verify against the acceptance criteria in the lab README, then work the troubleshooting challenges.
- **15:45-16:30** — Cleanup & cost check  
  Destroy or stop every billable resource. Check the AWS Billing dashboard before you stop.
- **16:30-17:00** — Commit + LinkedIn lab report  
  Today's post should describe what you BUILT, with a screenshot as evidence.

### Sunday 11 October 2026

- **10:00-12:00** — Finish, test and troubleshoot the week's lab  
  Finish and document Lab 6. Redraw the VPC diagram from memory without looking at your notes - if you cannot, you have not learned it yet.
- **12:00-13:00** — Documentation: README, diagram, screenshots  
  Update the lab README: objective, architecture, steps, verification, troubleshooting, cleanup.
- **13:00-14:00** — Lunch / rest
- **14:00-15:00** — Explain the week's project out loud  
  Answer all six questions aloud and record it: What did I build? Why? How does it work? What broke? How did I troubleshoot it? What would I improve?
- **15:00-15:30** — Weekly reflection + LinkedIn summary post  
  One weekly post that ties the week together, with your best evidence attached.

## Week 7 (Oct 12-18) - Docker and full containerization

*Milestone: The entire application stack running from a single `docker compose up`, with published images.*

### Monday 12 October 2026

- **09:00-10:30** — Udemy: Docker engine, commands, logs, volumes (Lectures 302–304)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Docker engine, commands, logs, volumes (Lectures 305–306)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Run Nginx in a container, break it deliberately, read the logs, then attach a named volume and prove data survives a container delete.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 302. Introduction — 10 min
- 303. Docker Setup — 9 min
- 304. Docker commands & concepts — 22 min
- 305. Docker Logs — 8 min
- 306. Docker volumes — 17 min

### Tuesday 13 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): Building images, ENTRYPOINT vs CMD (Lectures 307–308)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Write a Dockerfile for a tiny app. Change ENTRYPOINT to CMD and back, and write down in your notes what actually changed.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 307. Building images — 21 min
- 308. Entrypoint and CMD — 7 min

### Wednesday 14 October 2026

- **09:00-10:30** — Udemy: Compose, multi-stage, base images, Dockerhub (Lectures 309–311)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Compose, multi-stage, base images, Dockerhub (Lectures 312–315)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Write a multi-stage Dockerfile that builds the war in one stage and copies only the artifact into a slim runtime stage. Compare image sizes.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 309. Docker Compose — 15 min
- 310. Multi Stage Dockerfile — 10 min
- 311. Introduction — 10 min
- 312. Overview of Base Image — 9 min
- 313. Dockerhub Setup — 3 min
- 314. Setup Docker Engine — 6 min
- 315. Dockerhub & Dockerfile References — 7 min

### Thursday 15 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): App, DB and Web image Dockerfiles (Lectures 316–318)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Build all three vProfile images locally and push them to your Docker Hub account under your own namespace.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 316. App Image Dockerfile — 10 min
- 317. DB Image Dockerfile — 7 min
- 318. Web Image Dockerfile — 6 min

### Friday 16 October 2026

- **09:00-10:30** — Udemy: Compose stack + microservice containerization (Lectures 319–321)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Compose stack + microservice containerization (Lectures 322–323)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Bring the entire stack up with one `docker compose up -d`, then containerize the microservice project.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 319. Docker Compose — 19 min
- 320. Build and Run — 11 min
- 321. Summarize — 6 min
- 322. Containerizing Microservice Project — 22 min
- 323. Build & Run Microservice App — 12 min

### Saturday 17 October 2026

- **09:00-11:00** — LAB 7: Full containerization of the multi-tier application - build phase  
  Containerize every tier: a multi-stage Dockerfile for the Java app, a custom DB image with the schema pre-loaded, an Nginx web image, plus Memcached and RabbitMQ. Bring the whole thing up with one docker compose command and publish the images.
- **11:00-11:15** — Break
- **11:15-13:00** — LAB 7: Full containerization of the multi-tier application - continue  
  Keep going. Note every error message you hit.
- **13:00-14:00** — Lunch
- **14:00-15:45** — LAB 7: verification & deliberate breakage  
  Verify against the acceptance criteria in the lab README, then work the troubleshooting challenges.
- **15:45-16:30** — Cleanup & cost check  
  Destroy or stop every billable resource. Check the AWS Billing dashboard before you stop.
- **16:30-17:00** — Commit + LinkedIn lab report  
  Today's post should describe what you BUILT, with a screenshot as evidence.

### Sunday 18 October 2026

- **10:00-12:00** — Finish, test and troubleshoot the week's lab  
  Finish and document Lab 7. Then WRITE THE CAPSTONE PLAN: architecture diagram, repo layout, and the order you will build it in next week.
- **12:00-13:00** — Documentation: README, diagram, screenshots  
  Update the lab README: objective, architecture, steps, verification, troubleshooting, cleanup.
- **13:00-14:00** — Lunch / rest
- **14:00-15:00** — Explain the week's project out loud  
  Answer all six questions aloud and record it: What did I build? Why? How does it work? What broke? How did I troubleshoot it? What would I improve?
- **15:00-15:30** — Weekly reflection + LinkedIn summary post  
  One weekly post that ties the week together, with your best evidence attached.

## Week 8 (Oct 19-25) - Kubernetes and Helm - capstone phase 1

*Milestone: The application running on Kubernetes from a Helm chart, on a cluster created by Terraform.*

### Monday 19 October 2026

- **09:00-10:30** — Udemy: Kubernetes intro, Minikube, Kops, kubeconfig (Lectures 324–326)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Kubernetes intro, Minikube, Kops, kubeconfig (Lectures 327–328)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Get a working Minikube cluster and run `kubectl get nodes`. Understand your kubeconfig before touching a cloud cluster.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 324. Introduction — 23 min
- 325. Minikube for K8s Setup — 9 min
- 326. Kops for K8s Setup — 23 min
- 327. Objects and Documentation — 5 min
- 328. Kube Config — 10 min

### Tuesday 20 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): Pods, namespaces, logging (Lectures 329–331)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Create a pod from YAML, put it in its own namespace, then deliberately mistype the image name and read the resulting event stream.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 329. Pods — 11 min
- 330. Namespace — 8 min
- 331. Different levels of Logging — 9 min

### Wednesday 21 October 2026

- **09:00-10:30** — Udemy: Services, ReplicaSets, Deployments, ConfigMaps (Lectures 332–334)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Services, ReplicaSets, Deployments, ConfigMaps (Lectures 335–337)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Deploy 3 replicas behind a ClusterIP service, roll out an image change, then roll it back with `kubectl rollout undo`.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 332. Service — 21 min
- 333. Replica Set — 11 min
- 334. Deployment — 12 min
- 335. Command and Arguments — 7 min
- 336. Volumes — 9 min
- 337. Config Map — 15 min

### Thursday 22 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): Secrets and Ingress (Lectures 338–339)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Create a secret from a literal, mount it as an env var, and expose a deployment through an Ingress.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 338. Secret — 12 min
- 339. Ingress — 19 min

### Friday 23 October 2026

- **09:00-10:30** — Udemy: kubectl CLI, Helm, Lens, Terraform for EKS (Lectures 340–343)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: kubectl CLI, Helm, Lens, Terraform for EKS (Lectures 344–346)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Package one of your deployments as a Helm chart with values.yaml. Read (do not yet apply) the Terraform EKS module.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 340. Kubectl CLI & Cheatsheet — 12 min
- 341. Extras — 13 min
- 342. Helm Introduction — 6 min
- 343. Helm Hands On — 20 min
- 344. Helm with AI — 19 min
- 345. Lens — 7 min
- 346. Terraform For EKS Setup — 25 min

### Saturday 24 October 2026

- **09:00-11:00** — LAB 8: Kubernetes deployment with Helm - CAPSTONE PHASE 1 - build phase  
  This lab is the first phase of your capstone. Provision an EKS cluster with Terraform (or run on Minikube if you want to avoid EKS cost), package the application as a Helm chart, and deploy it with secrets, persistent volumes, services and an Ingress.
- **11:00-11:15** — Break
- **11:15-13:00** — LAB 8: Kubernetes deployment with Helm - CAPSTONE PHASE 1 - continue  
  Keep going. Note every error message you hit.
- **13:00-14:00** — Lunch
- **14:00-15:45** — LAB 8: verification & deliberate breakage  
  Verify against the acceptance criteria in the lab README, then work the troubleshooting challenges.
- **15:45-16:30** — Cleanup & cost check  
  Destroy or stop every billable resource. Check the AWS Billing dashboard before you stop.
- **16:30-17:00** — Commit + LinkedIn lab report  
  Today's post should describe what you BUILT, with a screenshot as evidence.

### Sunday 25 October 2026

- **10:00-12:00** — Finish, test and troubleshoot the week's lab  
  Finish Lab 8 / capstone phase 1. Confirm the cluster comes up from `terraform apply` alone. Prepare the capstone build checklist for the final week.
- **12:00-13:00** — Documentation: README, diagram, screenshots  
  Update the lab README: objective, architecture, steps, verification, troubleshooting, cleanup.
- **13:00-14:00** — Lunch / rest
- **14:00-15:00** — Explain the week's project out loud  
  Answer all six questions aloud and record it: What did I build? Why? How does it work? What broke? How did I troubleshoot it? What would I improve?
- **15:00-15:30** — Weekly reflection + LinkedIn summary post  
  One weekly post that ties the week together, with your best evidence attached.

## Week 9 (Oct 26-31) - App on Kubernetes, GitOps, and the capstone

*Milestone: A complete GitOps capstone: commit to Git, and the change reaches a live Kubernetes cluster on its own.*

### Monday 26 October 2026

- **09:00-10:30** — Udemy: vProfile on Kubernetes - secrets, PVC, services (Lectures 347–352)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: vProfile on Kubernetes - secrets, PVC, services (Lectures 353–356)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  Apply the full manifest set to your cluster and debug until every pod is Running. Expect failures - that is the point.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 347. Introduction — 5 min
- 348. Architecture — 7 min
- 349. Source Code Overview — 5 min
- 350. Secret — 5 min
- 351. Persistent Volume for DB [PVC] — 4 min
- 352. MySQL App — 10 min
- 353. MySQL Service — 4 min
- 354. Memcache App & Service — 4 min
- 355. RabbitMQ App & Service — 5 min
- 356. Tomcat App & Service — 7 min

### Tuesday 27 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): Ingress and full cluster deployment (Lectures 357–360)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  Reach the app in a browser through the Ingress. Screenshot it - this goes in the capstone README.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 357. Ingress — 6 min
- 358. K8s Cluster Setup & Source Code — 4 min
- 359. Deploy App on K8s Cluster — 12 min
- 360. Summarize — 4 min

### Wednesday 28 October 2026

- **09:00-10:30** — Udemy: GitOps project: Helm charts, CI pipeline, ECR (Lectures 361–367)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: GitOps project: Helm charts, CI pipeline, ECR (Lectures 368–371)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  CAPSTONE BUILD: repo structure, Helm charts, SonarQube, ECR + IAM, GitHub secrets, CI/CD pipeline parts 1 and 2.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 361. Introduction — 6 min
- 362. Architecture — 6 min
- 363. Git Repository Setup — 6 min
- 364. Helm Charts Part 1 — 3 min
- 365. Helm Charts Part 2 — 13 min
- 366. CI Pipeline Overview — 3 min
- 367. Sonar Qube Server — 6 min
- 368. ECR and IAM — 6 min
- 369. Github Secrets & Variables — 6 min
- 370. CICD Pipeline part 1 — 12 min
- 371. CICD Pipeline part 2 — 10 min

### Thursday 29 October 2026

- **09:00-13:00** — Tech365 in-person DevOps class  
  Fixed commitment - no Udemy work during this block.
- **13:00-14:00** — Lunch and reset
- **14:00-15:00** — Udemy (light): EKS prereqs, Terraform EKS, Argo CD (Lectures 372–375)  
  Lighter load today by design. Quality of attention beats volume.
- **15:00-16:00** — Short practical reinforcement  
  CAPSTONE BUILD: provision EKS with Terraform, install Argo CD, connect it to your Helm chart repo and watch it sync.
- **16:00-16:30** — Revision & buffer  
  Re-run one thing from earlier in the week from memory, without notes. If you cannot, that is what you revise. Also absorbs any slippage from Monday/Wednesday.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Short post is fine on Tech365 days - one thing learned, one thing built.

**Lectures:**

- 372. EKS Prereqs — 5 min
- 373. Terraform Code for EKS — 10 min
- 374. Argo CD Setup — 11 min
- 375. Argo App Sync — 19 min

### Friday 30 October 2026

- **09:00-10:30** — Udemy: Completing the setup, summary, resumes (Lectures 376–377)  
  Watch actively: pause after each lecture and write one sentence in your notes about what it does and when you would use it.
- **10:30-10:45** — Break  
  Stand up, leave the screen.
- **10:45-12:15** — Udemy: Completing the setup, summary, resumes (Lectures 378)  
  Same rule: no passive watching. If a lecture is a demo, follow along in your own terminal.
- **12:15-13:15** — Lunch
- **13:15-15:15** — Hands-on practice  
  CAPSTONE BUILD: finish the end-to-end flow, then update your CV with the project while it is fresh.
- **15:15-15:30** — Break
- **15:30-16:30** — Troubleshooting & revision  
  Break something on purpose, then fix it. Write the symptom, the cause and the fix in docs/troubleshooting-log.md.
- **16:30-17:00** — Commit to GitHub + LinkedIn report  
  Push today's work, then publish the LinkedIn post using linkedin-report-template.md.

**Lectures:**

- 376. Completing the whole Setup — 10 min
- 377. Summary — 9 min
- 378. Resumes — 6 min

### Saturday 31 October 2026

- **09:00-11:00** — CAPSTONE: final end-to-end run  
  Destroy everything and rebuild the entire capstone from your own code and README. If it does not come up, your documentation is not finished.
- **11:00-11:15** — Break
- **11:15-13:00** — CAPSTONE: monitoring, screenshots, diagram  
  Grafana dashboard live, Argo CD sync screenshot, architecture diagram final version.
- **13:00-14:00** — Lunch
- **14:00-15:30** — CAPSTONE: README, demo script, interview answers  
  Write the demo instructions so a stranger can reproduce it. Answer all six explanation questions in writing.
- **15:30-16:30** — Final presentation - record it  
  Record a 10-15 minute walkthrough of the whole two months. This is your portfolio centrepiece.
- **16:30-17:00** — Final LinkedIn post + tear down all cloud resources  
  Post the capstone. Then run terraform destroy everywhere and confirm a zero-resource account.
