import sys
import os
import time

def main():
      dir = os.path.dirname(__file__)
      in_file = os.path.join(dir, 'cmd.txt')
      try:
            with open(in_file, 'r') as infile:
                    # count number of lines in file
                for line in infile:
                     print(line)
      except: 
            print(cache_empty)
if __name__ == '__main__':
    main()