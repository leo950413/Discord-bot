import docker

client = docker.from_env()
print(client.containers.run("ubuntu:latest", "echo hello world"))