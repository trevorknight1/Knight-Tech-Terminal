from __future__ import print_function
import os

from datetime import datetime
import json
import os
import blessings
term = blessings.Terminal()


dir = os.path.dirname(__file__)
jumpfile = os.path.join(dir, 'jumpsites.txt')

def get_host(): 
      dir = os.path.dirname(__file__)
      pwd = os.getcwd()
      file = os.path.join(dir, '../../information.txt')
      with open(file) as json_file:
            info = json.load(json_file)
      return info['host']


def jumper_box(name, pwd):
      print("^", end='')
      for i in range(0,len(pwd)+4):
            print('-',end="")
      print("^")
      num = len(name)
      add = (len(pwd) - num)/2
      print("^  ", end='')
      for i in range(0, int(add)):
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



with open(jumpfile) as json_file:
      jump_sites = json.load(json_file)


def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw
    
tw = terminal_size()
count = 0
max = 0
host = get_host()
if host not in jump_sites: 
    jump_sites[host] = {}
for site in jump_sites[host]: 
      if len(jump_sites[host][site]) > max:
            max = len(jump_sites[host][site])
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
      add = int((length - num)/2)
      print(arrow + "  ", end='')
      for i in range(0,int(add)):
                  print(term.blue_on_white(' '),end="")
      if (len(name) % 2) == 0:
                  print(term.blue_on_white(' '),end="")
      print(term.blue_on_white(name),end='')
      for i in range(0,add):
            print(term.blue_on_white(' '),end="")
      print("  "+ arrow,end="")

def edit_sites(name):
      host = get_host()
      with open(jumpfile) as json_file:
            jump_sites = json.load(json_file)
      names = name.split(" ")[1]
      if names in jump_sites[host]:
            del jump_sites[host][names]
      outfile = open(jumpfile, 'w')
      sites = json.dumps(jump_sites)
      outfile.write(sites)
      outfile.close()

def remove_sites():
      jump_sites[host] = {}
      outfile = open(jumpfile, 'w')
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
host = get_host()
if host not in jump_sites: 
    jump_sites[host] = {}

for name in jump_sites[host]:
      if set not in jumpsets:
            jumpsets[set] = {}
      jumpsets[set][name] = jump_sites[host][name]
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
            print_name(jump_sites[host][name], length=max+4)
            print("  ",end='')
      print()
      print_top(len(jumpsets[set]), max+4)
      print()
print(term.white("To remove a jumpsite type \"rm <name>\"" ))
print(term.white("To remove all jumpsites type \"remove all\"" ))
select = term.green("Select Jump Site >> " )
inputf = raw_input(select)

dir = os.path.dirname(__file__)
out_file = os.path.join(dir, '../cmd_op/cmd.txt')
outfile = open(out_file, 'w')

if "rm" in inputf:
      edit_sites(inputf)
elif "remove all" == inputf:
      remove_sites()
elif inputf in jump_sites[host]:
      outfile.write("cd "+ jump_sites[host][inputf])
else:
      outfile.write("")
outfile.close()


def edit_sites(name):
      pwd = os.getcwd()
      with open(jumpfile) as json_file:
            jump_sites = json.load(json_file)
      host = get_host()
      jump_sites[host].remove(name)
      outfile = open(jumpfile, 'w')
      sites = json.dumps(jump_sites)
      outfile.write(sites)
      outfile.close()
