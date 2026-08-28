# Monitoring

## PromQL you should be able to write without looking it up

```promql
up                                              # 1 = scraped OK, 0 = target down
rate(node_cpu_seconds_total{mode="idle"}[5m])   # per-second rate over 5 minutes
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)   # CPU used %
node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100                # memory free %
```

`rate()` needs a counter and a time range. Using it on a gauge gives nonsense.

## Trigger your alert on purpose

```bash
sudo apt install -y stress
stress --cpu 4 --timeout 300
```

If Slack does not receive anything within the `for:` window plus the scrape interval,
your alert is decorative. Fix it now, not in production.

## Export your dashboard

Grafana dashboards live in Grafana's database, not in Git. Before you destroy anything:
Dashboard > Share > Export > Save to file, and commit the JSON into `grafana/`.
