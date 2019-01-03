#!/usr/bin/python3

import sys

from convert import *
from repeating_key_XOR import repeating_key_XOR
from break_single_byte_XOR_cipher import break_single_byte_XOR_cipher

def main():
  # argument is a file containing hex strings, one of which is a message encrypted with single-byte XOR cipher
  filename = sys.argv[1]
  file = open(filename, 'r')

  best_score = 0

  for line in file:
    msg = hex2bytes(line.rstrip('\n'))
    score, key = break_single_byte_XOR_cipher(msg)

    if (score > best_score):
      best_score = score
      best_key = key
      best_msg = msg

  print_hex(best_msg)
  print('Key: {} (Score: {})'.format(best_key, best_score))
  print('Msg: {}'.format(repeating_key_XOR(best_msg, best_key)))

if __name__ == '__main__':
  main()
