#!/bin/bash

command=$HOME/furlough/src/emailFinder.py

python3.5 ${command} www.jana.com &> jana.txt &
python3.5 ${command} web.mit.edu &> mit.txt &
