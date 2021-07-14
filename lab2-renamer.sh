#!/bin/bash

cd $1
count=1

for file in *
do
	mv "$file" $count-"$file"
done
ls
cd ~
