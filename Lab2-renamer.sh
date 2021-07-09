#!/bin/bash
echo "Input directory path to rename : "
read path
echo "Inputed path : $path"
num=0
cd $path
for file in *
do 
   (( num ++ ))	
	if [ */$num-"$file" ];
	then
	echo "File $file already renamed"
	else
	mv "$file" $num-"$file"
fi
done 
ls 
cd ~
