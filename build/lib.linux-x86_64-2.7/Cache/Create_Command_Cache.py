# This Program will input all of the commands into our cache. Commands.txt

import sys
import os
def main():
      fullCmdArguments = sys.argv
      dir = os.path.dirname(__file__)
      out_file = os.path.join(dir, 'commands.txt')
      outfile = open(out_file, 'a')
      command = ''
      for word in range(1, len(fullCmdArguments)):
            command += fullCmdArguments[word] + ' '
            outfile.write(fullCmdArguments[word] + ' ')
      outfile.write('\n')
      outfile.close()

if __name__ == '__main__':
    main()