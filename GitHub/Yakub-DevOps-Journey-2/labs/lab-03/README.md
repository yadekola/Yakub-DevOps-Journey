# Lab 3: GitHub Actions CI/CD with security scanning and secrets

**Week 3 — Saturday 19 September 2026**

## Objective

Port the Jenkins pipeline to GitHub Actions, then reproduce the core of it a third time in GitLab CI. Build the app, scan it, build and publish a Docker image, and gate deployment behind a branch rule. Write a short comparison of the three tools.

## Why this lab exists

Nobody uses one CI tool forever. Being able to say 'I have built the same pipeline in Jenkins, GitHub Actions and GitLab, and here is when I would choose each' is a genuinely differentiating answer.

## Architecture

```
git push -> GitHub Actions [build | test | scan | docker build | publish]
           -> GitLab CI  [same stages, different syntax]
```

Draw your own version of this diagram before you start building. Save it to
`../../architecture/lab-03.png`. If you cannot draw it, you do not understand it yet.

## Prerequisites

- Lab 2 pipeline working
- Docker Hub account
- Lectures 174-199 completed

## Acceptance criteria

- [ ] Matrix or multi-job workflow with dependencies between jobs
- [ ] GitHub Secrets for registry credentials - nothing in plaintext
- [ ] A security scan job that can fail the workflow
- [ ] A written Jenkins vs Actions vs GitLab comparison in the lab README

## Steps

1. **Port the Jenkins stages to `.github/workflows/ci.yml`.** Keep the same stage names
   so the comparison is fair.
2. **Add GitHub Secrets** for the registry credentials: repo Settings > Secrets and variables > Actions.
   *Why:* a token in a workflow file is public the moment the repo is.
3. **Add a security scan job** that runs in parallel with the build and can fail the workflow.
4. **Add a build-and-publish job** that only runs on `main`, using `if: github.ref == 'refs/heads/main'`.
5. **Rebuild the core of it in GitLab CI** as `.gitlab-ci.yml` with masked variables.
6. **Write the comparison** in `comparison.md`: setup effort, syntax, secret handling,
   runner model, cost, and when you would pick each.

## Verification

- [ ] Workflow runs on push AND on pull request
- [ ] The deploy job is skipped on a feature branch
- [ ] An image with your username appears on Docker Hub
- [ ] Introducing a vulnerable dependency fails the scan job
- [ ] `comparison.md` has an opinion in it, not just a feature table

## Troubleshooting challenges

Work these out yourself before looking anything up. Hints only — no answers.

1. **The workflow passes locally with `act` but fails in GitHub with a permissions error.**
   *Hint: Read the actual error, not the summary. Then ask: what changed?*
2. **The Docker push fails with 'denied: requested access to the resource is denied'.**
   *Hint: Check the layer below the one you think is broken.*
3. **The deploy job runs on a feature branch even though you added an `if` condition.**
   *Hint: Compare a working case with the broken one and list every difference.*

## Cleanup

No cloud resources. Delete test images from Docker Hub if you pushed junk. Disable scheduled workflows so they do not burn your Actions minutes for two months.

## Interview questions

Answer these in writing in `answers.md` before you consider the lab finished.

1. When would you choose GitHub Actions over Jenkins, and when the reverse?
2. What is the difference between a GitHub Actions secret and an environment variable?
3. How do you stop a workflow running on every branch?
4. What is a runner? What is the difference between hosted and self-hosted?
5. Your workflow needs a secret in a pull request from a fork. What is the risk?
6. How would you share one workflow across five repositories?
