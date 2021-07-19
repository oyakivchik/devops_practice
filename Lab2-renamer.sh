read -p "Enter path to directory:" path
num=0
cd $path
for var in *
do
  num=$((num+1))
  mv $var "$num-$var"
done
  
