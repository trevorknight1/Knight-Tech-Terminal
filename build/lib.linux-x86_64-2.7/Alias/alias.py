from __future__ import print_function
import os

from datetime import datetime
import json
import os
import blessings
term = blessings.Terminal()


dir = os.path.dirname(__file__)
aliasfile = os.path.join(dir, 'alias.txt')

def jumper_box(name, pwd):
      print("^", end='')
      for i in range(0,len(pwd)+4):
            print('-',end="")
      print("^")
      num = len(name)
      add = (len(pwd) - num)/2
      print("^  ", end='')
      for i in range(0,add):
                  print(' ',end="")
      if (len(name) % 2) == 0:
                  print(' ',end="")
      print(name,end='')
      for i in range(0,add):
            print(' ',end="")
      print('  ^')
      print("^  " + pwd + "  ^")
      print("^", end='')
      for i in range(0,len(pwd)+4):
            print('-',end="")
      print("^")



#jumper_box("hello", "pwd/hello")
#jumper_box("help", "pwd/hello")



with open(aliasfile) as json_file:
      aliases = json.load(json_file)


def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))

    return tw
    
tw = terminal_size()
count = 0
max = 0
for site in aliases: 
      if len(aliases[site]) > max:
            max = len(aliases[site])
      count = count + 1

boxes_per_line = (tw / (max+8))-1
if count < boxes_per_line: 
      boxes_per_line = count


arrow = term.bold_white_on_blue('^')
dash = term.white('-')



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

def edit_sites(name):
      with open(aliasfile) as json_file:
            jump_sites = json.load(json_file)
      names = name.split(" ")[1]
      if names in jump_sites:
            del jump_sites[names]
      outfile = open(aliasfile, 'w')
      sites = json.dumps(jump_sites)
      outfile.write(sites)
      outfile.close()

def remove_sites():
      jump_sites = {}
      outfile = open(aliasfile, 'w')
      sites = json.dumps(jump_sites)
      outfile.write(sites)
      outfile.close()

empty = False
numbers = []
listed = []
i = 0 


jumpsets = {}
set = 0 
count = 0 
print()
for name in aliases:
      if set not in jumpsets:
            jumpsets[set] = {}
      jumpsets[set][name] = aliases[name]
      if count >= boxes_per_line: 
            set = set + 1
            count = 0
      else: 
            count = count + 1 

for set in jumpsets:
      if max % 2 == 0: 
            max = max + 1
      print_top(len(jumpsets[set]), max+4)
      for name in jumpsets[set]:
            print_name(name, length=max+4)
            print("  ",end='')
      print()
      for name in jumpsets[set]:
            print_name(aliases[name], length=max+4)
            print("  ",end='')
      print()
      print_top(len(jumpsets[set]), max+4)
      print()
print(term.white("To remove an alias e type \"rm <name>\"" ))
print(term.white("To remove all alias type \"remove all\"" ))
select = term.green("Select alias command >> " )
input = raw_input(select)

dir = os.path.dirname(__file__)
out_file = os.path.join(dir, '../CMD_OP/cmd.txt')
outfile = open(out_file, 'w')

if "rm" in input:
      edit_sites(input)
elif "remove all" == input:
      remove_sites()
elif input in aliases:
      outfile.write(aliases[input])
else:
      outfile.write("")
outfile.close()


def edit_sites(name):
      pwd = os.getcwd()
      with open(aliasfile) as json_file:
            jump_sites = json.load(json_file)
      jump_sites.remove(name)
      outfile = open(aliasfile, 'w')
      sites = json.dumps(jump_sites)
      outfile.write(sites)
      outfile.close()