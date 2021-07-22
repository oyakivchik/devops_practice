
#!/bin/bash
echo "Input path : "
read path
cd $path
value=1
for file in *
do 
   mv "$file" $value-"$file"
   (( value ++ ))
done 
ls  
