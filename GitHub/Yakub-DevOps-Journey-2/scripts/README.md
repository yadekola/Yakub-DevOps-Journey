# Scripts

| Script | Purpose | Used in |
|---|---|---|
| `aws_audit.py` | Lists running resources, flags untagged ones, estimates monthly cost | Lab 4 onwards - run before every logoff |
| `health_check.sh` | Probes each tier in order to find which layer is broken | Lab 1 onwards |

## Habit worth building

```bash
python3 scripts/aws_audit.py --all-regions
```

Run it at the end of every session. The day it prints "Nothing running. Account is clean."
after you thought you had already cleaned up is the day it pays for itself.
