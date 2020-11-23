#!/bin/bash

# set the path

export PROJECT_PATH=`pwd`

sudo openresty -s stop
sudo openresty -c  $PROJECT_PATH/http/openresty.conf 
