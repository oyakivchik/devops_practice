#!/bin/bash

echo "Enter directory:"
read path
cd $path
echo Current directory: $(pwd)

number=1
for file in * 
do  
    if ! [ -d $file ] 
    then
        mv "$file" $number-"$file"
        ((number++))
    fi
done

ls -l

