# LinkedIn daily report template

One post per study day, published between 16:30 and 17:00. Consistency beats brilliance -
40 mediocre honest posts beat 3 polished ones.

## The template

```
Day X of my 60-day DevOps journey.

Today I learned:
<the concept, in one or two sentences, in your own words>

Today I built:
<what you actually made - be concrete>

The problem I hit:
<the real error message or symptom>

How I solved it:
<what you checked, what the cause turned out to be>

What I now understand that I didn't yesterday:
<the insight - this is the part people actually engage with>

#DevOps #AWS #Docker #Kubernetes #Terraform #100DaysOfDevOps
```

## Rules

- **Never** post "Today I watched videos 154-161." Nobody can hire you from that.
- Always attach evidence. A post without a screenshot is a claim; a post with one is proof.
- Write about the failure, not just the success. Engineers respect the debugging story.
- Keep it under 200 words. Long posts get scrolled past.
- Tag the tool you used. It is how the right people find you.

## Evidence to attach, by topic

| Topic | Attach |
|---|---|
| Linux / Bash | Terminal screenshot with the command and output visible |
| AWS | Console screenshot, or better, an architecture diagram you drew |
| Jenkins | Pipeline stage view (green), and one showing a failed quality gate |
| GitHub Actions | Workflow run summary page |
| Terraform | `terraform plan` output, and the resulting console resources |
| Ansible | Playbook recap showing `ok=` and `changed=` counts |
| Docker | `docker images` output showing your image size, or `docker compose ps` |
| Kubernetes | `kubectl get pods -o wide`, or the app running through the Ingress |
| Prometheus/Grafana | The dashboard itself, with a real alert firing |
| Any week | The GitHub commit or PR |

---

## Worked examples

### Example 1 - Week 1, AWS load balancing

> Day 2 of my 60-day DevOps journey.
>
> Today I learned how an Application Load Balancer decides whether a server is allowed to
> receive traffic. It is not "is the server running" - it is "does this specific health
> check path return 200".
>
> Today I built: two EC2 instances behind an ALB, serving the same app.
>
> The problem I hit: both targets sat at "unhealthy" even though I could curl the app
> successfully from inside each instance.
>
> How I solved it: I checked the security group first (wrong guess - it was fine), then
> looked at the target group health check. It was pointing at `/` but my app only responds
> on `/login`. Changed the path, both targets went healthy in about 30 seconds.
>
> What I now understand: a healthy server and a healthy target are two different things.
>
> [screenshot: target group showing 2/2 healthy]

### Example 2 - Week 2, Jenkins

> Day 9 of my 60-day DevOps journey.
>
> Today I learned the difference between a freestyle Jenkins job and Pipeline as Code.
> A freestyle job lives in Jenkins' database - if the server dies, the job dies. A
> Jenkinsfile lives in Git, gets reviewed like code, and can be rebuilt anywhere.
>
> Today I built: a Jenkinsfile that checks out the code, builds a .war with Maven, runs
> unit tests, and uploads the artifact to Nexus.
>
> The problem I hit: the build failed with "Unable to locate a Java Runtime" even though
> Java was installed on the server.
>
> How I solved it: Jenkins does not inherit your shell's PATH. I had to declare JDK 11
> under Manage Jenkins > Tools and reference it in the pipeline.
>
> What I now understand: Jenkins runs in its own environment. Anything a build needs has
> to be declared, not assumed.
>
> [screenshot: pipeline stage view, all green]

### Example 3 - Week 5, a day where things went badly

> Day 26 of my 60-day DevOps journey. Today was mostly failure, and that is fine.
>
> Today I built: an Ansible role to install and configure Nginx across two servers.
>
> The problem I hit: my playbook reported "changed" on every single run. It worked, but it
> was not idempotent - which means in production it would restart services for no reason.
>
> How I solved it: I was using the `shell` module to copy a config file. `shell` cannot
> know whether anything actually changed, so it always reports changed. Switching to the
> `template` module fixed it - second run reported ok=5 changed=0.
>
> What I now understand: idempotency is not automatic. It comes from using modules that
> can compare desired state to actual state. Reaching for `shell` is usually a sign I have
> not found the right module yet.
>
> [screenshot: PLAY RECAP showing changed=0 on the second run]

### Example 4 - Week 9, capstone

> Day 60. The final day of my 60-day DevOps journey.
>
> Today I built: the whole thing, from scratch, in one run. A commit to GitHub triggers a
> GitHub Actions pipeline that builds and scans the app, pushes an image to ECR, and
> updates a Helm chart. Argo CD notices the change and syncs it to an EKS cluster that
> Terraform created. Prometheus scrapes it and Grafana shows it.
>
> The problem I hit: Argo CD showed "OutOfSync" but refused to sync, with no useful error.
>
> How I solved it: the service account Argo CD was using did not have permission on the
> target namespace. `kubectl auth can-i` from the Argo service account made it obvious in
> about a minute - a tool I did not know existed six weeks ago.
>
> What I now understand: GitOps means Git is the source of truth. I never ran `kubectl
> apply` to deploy. I changed a file, and the cluster changed itself.
>
> [architecture diagram + Argo CD synced screenshot + Grafana dashboard]
