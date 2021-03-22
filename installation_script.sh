#!/bin/bash

clear

# --------------------------------------------
RED='\033[0;31m'
Yellow='\033[1;33m' # Yellow
NC='\033[0m' # No Color
#---------------------------------------------


apt install dos2unix
printf "${RED}-----------------------------------------------------------------${Yellow}Knight Tech${RED}-----------------------------------------------------------------${NC}\n"
printf "${Yellow}Thank you for using the Knight Tech Terminal. This shell program has many features that will make your terminal experience easier and faster. ${NC}\n"
echo -e "\e[32m Make sure that your in the home directory, more specifically, where your .bashrc or ./bash_profile lives."
echo -e "\e[32m Then for Automatic Installation type 1:"
printf "${Yellow}Follow the installation instructions below and we will be up and running in no time. ${NC}\n"
printf "Otherwise You can run these commands sequentially, in the home directory of your terminal or the entry point of your terminal.\n"
printf "${Yellow}# Step 1: Install python2.7\n"
printf "${RED} Notice: This version might be different on your computer, this is the python used to run the program. If you don't have python2.7 you need to install it\n" 
printf "${NC}sudo apt-get update 
sudo apt-get install build-essential checkinstall 
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev 
sudo wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz 
sudo tar xzf Python-2.7.16.tgz 
cd Python-2.7.16 
sudo ./configure --enable-optimizations 
sudo make altinstall \n "
printf "${Yellow}# Step 2: Install the Program \n"
printf "${NC} sudo apt install python2.7 python-pip 
pip2 install -r requirements.txt \n"
echo -e "\e[32m Type 1 to install:"
read -ep " " varname 
 # ----------------------------------------
            if [ "$varname" == "1" ]; then
                  echo -e "\e[32m Installing Knight Tech Terminal:"
                  apt-get update 
                  apt-get install build-essential checkinstall
                  apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
                  wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz
                  tar xzf Python-2.7.16.tgz
                  cd Python-2.7.16
                  ./configure --enable-optimizations
                  make altinstall
                  apt install python2.7 python-pip
                  pip2 install -r requirements.txt
                  

                  cp ./bin/alias.sh .bash_aliases
                  dos2unix ./bash_aliases
                  echo "./bash_aliases" >> .bashrc
                  echo "./KnightTechTerminal/main.sh" >> .bashrc
                  clear
                  printf "${Yellow}Knight Tech Terminal Successfully Installed:${RED}  Press 1 to ENTER >>"
                  read -ep " " name 
                  if [ "$name" == "1" ]; then
                    ./KnightTechTerminal/tech.sh
                  fi
            fi