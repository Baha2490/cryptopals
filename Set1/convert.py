#!/usr/bin/python3

import sys
import binascii

def print_b64(bytesval):
  print(binascii.b2a_base64(bytesval)[:-1].decode('ascii'))

def print_hex(bytesval):
  print(binascii.b2a_hex(bytesval).decode('ascii'))

def print_bin(bytesval):
  intval = int.from_bytes(bytesval, 'big')
  binstring = bin(intval)[2:]
  print(binstring.zfill((len(binstring) + 7) // 8 * 8))


def b642bytes(b64str):
  return binascii.a2b_base64(b64str)

def hex2bytes(hexstr):
  return binascii.a2b_hex(hexstr)

def bin2bytes(binstring):
  return int(binstring, 2).to_bytes((len(binstring) + 7) // 8, byteorder='big')

"""
def bytes2int(bytesval):
  return int.from_bytes(bytesval, byteorder='big')  

def int2bytes(intval):
  return intval.to_bytes((intval.bit_length() + 7) // 8, byteorder='big')
"""

def main():
  if len(sys.argv) not in [3, 4]:
    print('{} in_type input (out_type)'.format(sys.argv[0]))
    print('types: str, hex, bin, b64')
    return

  in_type = sys.argv[1]
  inp = sys.argv[2]

  if in_type == 'str':
    bytesval = inp.encode('utf-8')
  elif in_type == 'hex':
    bytesval = hex2bytes(inp)
  elif in_type == 'bin':
    bytesval = bin2bytes(inp)
  elif in_type == 'b64':
    bytesval = b642bytes(inp)
  else:
    print('invalid input type')
    return

  if len(sys.argv) == 4:
    out_type = sys.argv[3]
  else:
    out_type = 'display'

  if out_type == 'str':
    try:
      print(bytesval.decode('utf-8'))
    except:
      print('Not a valid UTF-8 string')
  if out_type == 'display':
    print(bytesval)
  if out_type == 'hex' or out_type == 'display':
    print_hex(bytesval)
  if out_type == 'bin' or out_type == 'display':
    print_bin(bytesval)
  if out_type == 'b64' or out_type == 'display':
    print_b64(bytesval)

if __name__ == '__main__':
  main()

