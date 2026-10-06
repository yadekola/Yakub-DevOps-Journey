#!/bin/bash
sudo apt update
sudo apt install fontconfig openjdk-21-jdk -y
java -version

sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key

echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
https://pkg.jenkins.io/debian-stable binary/ | \
sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

echo "something" | sudo tee file


sudo apt update
sudo apt install jenkins -y
sudo systemctl status jenkins


