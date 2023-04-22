archive_path=$1
image_name=$2
state_create=$3
disk_size=$4
memory_max=$5
cpu_shares=$6
ip_addres_allow=$7


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
      
    fi

    if [[ $archive_path == *.raw ]]
    then
      cp "$archive_path" "/var/lib/machines/$image_name.raw"
      machinectl import-raw "var/lib/machines/$image_name.raw" "$image_name"
      machinectl start "$image_name"
      
    fi    

  else
    echo "Ошибка! Укажите верный архив с файловой системой"
    exit 1   
  fi   
elif [[ "$state_create" == "image" ]]
then
  machinectl start "$image_name"
    
else
  echo "Ошибка режима создания контейнера"
  exit 1 

if [[ -n "$memory_max" && -n "$cpu_shares" && -n "$ip_addres_allow"]]
then
  machinectl set-limit "$image_name" MemoryMax="{$memory_max}G"
  machinectl set-limit "$image_name" CPUShares="$((cpu_shares * 1024))"
  exit 0
  machinectl set-limit "$image_name" IPAddressAllow="$ip_addres_allow"
elif [[ -n "$memory_max" && -n "$cpu_shares" ]]
then
  machinectl set-limit "$image_name" MemoryMax="{$memory_max}G"
  machinectl set-limit "$image_name" CPUShares="$((cpu_shares * 1024))"
  exit 0
elif [[ -n "$memory_max" && -n "$ip_addres_allow" ]]
then
  machinectl set-limit "$image_name" MemoryMax="{$memory_max}G"
  machinectl set-limit "$image_name" IPAddressAllow="$ip_addres_allow"
  exit 0
else
  machinectl set-limit "$image_name" MemoryMax="{$memory_max}G"
  exit 0   