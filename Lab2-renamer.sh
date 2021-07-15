#!/bin/bash
echo "Write path to directory that u want to rename : "
read path

echo "Your path : $path"
num=0
cd $path

for file in *
do 
   (( num ++ ))	

	if [ */$num-"$file" ];
	then
	echo "This file $file is already renamed"
	else
	mv "$file" $num-"$file"

fi
done 

ls 
cd ~