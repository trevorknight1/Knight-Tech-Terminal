from __future__ import print_function
import os
from datetime import datetime
import json
import os
import blessings
term = blessings.Terminal()
arrow = term.bold_white_on_blue('^')
dash = term.white('-')

def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw
    
tw = terminal_size()

def print_top(number, length):
      for j in range(0,number):
            print(arrow, end='')
            for i in range(0,length+4):
                  print(dash,end="")
            print(arrow,end='')
            print("  ",end='')
      print()

def print_name(name, length):
      num = len(name)
      add = (length - num)/2
      print(arrow + "  ", end='')
      for i in range(0,add):
                  print(term.blue_on_white(' '),end="")
      if (len(name) % 2) == 0:
                  print(term.blue_on_white(' '),end="")
      print(term.blue_on_white(name),end='')
      for i in range(0,add):
            print(term.blue_on_white(' '),end="")
      print("  "+ arrow,end="")

command = {
    "alias" : ["View aliases command: alias", "Create alias command: create alias"],
    "jumper" : ["View jump sites: jumper", "Create jump site: create jumper"]
}
set = 0 
print()

count = 0

max = 0
for title in command: 
    for text in command[title]: 
      if len(command[title][text]) > max:
            max = len(command[title][text])
      count = count + 1


for tool in command:
      if max % 2 == 0: 
            max = max + 1
      print_top(len(command[tool]), max+4)
      for name in command[tool]:
            print_name(name, length=max+4)
            print("  ",end='')
      print()
      for name in command[set]:
            print_name(command[tool][text], length=max+4)
            print("  ",end='')
      print()
      print_top(len(command[set]), max+4)
      print()
print(term.white("To remove a jumpsite type \"rm <name>\"" ))
print(term.white("To remove all jumpsites type \"remove all\"" ))
select = term.green("Select Jump Site >> " )      