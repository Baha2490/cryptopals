#!/usr/bin/python3

import sys

from convert import *
from language import english_score
from repeating_key_XOR import repeating_key_XOR

def break_single_byte_XOR_cipher(ciphertext):
  best_score = 0

  for i in range(256):
    key = i.to_bytes(1, byteorder='big')

    msg = repeating_key_XOR(ciphertext, key)
    score = english_score(msg)

    if (score > best_score):
      best_score = score
      best_key = key

  return best_score, best_key

def main():
  if (len(sys.argv) != 2):
    print('{} hex_ciphertext'.format(sys.argv[0]))
    return

  hex_ciphertext = sys.argv[1]
  ciphertext = hex2bytes(hex_ciphertext)

  score, key = break_single_byte_XOR_cipher(ciphertext)  

  print('Key: {} (Score: {})'.format(key, score))
  print('Msg: {}'.format(repeating_key_XOR(ciphertext, key)))

if __name__ == '__main__':
  main()
