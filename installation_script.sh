#!/bin/bash

clear

# --------------------------------------------
RED='\033[0;31m'
Yellow='\033[1;33m' # Yellow
NC='\033[0m' # No Color
#---------------------------------------------

apt install dos2unix
clear
printf "${RED}-----------------------------------------------------------------${Yellow}Knight Tech${RED}-----------------------------------------------------------------${NC}\n"
printf "${Yellow}Thank you for using the Knight Tech Terminal. This shell program has many features that will make your terminal experience easier and faster. ${NC}\n"
echo -e "\e[32m Make sure that your in the home directory, more specifically, where your .bashrc or ./bash_profile lives."
echo -e "\e[32m Then for Automatic Installation type 1:"
echo -e "\e[32m Type 1 to install:"
read -ep " " varname 
 # ----------------------------------------
            if [ "$varname" == "1" ]; then
                  echo -e "\e[32m Installing Knight Tech Terminal:"

                  

                  apt update 
                  apt -y install build-essential checkinstall
                  apt -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
                  echo -e "\e[32m ######################################################## Installing Python  ############################################################"
                  if [ ! -f ~/Python-2.7.16 ]; then
                        wget https://www.python.org/ftp/python/2.7.16/Python-2.7.16.tgz
                        tar xzf Python-2.7.16.tgz
                        rm -rf Python-2.7.16.tgz
                  fi
                  cd ~Python-2.7.16
                  ./configure --enable-optimizations
                  make altinstall
                  apt -y install python2.7 python-pip
                  cd ~/Knight-Tech-Terminal/
                  echo -e "\e[32m ######################################################## Installing Additional Requirements ###############################################"
                  pip2 install -r requirements.txt
                  pip2 install blessings
                  cd ..
                  echo -e "\e[32m ######################################################## Fixing Up Aliases ################################################################"
                  apt -y install dos2unix
                  cp ~/Knight-Tech-Terminal/bin/bash_aliases.sh ~/.bash_aliases
                  dos2unix ~/.bash_aliases
                  . ~/.bash_aliases
                  chmod 777 ~/.bashrc
                  echo -e "\e[32m ######################################################## Setting Up Terminal ##############################################################"
                  echo "~/Knight-Tech-Terminal/main.sh" >> ~/.bashrc
                  chmod 777 ~/.bashrc
                  dos2unix ~/Knight-Tech-Terminal/installation_script.sh
                  
                  loading="python ./Knight-Tech-Terminal/terminal/loadingbar.py"
                  $loading
                  
                  MENU="python ./Knight-Tech-Terminal/terminal/menu.py"
                  $MENU
                  printf "${Yellow}Knight Tech Terminal Successfully Installed:"
                  printf " ${RED}  Press 1 to ENTER >>"
                  read -ep " " name 
                  if [ "$name" == "1" ]; then
                    ~/Knight-Tech-Terminal/main.sh
                  fi
            fi





