#!/bin/bash
apt update
sudo apt install git -y
sudo apt install nginx -y
git clone https://github.com/waleolajumoke/car-rentals
sudo cp -r car-rentals/* /var/www/html/
systemctl status nginx
echo "Deployment Completed"

