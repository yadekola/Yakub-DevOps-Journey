# Lab 5: Ansible configuration management + Prometheus/Grafana observability

**Week 5 — Saturday 03 October 2026**

## Objective

Provision infrastructure with Terraform, configure it entirely with Ansible roles, and monitor it with Prometheus, Grafana, node_exporter and Loki. Build a real dashboard and a real alert that fires to Slack.

## Why this lab exists

Terraform creates servers. Ansible makes them useful. Monitoring tells you when they stop being useful. This is the first lab that looks like an actual operations job.

## Architecture

```
Terraform -> EC2 nodes
Ansible roles -> configure app + node_exporter
Prometheus -> scrapes nodes -> Grafana dashboards -> Slack alerts
Loki -> log aggregation
```

Draw your own version of this diagram before you start building. Save it to
`../../architecture/lab-05.png`. If you cannot draw it, you do not understand it yet.

## Prerequisites

- Lab 4 Terraform working
- Ansible installed
- Lectures 234-262 completed

## Acceptance criteria

- [ ] Ansible roles with handlers and Jinja2 templates - no long flat playbooks
- [ ] Prometheus scraping at least two nodes
- [ ] A Grafana dashboard with CPU, memory, disk and app-availability panels
- [ ] An alert rule with a threshold you can trigger on demand

## Steps

1. **Provision two nodes with Terraform**, output their IPs into an Ansible inventory.
2. **Write an Nginx role** with `tasks/`, `handlers/`, `templates/`, `defaults/`.
   *Why a role and not a playbook:* roles are reusable and reviewable; a 300-line playbook is not.
3. **Run the playbook twice.** The second run must report `changed=0`.
   *If it does not,* you used `shell` or `command` where a proper module exists.
4. **Install Prometheus and node_exporter** via a second role.
5. **Install Grafana**, add Prometheus as a datasource, build a dashboard with CPU, memory,
   disk and up/down panels.
6. **Create an alert rule** — e.g. CPU > 80% for 2 minutes — routed to Slack. Trigger it on
   purpose with `stress` or a busy loop and confirm the message arrives.
7. **Add Loki** and ship Nginx access logs to it. Query them in Grafana.

## Verification

- [ ] Second Ansible run: `changed=0`
- [ ] Prometheus targets page shows both nodes UP
- [ ] Grafana dashboard shows live data
- [ ] Alert fires to Slack within the configured window
- [ ] Dashboard JSON is exported into `monitoring/` in this repo

## Troubleshooting challenges

Work these out yourself before looking anything up. Hints only — no answers.

1. **Ansible reports 'changed' on every run - your playbook is not idempotent.**
   *Hint: Read the actual error, not the summary. Then ask: what changed?*
2. **Prometheus shows the target as DOWN but you can curl :9100/metrics from the Prometheus host.**
   *Hint: Check the layer below the one you think is broken.*
3. **Grafana panels are empty even though the datasource test succeeds.**
   *Hint: Compare a working case with the broken one and list every difference.*

## Cleanup

`terraform destroy -auto-approve`, then confirm with the sweep in `docs/cloud-cost-safety.md`. Export the Grafana dashboard JSON BEFORE you destroy — it is not recoverable afterwards.

## Interview questions

Answer these in writing in `answers.md` before you consider the lab finished.

1. What is idempotency in Ansible, and how do you know if you have it?
2. Ansible vs Terraform — what does each own?
3. What is the difference between a fact variable and a group variable?
4. What does a Prometheus exporter actually do?
5. What is the difference between monitoring and observability?
6. Your alert fires at 3am but nothing was wrong. How do you fix that?
