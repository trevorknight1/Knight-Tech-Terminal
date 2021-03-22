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
printf "${NC} apt update 
apt -y install build-essential checkinstall 
apt -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev 
wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz 
tar xzf Python-2.7.16.tgz 
cd Python-2.7.16 
./configure --enable-optimizations 
make altinstall \n "
printf "${Yellow}# Step 2: Install the Program \n"
printf "${NC} apt install python2.7 python-pip 
pip2 install -r requirements.txt \n"
echo -e "\e[32m Type 1 to install:"
read -ep " " varname 
 # ----------------------------------------
            if [ "$varname" == "1" ]; then
                  echo -e "\e[32m Installing Knight Tech Terminal:"
                  apt update 
                  apt -y install build-essential checkinstall
                  apt -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
                  echo -e "\e[32m ######################################################## Installing Python 2.7 ##############################################################"
                  wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz
                  tar xzf Python-2.7.16.tgz
                  cd Python-2.7.16
                  ./configure --enable-optimizations
                  make altinstall
                  apt -y install python2.7 python-pip
                  cd ..
                  cd ./Knight-Tech_Terminal/
                  pip2 install -r requirements.txt
                  pip2 install blessings
                  cd ..
                  apt -y install dos2unix
                  cp ./Knight-Tech-Terminal/bin/alias.sh .bash_aliases
                  dos2unix ./bash_aliases
                  chmod 777 .bashrc
                  echo "./Knight-Tech-Terminal/main.sh" >> .bashrc
                  chmod 777 .bashrc
                  dos2unix ./Knight-Tech-Terminal/installation_script.sh
                  clear
                  printf "${Yellow}Knight Tech Terminal Successfully Installed:"
                  printf " ${RED}  Press 1 to ENTER >>"
                  read -ep " " name 
                  if [ "$name" == "1" ]; then
                    ./main.sh
                  fi
            fi