#!/bin/bash

i=1

echo "Введіть шлях до обраної папки"
read userinput

cd $userinput

for folderfile in *
do
             mv "$folderfile" $i-"$folderfile"
 
             i=$((i+1))
done

echo "Файли в папці були переіменовані!"
