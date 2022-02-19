import os
import json
import blessings
term = blessings.Terminal()

def get_host(): 
      dir = os.path.dirname(__file__)
      pwd = os.getcwd()
      file = os.path.join(dir, '../../information.txt')
      with open(file) as json_file:
            info = json.load(json_file)
      return info['host']

def main():
      dir = os.path.dirname(__file__)
      pwd = os.getcwd()
      file = os.path.join(dir, 'jumpsites.txt')
      with open(file) as json_file:
            jump_sites = json.load(json_file)
      select = term.green("Name this Jumpsite >> " )
      input_f = input(select)
      host = get_host()
      if host not in jump_sites:
            jump_sites[host] = {}
      jump_sites[host][input_f.strip()] = pwd
      dir = os.path.dirname(__file__)
      out_file = os.path.join(dir, 'jumpsites.txt')
      outfile = open(out_file, 'w')
      sites = json.dumps(jump_sites)
      outfile.write(sites)
      outfile.close()
main()



