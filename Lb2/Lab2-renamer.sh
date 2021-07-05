#!/bin/sh

if [ -d $1 ] #Перевіряємо чи введений шлях це директорія
then

  echo -e "\t You entered the directory: [$1]" #Виводдимо шлях директорії

  CWD=`pwd`  #Зберігаємо шля до директорії в якій ми знаходимося
  cd $1 переходисо ди вказаної директорії
  NWD=`pwd` #Шлях до вказаної директорії
  echo -e "\t Now you in: [$NWD]" #Повідомляємо користувача

  ITER=1 #Визанчаємо ітератор
  for FILE in * #Проходимося по всім файлам в директорії
  do
    if [ -f $FILE ] #Перевіряємо чи це фаїл
    then
      NEWFILENAME="$ITER-$FILE" #Створюємо нову назву файла
      mv $FILE $NEWFILENAME #Присвоюємо нову назву
      ITER=`expr $ITER + 1` #Збільшуємо ітрератор на "1"
      echo -e "\t\t File renamed: $FILE -> $NEWFILENAME" #Виводимо нову назву
    fi      
  done

  cd $CWD
  echo -e "\t Now you back in: [$CWD]" #Повідоляємо що ми знову в директорії в якій були

else
  echo -e "Enter the directory path!" #Повідомляємо шо шлях введено неправильно
fi
