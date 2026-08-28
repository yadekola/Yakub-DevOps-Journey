#!/usr/bin/env bash
# Quick health check across the multi-tier stack.
#
# WHAT: probes each tier in order and reports the first one that fails.
# WHY:  when the browser shows an error, you need to know WHICH layer broke.
# USAGE: ./health_check.sh <web-host> <app-host> <db-host>

set -euo pipefail   # exit on error, on undefined variable, and on a failed pipe stage

WEB=${1:?usage: $0 <web-host> <app-host> <db-host>}
APP=${2:?}
DB=${3:?}

check() {
  local label=$1 host=$2 port=$3
  if timeout 3 bash -c "cat < /dev/null > /dev/tcp/${host}/${port}" 2>/dev/null; then
    echo "  OK    ${label} (${host}:${port})"
  else
    echo "  FAIL  ${label} (${host}:${port})  <- start looking here"
    return 1
  fi
}

echo "Checking tiers bottom-up (the bottom is usually where it breaks):"
check "database " "$DB"  3306 || true
check "app tier " "$APP" 8080 || true
check "web tier " "$WEB" 80   || true

echo
echo "HTTP response from the web tier:"
curl -s -o /dev/null -w "  status=%{http_code}  time=%{time_total}s\n" "http://${WEB}/" || \
  echo "  no HTTP response at all - is nginx running?"
