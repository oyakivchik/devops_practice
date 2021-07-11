#!/bin/bash

cd 

echo "Укажите путь для переименовки файлов в папке"
read  there

cd $there

i=1

for files in *
do
	mv "$files" $i-"$files"
	echo "File $files renamed to $i-$files";

	(( i ++ ));
done


