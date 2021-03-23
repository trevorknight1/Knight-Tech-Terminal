#!/bin/bash

# --------------------------------------------
RED='\033[0;31m'
Yellow='\033[1;33m' # Yellow
NC='\033[0m' # No Color

bind '"\e[B": "Cache'
SOURCE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
clear
# -----------------GUI FILES---------------------
HEADER="python $SOURCE/terminal/gui/header.py"
FOOTER="python $SOURCE/terminal/gui/exit_footer.py"
MENU="python $SOURCE/terminal/menu.py"
# -----------------------------------------------
# ----------------JUMPER FILES-------------------
JUMPER="python $SOURCE/terminal/jumper/jumper.py"
CREATE_JUMP="python $SOURCE/terminal/jumper/new_jumpsite.py"
# -----------------------------------------------
# -----------------CACHE FILES-------------------
CMD="python $SOURCE/terminal/cache/command_cache.py"
# -----------------------------------------------
# ----------------ALIAS FILES-------------------
ALIAS="python $SOURCE/terminal/alias/alias.py"
CREATE_ALIAS="python $SOURCE/terminal/alias/new_alias.py"
# -----------------------------------------------
# ----------------COMPUTER FILES-------------------
COMPUTER="python $SOURCE/terminal/computers/computer.py"
CREATE_COMPUTER="python $SOURCE/terminal/computers/new_computer.py"
# -----------------------------------------------
$HEADER
while [ "$varname" != "quit" ]
      do
            # Start Up Functionality -----------------
            printf "${RED}Knight Tech ${Yellow}>>${NC}"
            read -ep " " varname 
            VARIABLE=`python $SOURCE/terminal/cmd_op/iscd.py $varname`
            isalias=`python $SOURCE/terminal/alias/isalias.py $varname`
            # ----------------------------------------
            if [ "$varname" == "cache" ]; then
                  $CMD 
                  `python $SOURCE/terminal/cmd_op/get_cmd.py`

            elif [ "$VARIABLE" == "True" ]; then
                  $varname
                  pwd
            elif [ "$varname" == "quit" ]; then
                  $FOOTER
            elif [ "$varname" == "jumper" ]; then
                  $JUMPER
                  `python $SOURCE/terminal/cmd_op/get_cmd.py`
                  pwd
            elif [ "$varname" == "computers" ]; then
                  $COMPUTER
                  `python $SOURCE/terminal/cmd_op/get_cmd.py`
            elif [ "$varname" == "create computer" ]; then
                  $CREATE_COMPUTER
                  `python $SOURCE/terminal/cmd_op/get_cmd.py`
            elif [ "$varname" == "menu" ]; then
                  $MENU
            elif [ "$varname" == "create jumper" ]; then
                  $CREATE_JUMP
            elif [ "$varname" == "create alias" ]; then
                  $CREATE_ALIAS
            elif [ "$varname" == "alias" ]; then
                  $ALIAS
                  `python $SOURCE/terminal/cmd_op/get_cmd.py`
            elif [ "$varname" == "help" ]; then
                  echo "create jumper jumper"
            elif [ "$isalias" == "True" ]; then
                  `python $SOURCE/terminal/cmd_op/get_cmd.py`
            else
                  python $SOURCE/terminal/cache/create_command_cache.py $varname
                  $varname
            fi
      done

