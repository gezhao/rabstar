#!/bin/sh

## Author: George Zhao
## GetLog
#!/bin/sh

# e.g "sh check-chatbot.sh kill" it shall kill the process


hosts=("107.182.235.108")
target=/home/root/public_html



for ix in ${!hosts[*]}
do
	echo "testing...${hosts[$ix]}"
	if [ "$1" = "kill" ] 
	then
    	echo "kill processes"
    	ssh root@${hosts[$ix]} "pkill -f \"flask\""
	fi

done

echo "check is done!"


