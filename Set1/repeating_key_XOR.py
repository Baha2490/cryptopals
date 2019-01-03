#!/usr/bin/python3

import sys
from itertools import cycle

from convert import *

# input should be in bytes
def repeating_key_XOR(msg, key):
  XOR_int_array = [m^k for (m,k) in zip(msg, cycle(key))]
  return bytes(XOR_int_array)

def main():
  if len(sys.argv) not in [5, 6]:
    print('{} msg_type msg key_type key (out_type)'.format(sys.argv[0]))
    print('types: str, hex')
    return

  msg_inp_type = sys.argv[1]
  msg_inp = sys.argv[2]

  if msg_inp_type == 'str':
    msg = msg_inp.encode('utf-8')
  elif msg_inp_type == 'hex':
    msg = hex2bytes(msg_inp)
  else:
    print("invalid msg type")
    return

  key_inp_type = sys.argv[3]
  key_inp = sys.argv[4]

  if key_inp_type == 'str':
    key = key_inp.encode('utf-8')
  elif key_inp_type == 'hex':
    key = hex2bytes(key_inp)
  else:
    print("invalid key type")
    return

  XORed_msg = repeating_key_XOR(msg, key)

  if len(sys.argv) == 6:
    out_type = sys.argv[5]
  else:
    out_type = 'display'

  if out_type == 'str':
    try:
      print(XORed_msg.decode('utf-8'))
    except:
      print('Not a valid UTF-8 string')
  if out_type == 'display':
    print(XORed_msg)
  if out_type == 'hex' or out_type == 'display':
    print_hex(XORed_msg)

if __name__ == '__main__':
  main()
