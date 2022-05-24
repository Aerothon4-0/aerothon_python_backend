#!/bin/bash
app="python_backend_main"
docker build -t ${app} .
docker run -d -p 5000:5000 --name=${app} --net host ${app}