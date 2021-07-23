#!/bin/bash

cd $1
tmp=1
for file in *
do
	 mv "$file" $tmp-"$file"
done
ls 
cd ~ 
