#! /bin/bash
echo "input path: "
read path
echo "your path: $path"
num=0
cd $path
for file in *
do 
   (( num ++ ))	
	if [ */$num-"$file" ];
	then
	echo "$file renamed"
	else
	mv "$file" $num-"$file"
fi
done 