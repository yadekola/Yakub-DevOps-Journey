# Lab 2: Jenkins Continuous Integration pipeline with quality gates

**Week 2 — Saturday 12 September 2026**

## Objective

Build a complete CI pipeline as code for the vProfile app: checkout, Maven build, unit tests, Checkstyle, SonarQube analysis with a quality gate that can FAIL the build, artifact upload to Nexus, and a Slack notification on both success and failure.

## Why this lab exists

A build that only works on your machine is not a build. This lab is where 'it works locally' stops being an acceptable answer.

## Architecture

```
Git push -> Jenkins -> Maven build -> Unit tests -> Checkstyle -> SonarQube (quality gate)
                                                                  -> Nexus (artifact) -> Slack
```

Draw your own version of this diagram before you start building. Save it to
`../../architecture/lab-02.png`. If you cannot draw it, you do not understand it yet.

## Prerequisites

- Lab 1 concepts understood
- Jenkins, Nexus and SonarQube instances running (lectures 155, 165)
- Lectures 151-173 completed

## Acceptance criteria

- [ ] Jenkinsfile committed to the repo, not a freestyle job
- [ ] SonarQube quality gate wired through the webhook
- [ ] Nexus versioned artifact upload
- [ ] Credentials stored in Jenkins credentials store, never in the Jenkinsfile

## Steps

1. **Install Jenkins on an Ubuntu EC2** and complete the setup wizard.
   *Why an EC2 and not your laptop:* agents, webhooks and shared URLs all need a reachable host.

2. **Add tools under Manage Jenkins > Tools:** JDK 11 and Maven. Name them exactly — you
   reference these names in the Jenkinsfile.

3. **Store credentials in the Jenkins credentials store**, never in the pipeline:
   Nexus login, SonarQube token, Slack webhook.

4. **Write the Jenkinsfile** — see `Jenkinsfile` in this folder as a starting point.

5. **Configure the SonarQube webhook** back to Jenkins so the quality gate can report.
   *Why:* without the webhook `waitForQualityGate` blocks until timeout.

6. **Break the quality gate on purpose:** lower the threshold until the build fails, and
   confirm Slack tells you.

## Verification

- [ ] A push to the repo triggers the pipeline without you clicking Build
- [ ] The stage view shows all stages, with timings
- [ ] A versioned artifact appears in Nexus
- [ ] Slack receives both a success and a failure message
- [ ] `grep -ri password Jenkinsfile` returns nothing

## Troubleshooting challenges

Work these out yourself before looking anything up. Hints only — no answers.

1. **The pipeline hangs forever at the Quality Gate stage.**
   *Hint: Read the actual error, not the summary. Then ask: what changed?*
2. **Maven works on your laptop but the Jenkins agent cannot find JDK 11.**
   *Hint: Check the layer below the one you think is broken.*
3. **The Nexus upload returns 400 Bad Request.**
   *Hint: Compare a working case with the broken one and list every difference.*

## Cleanup

Jenkins, Nexus and SonarQube are all `t3.small`-ish. **Stop** them at the end of each
session rather than terminating — you will use them again in Week 3.

```bash
aws ec2 stop-instances --instance-ids i-xxxx i-yyyy i-zzzz
```
**Remember:** stopped instances still bill for EBS. If you will not touch them for more
than a week, terminate and rebuild from your notes — rebuilding is good practice anyway.

## Interview questions

Answer these in writing in `answers.md` before you consider the lab finished.

1. What is the difference between continuous integration, continuous delivery and continuous deployment?
2. Why is a Jenkinsfile better than a freestyle job?
3. Where are your credentials stored and why not in the repo?
4. What does a quality gate actually do, and should it block a build?
5. Your pipeline passes but the artifact is broken. What stage was missing?
6. How would you make this pipeline run on ten projects without copying the Jenkinsfile ten times?
