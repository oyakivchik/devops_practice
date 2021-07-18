#!/bin/bash

read path
cd $path
num=0
for file in *
do 
num=$((num+1))
mv "$file" $num-"$file"
done