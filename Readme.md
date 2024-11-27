# Workshop FastAPI

## Docker Automatic Install

```sh
cp .env.example .env
docker compose up --build
```

## Install Docker

[Here is the link to install Docker](https://docs.docker.com/engine/install/)

Here is the command to install Docker on Ubuntu

```sh
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```sh
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify that Docker is installed correctly by running the hello-world image.

```sh
sudo docker run hello-world
```

For people that use another distribution, please refer to the [official documentation](https://docs.docker.com/engine/install/)