import os
import json
import blessings
term = blessings.Terminal()





def main():
      dir = os.path.dirname(__file__)
      
      file = os.path.join(dir, 'alias.txt')
      with open(file) as json_file:
            jump_sites = json.load(json_file)
      select = term.green("Name this Command >> " )
      cmd = term.green("Type Command >> " )
      input = raw_input(select)
      input2 = input(cmd)
      jump_sites[input.strip()] = input2
      dir = os.path.dirname(__file__)
      out_file = os.path.join(dir, 'alias.txt')
      outfile = open(out_file, 'w')
      sites = json.dumps(jump_sites)
      outfile.write(sites)
      outfile.close()
main()
