#!/bin/bash
sudo mkrir -p /backup
arg=$1
echo "backup creating"
sudo tar -czf /backup/$arg-$(date '+%s').tar.gz $1
echo "backup created"