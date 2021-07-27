#! /bin/bash
echo "INPUT DIRECTORY PATH: "
read path
echo "YOUR PATH: $path"
num=0
cd $path
for file in *
do 
   (( num ++ ))	
	if [ */$num-"$file" ];
	then
	echo "FILE $file RENAMED"
	else
	mv "$file" $num-"$file"
fi
done 
ls 