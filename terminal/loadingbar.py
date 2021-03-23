from __future__ import print_function
import os
from datetime import datetime
import json
import os
import blessings 
import fcntl, termios, struct
from time import sleep

term = blessings.Terminal()
arrow = term.bold_white_on_blue('^')
dash = term.white('-')


menu = term.yellow('<< Getting Ready >>')
loading = term.yellow('Loading [')
endloading = term.yellow('] Completed')
loadpartical = term.green('#')
def terminal_size():
      th, tw, hp, wp = struct.unpack('HHHH',
            fcntl.ioctl(0, termios.TIOCGWINSZ,
            struct.pack('HHHH', 0, 0, 0, 0)))
      for i in range(0,int(tw/2-len(menu)/2)+4):
            print(dash,end='')
      print(menu,end='')
      for i in range(0,int(tw/2 - len(menu)/2)+4):
            print(dash,end='')
      return tw
tw = terminal_size()
print()
print()
print(loading, end='')
for i in range(0, int(tw-24)):
    print(loadpartical, end='')
    sleep(.005)
print(endloading, end='')
print()
print()
print()
print()


