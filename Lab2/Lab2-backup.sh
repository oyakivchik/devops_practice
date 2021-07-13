#!/bin/bash

if [ ! -d "/backup"]
then 
	cd /
	mkdir backup
fi

file=$1
dest=/backup/$(basename "$file")$(date +%s).tar.gz

tar -cpzf $dest $file

echo "Backup of $(basename "$file") was created in $dest"