#!/bin/bash

echo "Enter path:"
read path
cd $path
i=0
for file in *
do
  i=$((i+1))
  mv "$file" $i-"$file"
done
