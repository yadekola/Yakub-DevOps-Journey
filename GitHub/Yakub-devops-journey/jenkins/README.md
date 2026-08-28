# Jenkins

## Setup checklist

- [ ] Jenkins installed on an EC2 (t3.small is enough; **stop it when not in use**)
- [ ] Plugins: Pipeline, Git, Maven Integration, SonarQube Scanner, Nexus Artifact Uploader, Slack Notification
- [ ] Manage Jenkins > Tools: JDK named `JDK11`, Maven named `MAVEN3`
- [ ] Manage Jenkins > System: SonarQube server named `sonarserver`
- [ ] Credentials: `nexus-login`, SonarQube token, Slack token — all in the credentials store
- [ ] SonarQube webhook pointing back at `http://<jenkins>:8080/sonarqube-webhook/`

## The two failures everyone hits

**"Unable to locate a Java Runtime"** — Jenkins does not inherit your shell PATH. Declare
the JDK in Manage Jenkins > Tools and reference it in the `tools {}` block.

**Quality Gate hangs until timeout** — the SonarQube webhook is missing. `waitForQualityGate`
waits for SonarQube to call Jenkins back; without the webhook, nothing ever calls.

## Never in a Jenkinsfile

Passwords, tokens, private URLs with credentials embedded. Use `credentials()` and the
credentials store. Run `grep -riE "password|token|secret" Jenkinsfile` before every commit.
