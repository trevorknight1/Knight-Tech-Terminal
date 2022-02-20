from __future__ import print_function
import os
from datetime import datetime
import json
import os
import blessings 
import fcntl, termios, struct
term = blessings.Terminal()
arrow = term.bold_white_on_blue('^')
dash = term.white('-')


menu = term.yellow('<< Feature Tools 2021 >>')
def terminal_size():
      th, tw, hp, wp = struct.unpack('HHHH',
            fcntl.ioctl(0, termios.TIOCGWINSZ,
            struct.pack('HHHH', 0, 0, 0, 0)))
      for i in range(0,int(tw/2-len(menu)/2)+4):
            print(dash,end='')
      print(menu,end='')
      for i in range(0,int(tw/2 - len(menu)/2)+4):
            print(dash,end='')
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
      add = int((length - num)/2)
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
    "alias" : "view: alias | create: create alias",
    "jumper" : "view: jumper | create: create jumper",
    "ssh VPN/Server" : "view: computers | create: create computer",
    "command cache" : "down arrow",
    "menu" : "view: menu",
    "exit terminal" : "CTRL C",
    "re-enter terminal" : "knighttech"
}

set = 0 
print()

count = 0
max = 0
for title in command: 
      if len(command[title]) > max:
            max = len(command[title])
      elif len(command[title][txt]) > max:
            max = len(command[title][txt])
      count = count + 1


boxes_per_line = (tw / (max+8))-1
if count < boxes_per_line: 
      boxes_per_line = count

command_set = {}
count = 0
for name in command:
      if set not in command_set:
            command_set[set] = {}
      command_set[set][name] = command[name]
      if count >= boxes_per_line: 
            set = set + 1
            count = 0
      else: 
            count = count + 1 

for set in command_set:
      if max % 2 == 0: 
            max = max + 1
      print_top(len(command_set[set]), max+4)
      for name in command_set[set]:
            print_name(name, length=max+4)
            print("  ",end='')
      print()
      for name in command_set[set]:
            print_name(command[name], length=max+4)
            print("  ",end='')
      print()
      print_top(len(command_set[set]), max+4)
      print()
