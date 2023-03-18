
if [[ $1 == *.tar && $1 == *.xz ]]
then
   muchinectl import-tar ../images-archive/$1 $2
fi

if [[ $1 == *.raw ]]
then
   muchinectl import-raw ../images-archive/$1 $2
