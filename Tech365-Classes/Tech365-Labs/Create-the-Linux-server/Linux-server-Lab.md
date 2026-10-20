Task 1: Create the Linux server

Install Ubuntu Server using VirtualBox, VMware, Vagrant, AWS EC2, or another cloud platform.

Requirements:
- Create a non-root administrator
- Set the hostname to devops-app-server
- Update all installed packages
- Install curl, wget, git, vim, unzip, tree, and htop

Submission:

Screenshot showing the hostname
Screenshot showing the operating system version
List of installed packages
Brief explanation of how the server was created

Task 2: Create users and groups

The company has developers, testers, and DevOps engineers.

Create the following groups:
developers
testers
devops

Create these users and put them in the specified groups:
Username/groups
david - developers
sarah - developers
grace - testers
wale - devops

Requirements:
Every user must have a home directory
Add wale to the sudo group
Create /opt/company-app

Developers should have read and write access

Testers should only have read access

Other users should have no access

Users must not share passwords

Task 3: Manage files and permissions

Create the following project structure:

/opt/company-app/
├── app/
├── backups/
├── config/
├── logs/
├── scripts/
└── uploads/

Requirements:
Developers can modify files inside app

Only DevOps engineers can modify config

The application can write to logs and uploads

Other users cannot access config

New files created in app must inherit the developers group

Task 4: Manage processes and services

Install Nginx and manage it as a Linux service.

Requirements:
- Install Nginx
- Start the service
- Enable it to start automatically after reboot
- Stop and restart the service
- Find the Nginx processes
- Identify the process IDs
- Check which port Nginx uses
- Review the service logs

Troubleshooting exercise:
- Stop Nginx.
- Try to access the server.
- Find the cause.
- Start Nginx.
- Confirm that the website works again.

Task 5: Write a server health-check script

Create:
/opt/company-app/scripts/health-check.sh

The script must check:
- Current date and time
- Server hostname
- Server uptime
- CPU load
- Memory usage
- Disk usage
- Running processes
- Nginx status
- Internet connectivity
- Application availability

The script should display a warning when:
- Disk usage is above 80 percent
- Memory usage is above 85 percent
- Nginx is not running
- The application is unavailable

Sample output:
SERVER HEALTH REPORT
Hostname: devops-app-server
Date: 26 September 2026
Uptime: 2 days

Disk Usage: 45% - OK
Memory Usage: 62% - OK
Nginx: Running
Application: Available
Internet: Connected