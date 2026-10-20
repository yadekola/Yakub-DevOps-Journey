#!/bin/bash
# Update the package list
sudo apt-get update
sudo apt-get install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo chmod 777 /var/www/html/index.html