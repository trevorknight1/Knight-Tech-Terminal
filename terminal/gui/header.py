from __future__ import print_function
import os
import blessings
term = blessings.Terminal()
import fcntl, termios, struct
try:
      os.remove("commands.txt") 
except:
      pass
dash = term.yellow('-')
knight_tech = term.red('<< Knight Tech Terminal >>')

def terminal_size():

    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))

    for i in range(0,int(tw/2-len(knight_tech)/2)+4):
      print(dash,end='')
    print(knight_tech,end='')
    for i in range(0,int(tw/2 - len(knight_tech)/2)+4):
      print(dash,end='')

terminal_size()
print()


json_data = {}

def get_host(dictionary):
      import socket
      import json
      from datetime import date
      today = date.today()
      hostname = socket.gethostname()
      dictionary['host'] = hostname 
      dictionary['today'] = str(today) 
      data = json.dumps(json_data)
      dir = os.path.dirname(__file__)
      out_file = os.path.join(dir, '../../information.txt')
      outfile = open(out_file, 'w')
      data = json.dumps(dictionary)
      outfile.write(data)
      outfile.close()

get_host(json_data)

def Host_and_Date(json_data):

    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))

    print(term.yellow(json_data['host']),end='')
    for i in range(0,int(tw/2-len(knight_tech)/2)+4):
      print(" ",end='')
    for i in range(0,int(tw/2 - len(knight_tech)/2)+4):
      print(" ",end='')
    print(" " + term.yellow(json_data['today']))

Host_and_Date(json_data)

def Options():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
     Menu = term.yellow('For Terminal Tools -> menu')
    print(Menu,end='')
    for i in range(0,int(tw/2-len(knight_tech)/2)+4):
      print(" ",end='')
    for i in range(0,int(tw/2 - len(knight_tech)/2)+4):
      print(" ",end='')
    print(" " + term.yellow(json_data['today']))
print() 
