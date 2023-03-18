
if [[ $1 == *.xz && $1 == *.tar && $1 == *.raw ]]
then
   cp $1 ../images-archive/
else
   echo "Ошибка! Укажите верный архив с файловой системой"   
fi   