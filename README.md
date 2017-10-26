## 2017-10-26
# Katya Notkin
# 
#
The following instructions are for Linux. 


Virgin AWS ubuntu EC2 instance setup (

Part 1 - mostly manual

0) ssh to EC2, for example: 
> $ ssh -i "mykeys.pem" ubuntu@<public dns>

1.1) clone code from github into 

> $ git init; git clone https://github.com/knot-mem/furlough  

1)
 
> $ REPO=$HOME/furlough


2) Execute setup & deployment script

> $ cd ${REPO}/scripts

While executing `setupEnv` script below answer positively to all prompts (<ENTER>, "yes", "Y"); 
> $ ./setupEnv.sh 


3) Activate virtual env, run tests and observe results of testing 

> $ source ${REPO}/env/bin/activate

> $ cd ${REPO}

> $ pytest -s -vv tests/

You can save report in html format at the same time (easier to analyze and share), e.g.:
 
> $ pytest --html=ReportTest.html --self-contained-html -s -vv tests/

