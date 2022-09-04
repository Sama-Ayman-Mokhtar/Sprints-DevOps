#!/usr/bin/env bash

echo "Please Enter an Integer To Set as SSH Port: "
read INT_FROM_USER
if [[ ${INT_FROM_USER} -lt 1024  && ${INT_FROM_USER} != 22 || ${INT_FROM_USER} -gt 65535 ]]
then 
	echo "invalid port number - choose a number between 1024 and 65535 or 22"
else
	sed -i -e "/Port /c\Port ${INT_FROM_USER}" /etc/ssh/sshd_config
	echo "[+] Edited the config file"
	service ssh restart
	echo "[+] Restarted ssh service"
fi

