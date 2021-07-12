#!/usr/bin/bash

#If argument is not a direcotry or is empty then leave
if ! [ -d $1 ] || [ -z $1 ]; then
   echo "Please enter directory correctly as an argument"
   exit 1
fi

curr=$(pwd)   #Save current directory
cd $1   #Go to specified directory
counter=0   #Counter for iterations

#Rename all files
for file in *; do
   ((counter++))  
   mv "$file" "$counter-$file"
done

echo "Successfully renamed $counter files"
ls   #Show renamed files
cd $curr   #Go to previous directory
