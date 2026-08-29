"""Hand-rolled Prometheus exposition.

Deliberately written by hand instead of using prometheus_client, so that Yacoub can see
what a /metrics endpoint actually is: plain text, one metric per line, scraped over HTTP.
Once he understands that, swapping in the real library is a five-minute change - and a
good extension exercise.
"""
from collections import defaultdict
from threading import Lock

_lock = Lock()
_counters: dict[tuple, int] = defaultdict(int)


def inc(name: str, **labels):
    with _lock:
        _counters[(name, tuple(sorted(labels.items())))] += 1


def _fmt(name: str, labels: tuple) -> str:
    if not labels:
        return name
    inner = ",".join(f'{k}="{v}"' for k, v in labels)
    return f"{name}{{{inner}}}"


def render(gauges: dict[str, float]) -> str:
    lines = [
        "# HELP stockpulse_http_requests_total Total HTTP requests handled.",
        "# TYPE stockpulse_http_requests_total counter",
    ]
    with _lock:
        snapshot = dict(_counters)
    for (name, labels), value in sorted(snapshot.items(), key=lambda x: str(x[0])):
        lines.append(f"{_fmt(name, labels)} {value}")
    for name, value in gauges.items():
        lines.append(f"# TYPE {name} gauge")
        lines.append(f"{name} {value}")
    return "\n".join(lines) + "\n"
