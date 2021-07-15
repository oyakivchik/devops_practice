#!/bin/bash
sudo mkdir -p /backup
arg=$1
sudo tar -czf /backup/$arg-$(date '+%s').tar.gz $1
echo "back created"
