#!/bin/bash
n=1
for f in *
do
if [ "$f" = "rename.sh" ]
then 
continue
fi
mv "$f" "$((n++))_$f"
done
