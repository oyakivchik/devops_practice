#!/bin/bash

new_name=$1'-'$(date +%s)

sudo mkdir -p backup
sudo tar -czf backup/$new_name.tar.gz $1
