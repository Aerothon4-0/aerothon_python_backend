#!/bin/bash
app="python_backend"
docker build -t ${app} .
docker run -d -p 5001:5001 --name=${app} --net host ${app}

 #sudo docker rm $(sudo docker stop $(sudo docker ps --filter name=user_backeend_python_docker -q) )