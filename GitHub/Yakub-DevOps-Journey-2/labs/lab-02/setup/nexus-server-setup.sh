#!/bin/bash

set -e

# ==========================================================
# Nexus Repository Manager Installation
# Amazon Linux 2023
# ==========================================================

NEXUS_VERSION="3.78.0-14"
NEXUS_URL="https://download.sonatype.com/nexus/3/nexus-unix-x86-64-${NEXUS_VERSION}.tar.gz"

NEXUS_USER="nexus"
NEXUS_BASE="/opt/nexus"
NEXUS_TMP="/tmp/nexus"

echo "=========================================="
echo " Installing Nexus Repository Manager"
echo " Version: ${NEXUS_VERSION}"
echo "=========================================="

# ----------------------------------------------------------
# 1. Configure Amazon Corretto repository
# ----------------------------------------------------------

echo "[1/9] Configuring Java repository..."

rpm --import https://yum.corretto.aws/corretto.key

curl -L \
    -o /etc/yum.repos.d/corretto.repo \
    https://yum.corretto.aws/corretto.repo

# ----------------------------------------------------------
# 2. Install required packages
# ----------------------------------------------------------

echo "[2/9] Installing required packages..."

yum install -y \
    java-17-amazon-corretto-devel \
    wget \
    tar

echo ""
echo "Java version:"
java -version

# ----------------------------------------------------------
# 3. Create Nexus user
# ----------------------------------------------------------

echo ""
echo "[3/9] Creating Nexus user..."

if id "$NEXUS_USER" >/dev/null 2>&1; then
    echo "User '$NEXUS_USER' already exists."
else
    useradd --system --no-create-home "$NEXUS_USER"
    echo "User '$NEXUS_USER' created."
fi

# ----------------------------------------------------------
# 4. Create directories
# ----------------------------------------------------------

echo "[4/9] Creating directories..."

mkdir -p "$NEXUS_BASE"
mkdir -p "$NEXUS_TMP"

# ----------------------------------------------------------
# 5. Download Nexus
# ----------------------------------------------------------

echo "[5/9] Downloading Nexus..."

cd "$NEXUS_TMP"

rm -f nexus.tar.gz

wget \
    "$NEXUS_URL" \
    -O nexus.tar.gz

# Make sure download exists
if [ ! -s nexus.tar.gz ]; then
    echo "ERROR: Nexus download failed."
    exit 1
fi

# ----------------------------------------------------------
# 6. Extract Nexus
# ----------------------------------------------------------

echo "[6/9] Extracting Nexus..."

rm -rf "$NEXUS_TMP"/nexus-*

tar -xzf nexus.tar.gz

NEXUS_DIR=$(find "$NEXUS_TMP" \
    -maxdepth 1 \
    -type d \
    -name "nexus-*" \
    -print -quit)

if [ -z "$NEXUS_DIR" ]; then
    echo "ERROR: Nexus directory was not found after extraction."
    exit 1
fi

NEXUS_NAME=$(basename "$NEXUS_DIR")

echo "Nexus directory detected:"
echo "$NEXUS_NAME"

# ----------------------------------------------------------
# 7. Install and configure Nexus
# ----------------------------------------------------------

echo "[7/9] Installing Nexus..."

rm -rf "$NEXUS_BASE/$NEXUS_NAME"

cp -a "$NEXUS_DIR" "$NEXUS_BASE/"

echo 'run_as_user="nexus"' \
    > "$NEXUS_BASE/$NEXUS_NAME/bin/nexus.rc"

chown -R "$NEXUS_USER:$NEXUS_USER" "$NEXUS_BASE"

# ----------------------------------------------------------
# 8. Create systemd service
# ----------------------------------------------------------

echo "[8/9] Creating Nexus systemd service..."

cat > /etc/systemd/system/nexus.service <<EOF
[Unit]
Description=Nexus Repository Manager
After=network.target

[Service]
Type=forking
User=nexus
Group=nexus

LimitNOFILE=65536
LimitNPROC=65536

ExecStart=$NEXUS_BASE/$NEXUS_NAME/bin/nexus start
ExecStop=$NEXUS_BASE/$NEXUS_NAME/bin/nexus stop

Restart=on-abort

TimeoutStartSec=600
TimeoutStopSec=600

[Install]
WantedBy=multi-user.target
EOF

# ----------------------------------------------------------
# 9. Enable and start Nexus
# ----------------------------------------------------------

echo "[9/9] Configuring systemd..."

systemd-analyze verify /etc/systemd/system/nexus.service

systemctl daemon-reload

systemctl enable nexus.service

systemctl start nexus.service

echo ""
echo "=========================================="
echo " Nexus installation completed"
echo "=========================================="

echo ""
echo "Service status:"
systemctl status nexus.service --no-pager -l

echo ""
echo "Nexus directory:"
echo "$NEXUS_BASE/$NEXUS_NAME"

echo ""
echo "Nexus port:"
ss -lntp | grep 8081 || true

echo ""
echo "=========================================="
echo " Access Nexus at:"
echo " http://YOUR_PUBLIC_IP:8081"
echo "=========================================="




systemctl stop nexus

mkdir -p /opt/nexus/sonatype-work/nexus3

chown -R nexus:nexus /opt/nexus

chmod -R 755 /opt/nexus

systemctl daemon-reload

systemctl start nexus

systemctl status nexus --no-pager -l




#!/bin/bash
echo "===== MEMORY ====="
free -h

echo "===== NEXUS LOG DIRECTORY ====="
ls -lah /opt/nexus/sonatype-work/nexus3/log/

echo "===== NEXUS LOG ====="
tail -n 100 /opt/nexus/sonatype-work/nexus3/log/nexus.log 2>/dev/null || true

echo "===== JVM LOG ====="
tail -n 100 /opt/nexus/sonatype-work/nexus3/log/jvm.log 2>/dev/null || true

echo "===== NEXUS PROCESS ====="
pgrep -a -f 'nexus-3.78.0|sonatype-nexus' || true

echo "===== PORT 8081 ====="
ss -lntp | grep 8081 || true

echo "===== OOM CHECK ====="
journalctl -k --no-pager | grep -i -E 'oom|out of memory|killed process' | tail -30 || true



ls -ld /opt/nexus/sonatype-work
ls -ld /opt/nexus/sonatype-work/nexus3
ls -ld /opt/nexus/sonatype-work/nexus3/log

stat -c '%U:%G %a %n' \
/opt/nexus/sonatype-work \
/opt/nexus/sonatype-work/nexus3 \
/opt/nexus/sonatype-work/nexus3/log
