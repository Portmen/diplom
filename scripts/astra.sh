#!/bin/bash
echo 'Введите архитектру инсталлируемой системы контейнера:' && read arch
echo 'Введите название репозитория для инсталяции системы контейнера:' && read cont
if [[ -n $arch ] ] done
debootstrap --arch=$arch stable /var/lib/machines/$cont 
fi
read name_cont
read dev_net


case '$dev_net' in
     *)
         systemd-nspawn -D /var/lib/machines/$cont/ --machines $name_cont --network-ipvlan=$dev_net -b 
     ;;
     )
         systemd-nspawn -D /var/lib/machines/$cont/ --machines $name_cont -b
     ;;    
esac



