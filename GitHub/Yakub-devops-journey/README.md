# yaco-devops-journey

My 60-day DevOps engineering journey: **1 September - 31 October 2026**.

This repository is the evidence trail for two months of deliberate practice. Every week I
learn a block of the *Decoding DevOps* curriculum, then build something real with it,
break it on purpose, fix it, document it, and explain it out loud.

The success metric is not "I watched 378 videos". It is:

> I can build, deploy, automate, monitor, troubleshoot and **explain** what I built.

## The application

Everything in this repo revolves around one multi-tier application - the **vProfile**
stack used in the course:

```
Nginx (web)  ->  Tomcat / Java app  ->  MySQL
                          |-> Memcached
                          |-> RabbitMQ
```

It starts as five servers I configure by hand, and ends as a Helm-packaged workload on a
Terraform-provisioned EKS cluster, deployed by Argo CD and watched by Prometheus and
Grafana. Same app throughout - so every week the architecture gets more sophisticated
instead of starting over.

## Progression

```
Linux / AWS fundamentals
      |
Manual multi-tier deployment (Lift & Shift)
      |
Re-architecting on managed services (Beanstalk, RDS, ElastiCache, MQ)
      |
Maven -> Jenkins CI -> quality gates -> Nexus
      |
GitHub Actions / GitLab CI
      |
Python + Boto3 automation
      |
Terraform (Infrastructure as Code)
      |
Ansible (Configuration Management)
      |
Prometheus / Grafana / Loki (Observability)
      |
Custom VPC + AWS-native CI/CD + GCP
      |
Docker + full containerization
      |
Kubernetes + Helm
      |
CAPSTONE: GitOps pipeline to EKS with Argo CD
```

## Weekly roadmap

| Week | Dates | Focus | Lab | Milestone |
|---|---|---|---|---|
| 1 | Week 1 (Sep 1-6) | AWS compute, storage and the Lift & Shift deployment | Lab 1 | A multi-tier application running on AWS that you built and can explain, plus a clean AWS account afterwards. |
| 2 | Week 2 (Sep 7-13) | Re-architecting on PAAS/SAAS, Maven, and Jenkins CI | Lab 2 | A Jenkinsfile in your repo that builds, tests, analyses and publishes an artifact automatically. |
| 3 | Week 3 (Sep 14-20) | Jenkins CD, GitHub Actions, GitLab CI, Python foundations | Lab 3 | The same pipeline expressed three ways (Jenkins, GitHub Actions, GitLab) and a written comparison. |
| 4 | Week 4 (Sep 21-27) | Python automation with Boto3, and Terraform | Lab 4 | Infrastructure you can create and destroy with two commands, plus a Python tool that audits your own AWS account. |
| 5 | Week 5 (Sep 28-Oct 4) | Ansible configuration management and observability | Lab 5 | A server you never configured by hand, and a dashboard that tells you when it breaks. |
| 6 | Week 6 (Oct 5-11) | VPC networking, AWS-native CI/CD, and Google Cloud | Lab 6 | A production-shaped private network, and an application deployed into it by a pipeline you did not touch. |
| 7 | Week 7 (Oct 12-18) | Docker and full containerization | Lab 7 | The entire application stack running from a single `docker compose up`, with published images. |
| 8 | Week 8 (Oct 19-25) | Kubernetes and Helm - capstone phase 1 | Lab 8 | The application running on Kubernetes from a Helm chart, on a cluster created by Terraform. |
| 9 | Week 9 (Oct 26-31) | App on Kubernetes, GitOps, and the capstone | Lab Capstone | A complete GitOps capstone: commit to Git, and the change reaches a live Kubernetes cluster on its own. |

## Repository layout

```
yaco-devops-journey/
├── README.md
├── progress-tracker.md          Daily and weekly checkboxes
├── linkedin-report-template.md  Reusable post template + worked examples
├── docs/
│   ├── study-plan-summary.md    Condensed day-by-day plan
│   ├── curriculum-inventory.md  Every lecture number, title and duration
│   ├── troubleshooting-log.md   Running log of every failure and its fix
│   └── cloud-cost-safety.md     Free tier rules and cleanup discipline
├── architecture/                Diagrams (draw.io / PNG) for each week
├── week-01/ ... week-09/        Daily notes and exercises
├── labs/lab-01 ... lab-08/      One substantial integration lab per week
├── capstone/                    The final end-to-end project
├── terraform/                   Reusable Terraform modules and stacks
├── ansible/                     Roles, playbooks, inventories
├── docker/                      Dockerfiles and compose stacks
├── kubernetes/                  Manifests and Helm charts
├── jenkins/                     Jenkinsfiles and shared library snippets
├── github-actions/              Reusable workflow examples
├── monitoring/                  Prometheus config, Grafana dashboard JSON
└── scripts/                     Python and Bash automation
```

## How to use this repo

1. `git clone` it, or unzip and `git init`.
2. Work the day listed in `progress-tracker.md`.
3. Commit at the end of every study day - small commits, honest messages.
4. Post the LinkedIn report before you close the laptop.
5. On Sunday, write the README for that week's lab and record yourself explaining it.

## Secrets policy

**Nothing secret ever enters this repository.** No AWS keys, no database passwords, no
tokens, no kubeconfig files. See `docs/cloud-cost-safety.md` and the `.gitignore`.
Every lab uses environment variables, GitHub Secrets, Jenkins credentials, or Kubernetes
secrets created out-of-band.

If you ever commit a secret by accident: rotate the credential first, then clean history.
Rotating comes first because the moment it hits GitHub it is compromised.
