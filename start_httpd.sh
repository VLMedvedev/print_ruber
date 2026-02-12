#!/bin/bash

killall python
killall python3

cd /home/user/print_ruber

./cgiserver.py &

exit 0

