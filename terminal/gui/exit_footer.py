from __future__ import print_function
from datetime import datetime
import time
import os
import blessings
term = blessings.Terminal()

try:
      dir = os.path.dirname(__file__)
      file = os.path.join(dir, '../cache/commands.txt')  # change filename here
      os.remove(file) 
except:
      pass
dash = term.yellow('-')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
knight_tech = term.red(current_time)

def terminal_size():
    import fcntl, termios, struct
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))

    for i in range(0,(tw/2-len(knight_tech)/2)+4):
      print(dash,end='')
    print(knight_tech,end='')
    for i in range(0,(tw/2 - len(knight_tech)/2)+4):
      print(dash,end='')

terminal_size()

print()
time.sleep(4)