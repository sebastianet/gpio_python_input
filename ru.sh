#!/bin/bash 
myip="$(/sbin/ifconfig wlan0 | grep 'inet addr:192' | cut -d: -f2 | awk '{print $1}')"
sudo  node  wsm.js  $myip
exit 0
