#!/bin/bash
app="user_react_blog"
docker build -t ${app} .
docker run -d -p 3000:3000 --name=${app} ${app}