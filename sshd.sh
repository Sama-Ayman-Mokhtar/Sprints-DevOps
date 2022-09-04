#!/usr/bin/env bash

# To run:
# sudo ./sshd.sh

echo "Please Enter an Integer To Set as SSH Port: (run as root)"
read INT_FROM_USER
if [[ ${INT_FROM_USER} -lt 1024  && ${INT_FROM_USER} != 22 || ${INT_FROM_USER} -gt 65535 ]]
then 
	echo "[Error] Invalid port number - choose a number between 1024 and 65535 or 22"
else
	sed -i -e "/Port /c\Port ${INT_FROM_USER}" /etc/ssh/sshd_config
	echo "[+] Changed ssh port number"
fi

sed -i -e "/PermitRootLogin /c\PermitRootLogin no" /etc/ssh/sshd_config
echo "[+] Disabled root login to system"
service sshd restart
echo "[+] Restarted ssh service"

