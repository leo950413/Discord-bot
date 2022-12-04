import docker
import os
from lib.db import *
import subprocess
import random

client = docker.from_env()

def create(id:str,challenge:int):

    if(not(instance_validate(id))):return "Delete other instance before you start a new one"
    if(not(can_create(challenge))): return "Not a valid challenge id"
    
    used_port = find_used_port()
    k = random.randint(8000,10000)
        
    while(k in used_port):

        k = random.randint(8000,10000)

        if(len(used_port)>2000):
                
            return "Too many active machine"
    
    os.chdir(f"/home/bitnami/ctf/web/c{str(challenge)}/")
    subprocess.Popen(f"export PORT={str(k)} && docker-compose -p {id}-{str(challenge)} up -d",shell=True).wait()
    container_id = str(client.containers.list()[0].id)
    save_instance_record(id,container_id,k)
    return f"Create successfully , your instance has been active at http://cmsctf.com:{str(k)}"


def delete(id:str):
    container_id = id_to_container(id)[0]
    subprocess.Popen(f"docker stop {container_id}",shell=True).wait()
    subprocess.Popen(f"docker rm {container_id}",shell=True).wait()
    remove_container(id)

    return "Delete successfully"