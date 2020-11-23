#!/bin/bash
docker run -rm -d --hostname rabbit --name rabbit  -p 5672:5672    rabbitmq:3 
