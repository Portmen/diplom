archive_path=$1
image_name=$2
state_create=$3
disk_size=$4


if [[ "$state_create" == "archive" ]]
then
  if [[ -f "$archive_path" && ( $archive_path == *.tar.xz || $archive_path == *.raw ) ]]
  then
    cp "$archive_path" "../images-archive/"
    
    if [[ $archive_path == *.tar.xz ]]
    then
      cp "$archive_path" "/var/lib/machines/$image_name.tar.xz"
      machinectl import-tar "/var/lib/machines/$image_name.tar.xz" "$image_name"
      machinectl start $image_name
      exit 0
    fi

    if [[ $archive_path == *.raw ]]
    then
      cp "$archive_path" "/var/lib/machines/$image_name.raw"
      machinectl import-raw "var/lib/machines/$image_name.raw" "$image_name"
      machinectl start "$image_name"
      exit 0
    fi    

  else
    echo "Ошибка! Укажите верный архив с файловой системой"
    exit 1   
  fi   
else
  machinectl start "$image_name"
  exit 0
fi  

