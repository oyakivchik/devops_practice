#!/bin/bash
echo "enter directory for renaming path"
read path

if ! [-d $path ] || [-z $path]; then
echo "data incorrect"
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
