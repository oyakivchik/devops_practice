#!/bin/bash

sudo mkdir -p backup
sudo tar -czf  backup/$1'-'$(date +%s).tar.gz $1
echo "Backup of this file was created"
