# Troubleshooting log

The single most valuable file in this repository for interviews. Every time something
breaks, add a row. Interviewers ask "tell me about a time something broke" - this is
where your answer comes from.

| Date | What broke | Symptom / error message | What I checked | Root cause | Fix | Lesson |
|---|---|---|---|---|---|---|
| 2026-09-01 | *example* | ALB target shows `unhealthy` | curl to instance worked; checked SG, health check path | Health check path was `/` but app serves `/login` | Changed health check path in target group | An unhealthy target is usually a health-check config problem, not an app problem |

## How to write a good entry

Do not write "it didn't work, I fixed it." Write what you **observed**, what you
**hypothesised**, how you **tested** the hypothesis, and what was actually wrong.
The wrong hypotheses are worth recording too - they show diagnostic reasoning.
