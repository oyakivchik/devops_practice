#!/bin/bash
echo "Enter path to directory for renaming: "
read path

if ! [ -d $path ] || [ -z $path ]; then
  echo "Please enter correct data"
  exit 1
fi

echo "Changing files in $path"
counter=0
cd $path

for file in *
do 
   ((counter++))
      mv "$file" "$counter-$file"
done
echo "Files renamed"
ls
cd ~
