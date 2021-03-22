import sys
import os

def main():
      fullCmdArguments = sys.argv

      command = ''
      for word in range(1, len(fullCmdArguments)):
            command += fullCmdArguments[word] + ' '

      if 'cd' in command:
           print("True")
      else: 
           print("False")

if __name__ == '__main__':
    main()
