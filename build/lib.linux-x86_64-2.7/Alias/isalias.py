import sys
import os
import json
def main():

      dir = os.path.dirname(__file__)
      aliasfile = os.path.join(dir, 'alias.txt')
      fullCmdArguments = sys.argv
      with open(aliasfile) as json_file:
            aliases = json.load(json_file)
      command = ''
      for word in range(1, len(fullCmdArguments)):
            command += fullCmdArguments[word] + ' '

      c = command.strip()
      if c in aliases:
            dir = os.path.dirname(__file__)
            out_file = os.path.join(dir, '../CMD_OP/cmd.txt')
            outfile = open(out_file, 'w')
            outfile.write(aliases[c])
            outfile.close()
            print("True")
      else: 
            print("False")

if __name__ == '__main__':
    main()

