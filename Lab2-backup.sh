#!/bin/bash

#echo "Enter the path of file for backup"

#read path
tar -cvzf ~/Documents/backup/backup-`date +%s`.tar.gz $1

