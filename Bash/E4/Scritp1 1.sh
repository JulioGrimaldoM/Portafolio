#!/bin/bash
host=10.0.2.15
firstport=10
lastport=500
function portscan {
        for((counter=$firstport;counter<=$lastport;counter++))
        do 
		(echo > /dev/tcp/$host/$counter)> /dev/null 2>&1 && echo "$counter open" 
        done
}
function SO {
	if type -t wevtutil &> /dev/null
	then 
        	OS=MSWin
	elif type -t scutil &> /dev/null
	then 
        	OS=MacOS
	else 
        	OS=Linux
	fi 
	echo $OS
}
function ping_alive {
        ping -c 1 $1 > /dev/null 2>&1 
        [ $? -eq 0 ] && echo "Node with IP: $i is up." >> Reporte.txt 
}
portscan >> Reporte.txt
for i in 10.0.2.{1..255}
do
	ping_alive $i & disown 
done 
SO>>Reporte.txt

