#! /bin/bash
echo "input dir path: "
read path
echo "path: $path"
num=0
cd $path
for file in *
do 
   (( num ++ ))	
	if [ */$num-"$file" ];
	then
	echo "$file done"
	else
	mv "$file" $num-"$file"
fi
done 