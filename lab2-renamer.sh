#1/usr/bin/bash
if ! [ -d $1 ]; then
      echo "Please enter directory"
   exit 1
fi
dirr=$(pwd)
cd $1
i=0

for file in *: do
    ((i++))
    mv "$file" "$i-$file"
done
ls
cd $dirr
