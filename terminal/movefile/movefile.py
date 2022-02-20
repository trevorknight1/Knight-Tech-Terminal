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



