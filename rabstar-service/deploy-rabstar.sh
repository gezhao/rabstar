#!/bin/sh

## Author: George Zhao

#Copy the artifacts over and start the process

hosts=("107.182.235.108")


target=/home/root/public_html

for ix in ${!hosts[*]}
do
	echo "scp file to ${hosts[$ix]}"
    scp *.py root@${hosts[$ix]}:$target
    scp ./templates/*.* root@${hosts[$ix]}:$target/templates
    scp ./backend/*.* root@${hosts[$ix]}:$target/backend
    ##scp ./backend/CryptoList/*.* root@${hosts[$ix]}:$target/backend/CryptoList/    
    scp startRB.sh root@${hosts[$ix]}:$target
    echo "run command  ${cmds[$ix]} ..."
    ssh root@${hosts[$ix]} "cd $target; pwd; sh startRB.sh"
done

echo "deploy is done!"

