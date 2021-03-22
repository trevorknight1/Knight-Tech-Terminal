from __future__ import print_function
import os
import blessings
term = blessings.Terminal()
import json

def isalias(input):

      dir = os.path.dirname(__file__)
      aliasfile = os.path.join(dir, '../alias/alias.txt')
      with open(aliasfile) as json_file:
            aliases = json.load(json_file)
      new_st = input.strip()
      if new_st in aliases:
           return aliases[str(new_st)]
      else: 
           return "False"


Knight_tech = term.red('Knight Tech') + ' ' + term.yellow('>') + term.green('> ')
cache_empty = term.yellow('Nothing in the Cache')

dir = os.path.dirname(__file__)
input_file = os.path.join(dir, 'commands.txt')  # change filename here
out_file = os.path.join(dir, '../cmd_op/cmd.txt')
commands = []

try:
      outfile = open(out_file, 'w').close()
      with open(input_file, 'r') as infile:
              # count number of lines in file
          for line in infile:
               commands.append(line)
          cmds =[]
          if len(commands) > 10: 
            for i in range(len(commands)-10, len(commands)):
                  cmds.append(commands[i])
          else: 
            for cmd in commands:
                  cmds.append(cmd)
            cmds.reverse()
            num_lines = 0
except: 
      print(cache_empty)
      exit(0)
good = True
while good:
      num_lines = 0
      for cmd in cmds:
            print(str(num_lines) + ": " + str(cmd), end='')
            num_lines += 1
      dirty_in = raw_input(Knight_tech)
      input = dirty_in.strip()
      input = str(input)
      outfile = open(out_file, 'w')
      try:
            if int(input) in range(0,len(cmds)):
                  if isalias(input=cmds[int(input)]) is not "False":
                        outfile.write(isalias(input=cmds[int(input)]))
                  else:
                        outfile.write(cmds[int(input)])
                  outfile.close()
                  good = False
      except: 
            outfile.write(input)
            good = False


exit(0)

