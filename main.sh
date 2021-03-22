#!/bin/bash

# --------------------------------------------
RED='\033[0;31m'
Yellow='\033[1;33m' # Yellow
NC='\033[0m' # No Color

bind '"\e[B": "Cache'
SOURCE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
clear
# -----------------GUI FILES---------------------
HEADER="python $SOURCE/terminal/GUI/header.py"
FOOTER="python $SOURCE/terminal/GUI/exit_footer.py"
# -----------------------------------------------
# ----------------JUMPER FILES-------------------
JUMPER="python $SOURCE/terminal/Jumper/jumper.py"
CREATE_JUMP="python $SOURCE/terminal/Jumper/new_jumpsite.py"
# -----------------------------------------------
# -----------------CACHE FILES-------------------
CMD="python $SOURCE/terminal/Cache/Command_Cache.py"
# -----------------------------------------------
# ----------------ALIAS FILES-------------------
ALIAS="python $SOURCE/terminal/Alias/alias.py"
CREATE_ALIAS="python $SOURCE/terminal/Alias/new_alias.py"
# -----------------------------------------------
# ----------------COMPUTER FILES-------------------
COMPUTER="python $SOURCE/terminal/Computers/computer.py"
CREATE_COMPUTER="python $SOURCE/terminal/Computers/new_computer.py"
# -----------------------------------------------
$HEADER
while [ "$varname" != "quit" ]
      do
            # Start Up Functionality -----------------
            printf "${RED}Knight Tech ${Yellow}>>${NC}"
            read -ep " " varname 
            VARIABLE=`python $SOURCE/terminal/CMD_OP/iscd.py $varname`
            isalias=`python $SOURCE/terminal/Alias/isalias.py $varname`
            # ----------------------------------------
            if [ "$varname" == "Cache" ]; then
                  $CMD 
                  `python $SOURCE/terminal/CMD_OP/get_cmd.py`

            elif [ "$VARIABLE" == "True" ]; then
                  $varname
                  pwd
            elif [ "$varname" == "quit" ]; then
                  $FOOTER
            elif [ "$varname" == "jumper" ]; then
                  $JUMPER
                  `python $SOURCE/terminal/CMD_OP/get_cmd.py`
                  pwd
            elif [ "$varname" == "computer" ]; then
                  $COMPUTER
                  `python $SOURCE/terminal/CMD_OP/get_cmd.py`
            elif [ "$varname" == "create computer" ]; then
                  $CREATE_COMPUTER
                  `python $SOURCE/terminal/CMD_OP/get_cmd.py`
            elif [ "$varname" == "create jumper" ]; then
                  $CREATE_JUMP
            elif [ "$varname" == "create alias" ]; then
                  $CREATE_ALIAS
            elif [ "$varname" == "alias" ]; then
                  $ALIAS
                  `python $SOURCE/terminal/CMD_OP/get_cmd.py`
            elif [ "$varname" == "help" ]; then
                  echo "create jumper jumper"
            elif [ "$isalias" == "True" ]; then
                  `python $SOURCE/terminal/CMD_OP/get_cmd.py`
            else
                  python $SOURCE/terminal/Cache/Create_Command_Cache.py $varname
                  $varname
            fi
      done

