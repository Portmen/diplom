cont_name=$1
memory_max=$2
cpu_shares=$3
ip_addres_allow=$4





if [[ (-n "$memory_max") && (-n "$cpu_shares") && (-n "$ip_addres_allow") ]]
then
  systemctl set-property machine-"$cont_name".scope MemoryLimit="$memory_max"M
  systemctl set-property machine-"$cont_name".scope CPUQuota="$cpu_shares"%
  exit 0
  #machinectl set-limit "$image_or_path_archive_namee" IPAddressAllow="$ip_addres_allow"
elif [[ -n "$memory_max" && -n "$cpu_shares" ]]
then
  systemctl set-property machine-"$cont_name".scope MemoryLimit="$memory_max"M
  systemctl set-property machine-"$cont_name".scope CPUQuota="$cpu_shares"%
  exit 0
elif [[ -n "$memory_max" && -n "$ip_addres_allow" ]]
then
  systemctl set-property machine-"$cont_name".scope MemoryLimit="$memory_max"M
  exit 0
  #machinectl set-limit "$image_name" IPAddressAllow="$ip_addres_allow"
else
  systemctl set-property machine-"$cont_name".scope MemoryLimit="$memory_max"M
  exit 0   
fi
exit 0