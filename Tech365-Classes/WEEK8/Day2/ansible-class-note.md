# Ansible Class Notes

## 1. What is infrastructure automation?

Infrastructure automation means using tools and instructions to manage computers and servers automatically. Instead of signing in to every server and repeating the same steps by hand, we write the steps once and let a tool run them for us.

**Ansible** is an automation tool. It can connect to many servers over SSH and perform tasks such as installing software, starting services, copying files, and creating folders. Ansible usually does not need an agent installed on each managed server.

## 2. The servers used in class

We launched Ubuntu EC2 virtual machines in AWS. One machine was used to run Ansible, and the other machines were managed by Ansible. The managed servers were listed by their private IP addresses in the `inventory` file.

Ansible connects to Linux servers over SSH. It needs a username and an SSH private key that is allowed to connect to those servers. Keep the private key secret and set restrictive permissions on it. On Linux, a common command is:

```bash
chmod 400 server-tech365.pem
```

## 3. Installing Ansible on Ubuntu

These are the installation commands from class:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install ansible -y
```

To check that Ansible is installed:

```bash
ansible --version
which ansible
dpkg -l | grep ansible
```

`apt update` refreshes the package list. `apt upgrade` installs available updates. `apt install` installs Ansible. The other commands show its version, location, or installed package entry.

## 4. Inventory: telling Ansible which servers to manage

An inventory is a list of the computers Ansible can manage. In our `inventory` file, the group is named `server` and contains three private IP addresses:

```ini
[server]
172.31.21.115
172.31.24.67
172.31.29.221
```

The name inside square brackets is a group name. We can target the whole group by using `server` in an Ansible command or playbook.

## 5. Ansible configuration

The `ansible.cfg` file contains default settings for this project:

```ini
[defaults]
inventory = inventory
remote_user = ubuntu
private_key_file = server-tech365.pem
host_key_checking = False
```

- `inventory` tells Ansible which inventory file to use.
- `remote_user` is the account Ansible uses to sign in to the servers.
- `private_key_file` points to the SSH key used for the connection.
- `host_key_checking` controls SSH host identity checks. Turning it off can make first-time connections easier, but it reduces protection against connecting to an unexpected server. For regular use, keep host key checking enabled and verify server identities.

Keep the config and key paths correct for where you run Ansible. Do not share or commit a private key.

## 6. Testing the connection and running commands

Ansible can run a one-off task with an ad hoc command. The `-m` option selects a module, which is a built-in kind of task.

```bash
ansible server -m ping
```

The `ping` module checks whether Ansible can connect and run a basic task. It is not the same as the network ping command.

```bash
ansible server -m command -a "uptime"
ansible server -m command -a "df -h"
```

These run Linux commands on the servers in the `server` group. `uptime` shows how long a server has been running and its load. `df -h` shows disk usage in readable units.

## 7. Playbooks

A playbook is a YAML file containing a repeatable set of tasks. We ran our playbook with:

```bash
ansible-playbook nginx.yaml
```

The `nginx.yaml` playbook is set up to:

1. Target the `server` inventory group.
2. Use `become: true` to run tasks with administrator privileges when needed.
3. Set a variable named `nginx_path` to `/var/www/html/`.
4. Install Nginx using the `apt` module.
5. Start Nginx and enable it to start automatically when the server boots.
6. Copy the local `index.html` file to the web server's document directory with file mode `0644`.
7. Install `curl`, `unzip`, `git`, and `wget`.
8. Create `logs`, `configs`, and `backups` directories under `/home/ubuntu`.

The `copy` task uses `src: index.html`, so that file needs to be available on the Ansible control machine in the location expected by the playbook. The supplied `index.html` contains:

```html
<h1>Welcome To Tech365</h1>
```

After the playbook runs successfully, Nginx can serve that page from the managed server. The `file` task's `loop` repeats the directory-creation task for each listed folder. YAML uses indentation to show which settings belong to each task, so spaces and alignment matter.

## 8. Copying files with `scp`

`scp` copies files over SSH. For example, this command copies the key to a remote Ubuntu account:

```bash
scp -i server-tech365.pem server-tech365.pem ubuntu@SERVER_PUBLIC_IP:/home/ubuntu/
```

Be careful when copying private keys: only place them where needed and keep their permissions restricted. A recursive `scp -r` can copy a directory and its contents. Check source and destination paths before running it so you copy the intended files.

## 9. Quick reminder

- **Inventory** says which servers Ansible can manage.
- **`ansible.cfg`** holds project defaults such as the inventory, login user, and key path.
- **Ad hoc commands** are useful for quick checks and one-time tasks.
- **Playbooks** store multiple tasks so they can be repeated consistently.
- **Modules** do common work, such as `apt` for packages, `service` for services, `copy` for files, and `file` for files and directories.
- **Variables** store values, such as the web directory path, so they can be reused.
- **Loops** repeat a task for several values.
