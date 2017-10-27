#!/bin/bash

command=$HOME/furlough/src/find_email_addresses.py

python3.5 ${command} www.jana.com/contact &> jana.txt 
python3.5 ${command} web.mit.edu &> mit.txt 
