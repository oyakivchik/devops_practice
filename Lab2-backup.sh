#!/bin/bash

sudo mkdir backup
sudo tar -cvzf ~/backup/-`date +%s`.tar.gz $1 --exclude=proc --exclude=sys --exclude=dev/pts .
echo "end of backup"
