What is jenkins?
Jenkins is an open sourece authomation server

What Continuous Integration CI?
WHAT HAPPENS DURING CI?
1. Update the code 
2. Push to Github 
3. Build and test

what is cd mean ----> Continuous Delivery VS Continuous Deployment

What problem is jenkins solves?

   Common Problem                      How Jeckins Helps
1. Repeated manual                     Automation pipeline
2. Problems discovered late            Earlier feedback
3. Inconsistent release steps          Version controlled instructions
4. Unclear failure details             Logs and build history

Why is jenkins is fits in the DevOps toolchain

Jenkins Architecture: Controller And Agents

Jobs, Build, Workspaces, and Exexutors
<!-- A successfull Job is a build -->

jenkins plugins and integrations
 
   Plugins VS external tools


Preparing the Jenkins installation Environment

ubuntu server on aws ec2
access and connectivity
SSH access port 22
jenkins 8080


Here are the command lines i run in my server i launch 
   1  clear
    2  free -h
    3  ldisk -h
    4  ldisk -l
    5  clear
    6  free -h
    7  nproc
    8  df -h
    9  free -h
   10  sudo apt update
   11  sudo apt upgrade -y
   12  swapon --show
   13  sudo fallocate -l 2G /swapfile
   14  sudo chmod 600 /swapfile
   15  sudo mkswap /swapfile
   16  sudo swapon /swapfile
   17  swapon --show
   18  lsblk
   19  clear
   20  sudo apt install fontconfig openjdk-21-jre -y
   21  java -version
   22  sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc   https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
   23  echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]"   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
   24  sudo apt update
   25  sudo apt install jenkins
   26  sudo systemctl enable jenkins
   27  sudo systemctl start jenkins
   28  sudo systemctl status jenkins
   29  clear
   30  history
   31  clear
   32  cat /var/lib/jenkins/secrets/initialAdminPassword
   33  clear
   34  cat /var/lib/jenkins/secrets/initialAdminPassword
   35  sudo cat /var/lib/jenkins/secrets/initialAdminPassword
   36  clear
   37  history

Jenkins is now working by visiting this http://100.59.200.129:8080/


 38  clear
   39  # Add Docker's official GPG key:
   40  sudo apt update
   41  sudo apt install ca-certificates curl
   42  sudo install -m 0755 -d /etc/apt/keyrings
   43  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
   44  sudo chmod a+r /etc/apt/keyrings/docker.asc
   45  # Add the repository to Apt sources:
   46  sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

   47  sudo apt update
   48  sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
   49  sudo apt install nodejs -y
   50  sudo apt install npm -y
   51  docker --version
   52  npm --version
   53  sudo systemctl enable --now docker
   54  sudo usermod docker jenkins
   55  sudo usermod -aG docker jenkins
   56  sudo usermod -aG docker ubuntu
   57  whoami
   58  sudo systemctl restart jenkins
   59  sudo -u jeckind docker version
   60  sudo -u jeckins docker version
   61  sudo -u jenkins docker version
   62  top
   63  ps -aux
   64  grep jenkins
   65  ls | grep jenkins docker
   66  ls | grep jenkins
   67  ls
   68  clear
   69  history



Credentials 
we create 