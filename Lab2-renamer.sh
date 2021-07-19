#!/bin/bash
echo "Введіть шлях до обраної папки "
read path
num=0
cd $path
for file in *
do 
   (( num ++ ))	
	if [ */$num-"$file" ];
	then
	echo "Файл $file вже перейменований"
	else
	mv "$file" $num-"$file"
fi
done 
ls 
cd ~