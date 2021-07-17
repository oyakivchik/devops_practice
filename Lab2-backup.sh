#!/bin/bash

if [ -e $1 ]
then
echo "backup is creating..."
name_backup=$1'-'$(date +%s)
mkdir -p a
tar -czf /a/$name_backup.tar.gz $1
echo "backup is created!"
exit 1
else
echo "file not found"
exit 1
fi


