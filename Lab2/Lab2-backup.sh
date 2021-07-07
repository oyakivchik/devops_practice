#!/bin/bash

name_gz=$1'-'$(date +%s)

mkdir backup
tar -cvzf $name_gz.tar.gz $1
mv $name_gz.tar.gz backup/

exit 0
