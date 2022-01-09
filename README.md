# help_to_animal
## Run this commands to start project
### create env
> python3 -m venv env

> source env/bin/activate
### install docker 
> sudo apt update && sudo apt upgrade

> sudo apt install linux-image-extra-$(uname -r) linux-image-extra-virtual

> sudo apt install apt-transport-https ca-certificates curl software-properties-common

> curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

> sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

> sudo apt update && apt-cache policy docker-ce

> sudo apt install -y docker-ce

### create user
> sudo usermod -aG docker $(name)
### install docker-compose
> sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

> sudo chmod +x /usr/local/bin/docker-compose

