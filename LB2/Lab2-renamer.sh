#!/bin/sh

if [ -d $1 ] #Перевірка на директорію
then

  echo -e "\t You entered the directory: [$1]" #Шлях до неї

  CWD=`pwd`  #Шлях збережено
  cd $1 
  NWD=`pwd` #Шлях до директорії
  echo -e "\t Now you in: [$NWD]" #Вивід користувача

  ITER=1 
  for FILE in * #Обхід файлів дерикторії
  do
    if [ -f $FILE ] 
    then
      NEWFILENAME="$ITER-$FILE" 
      mv $FILE $NEWFILENAME #Нова назва файлу
      ITER=`expr $ITER + 1` #Збільшуємо ітрератор на "1"
      echo -e "\t\t File renamed: $FILE -> $NEWFILENAME" #Вивід нової назви
    fi      
  done

  cd $CWD
  echo -e "\t Now you back in: [$CWD]" 

else
  echo -e "Enter the directory path!" #Неправильно введений шлях
fi
