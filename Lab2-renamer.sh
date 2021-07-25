#! /bin/bash
url=$1
home=$(pwd)
a=1
cd $url
for file in *;
do
mv "$file" "$a-$file"
let "a=a+1"
done
cd $home
exit 0 
