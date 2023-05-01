#!/bin/bash

state_create=$1
image_or_path_archive_name=$2
name_cont=$3
name_img=$4



if [[ "$state_create" == "archive" ]]
then
  if [[ -f "$image_or_path_archive_name" && ( $image_or_path_archive_name == *.tar.xz || $image_or_path_archive_name == *.raw ) ]]
  then
    cp "$image_or_path_archive_name" "./images-archive/"
    
    if [[ $image_or_path_archive_name == *.tar.xz ]]
    then
      cp "$image_or_path_archive_name" "/var/lib/machines/"
      machinectl import-tar "/var/lib/machines/$name_img.tar.xz" "$name_img"
      sudo systemd-nspawn --directory="/var/lib/machines/$name_img" -M "$name_cont" -b "&"
      
    fi

    if [[ $archive_path == *.raw ]]
    then
      cp "$image_or_path_archive_name" "/var/lib/machines/$name_img.raw"
      machinectl import-raw "var/lib/machines/$name_img.raw" "$name_img"
      sudo systemd-nspawn --directory="/var/lib/machines/$name_img" -M "$name_cont" -b &
      
    fi    

  else
    echo "Ошибка! Укажите верный архив с файловой системой"
    exit 1   
  fi   
elif [[ "$state_create" == "image" ]]
then
  sudo systemd-nspawn --directory="/var/lib/machines/$image_or_path_archive_name" -M "$name_cont" -b "&"
    
else
  echo "Ошибка режима создания контейнера"
  exit 1 
fi

# if [[ (-n "$memory_max") && (-n "$cpu_shares") && (-n "$ip_addres_allow") ]]
# then
#   systemctl set-property systemd-nspawn@"$image_name".service MemoryMax="$memory_max"M
#   systemctl set-property systemd-nspawn@"$image_name".service CPUQuota="$cpu_shares"%
#   exit 0
#   #machinectl set-limit "$image_or_path_archive_namee" IPAddressAllow="$ip_addres_allow"
# elif [[ -n "$memory_max" && -n "$cpu_shares" ]]
# then
#   systemctl set-property systemd-nspawn@"$image_name".service MemoryMax="$memory_max"M
#   systemctl set-property systemd-nspawn@"$image_name".service CPUQuota="$cpu_shares"%
#   exit 0
# elif [[ -n "$memory_max" && -n "$ip_addres_allow" ]]
# then
#   machinectl set-limit "$image_name" MemoryMax="$memory_maxG"
#   exit 0
#   #machinectl set-limit "$image_name" IPAddressAllow="$ip_addres_allow"
# else
#   systemctl set-property systemd-nspawn@"$image_name".service MemoryMax="$memory_max"M
#   exit 0   
# fi
# exit 0