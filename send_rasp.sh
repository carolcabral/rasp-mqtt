#!/bin/bash

# -a address
if [ $# -lt 1 ]; then
	echo "Warning: IP Address as default (192.168.100.76)!"
	raspi_ip="192.168.100.76"
else
	raspi_ip=${1}
fi

# -u user
raspi_user="pi"
# -p password
raspi_passwd="2013046270"
# -f file
file="mqtt-client.py"
#file="send_pc.sh"
# -w working directory in raspi
path_to_file="/home/pi/mosquitto-bridge"

sshpass -p ${raspi_passwd} scp ${file} ${raspi_user}@${raspi_ip}:${path_to_file}

#sshpass -p ${password} ssh ${login_rasp}@${ip_rasp} 'cd /home/pi/src && gcc main.c -o ../prog/mesa -lwiringPi'