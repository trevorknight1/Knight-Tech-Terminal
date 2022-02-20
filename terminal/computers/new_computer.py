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
      
      file = os.path.join(dir, 'comps.txt')
      with open(file) as json_file:
            computers = json.load(json_file)
      select = term.green("Name this Computer >> " )
      pwds = term.green("This Entry Command >> " )
      input_f = input(select)
      pwd = input(pwds)
      host = get_host()
      if host not in computers:
            computers[host] = {}
      computers[host][input_f.strip()] = pwd
      dir = os.path.dirname(__file__)
      out_file = os.path.join(dir, 'comps.txt')
      outfile = open(out_file, 'w')
      sites = json.dumps(computers)
      outfile.write(sites)
      outfile.close()
main()



