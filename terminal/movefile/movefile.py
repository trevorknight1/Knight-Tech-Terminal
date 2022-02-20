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

def main():
      select = term.green("Select File To Move >> " )
      input_f = input(select)
      if os.path.isfile(join(os.getcwd(), input_f)):
            notice = term.yellow("File Selected")
      elif os.path.isdir(join(os.getcwd(), input_f)):
            notice = term.yellow("Directory Selected")
      else:
           notice =  term.yellow("not a directory or file")
           
      print(notice)
      print(os.path.abspath(join(os.getcwd(), input_f))
     
  
                        
      
main()



