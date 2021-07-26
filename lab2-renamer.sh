#!/bin/bash

cd $1
count=1
for name in *
do
	 mv "$name" $count-"$name"
done
ls 
cd ~ 
