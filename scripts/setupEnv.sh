#!/bin/bash
echo "Virgin AWS ubuntu EC2 instance setup"
echo "Setting up Python 3.5"
cd
echo "$ git init"
echo "$ git clone <>"

sudo apt-get install python3

echo '#!/bin/bash' > .bash_aliases
echo alias python="/usr/bin/python3" >> .bash_aliases
echo alias python3="/usr/bin/python3.5" >> .bash_aliases
source .bash_aliases

sudo apt install virtualenv

# the next 2 exports are needed for this flavor/version of ubuntu"
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"

REPO=$HOME/furlough
cd ${REPO}

virtualenv --python=python3.5 env
source env/bin/activate
pip install -r requirements.txt

