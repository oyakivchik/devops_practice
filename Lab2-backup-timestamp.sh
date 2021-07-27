#!/bin/bash

echo "S T A R T I N G"
echo ". . ."
sudo mkdir -p backup
sudo tar -czf backup/$1'-'$(date +%s).tar.gz $1
echo "D O N E"
echo ". . ."
 
