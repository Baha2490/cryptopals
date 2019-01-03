#!/usr/bin/python3

from argparse import ArgumentParser

from convert import *
from repeating_key_XOR import repeating_key_XOR
from break_single_byte_XOR_cipher import break_single_byte_XOR_cipher

vprint = None

# if bytes1 and bytes2 don't have the same nb of bytes, distance is computed on the min(len(b1), len(b2)) first bytes
def hamming_distance(bytes1, bytes2):
   return min(len(bytes1), len(bytes2)), sum([bin(b1^b2).count('1') for (b1,b2) in zip(bytes1,bytes2)])

def guess_keysize(ciphertext, max_keysize, hamming_min_nb_byte_pairs):
  best_keysize_score = 8 # init with worst possible hamming distance per byte
  best_keysize = 0

  for keysize in range(1, max_keysize + 1):
    total_nb_byte_pairs_tested = 0
    total_distance = 0
    i = 0

    # the higher the nb of byte pairs on which hamming distance is computed,
    # the smaller the variance of the average distance
    while (total_nb_byte_pairs_tested < hamming_min_nb_byte_pairs):
      if ((i + 1) * keysize > len(ciphertext)):
        break

      chunk1 = ciphertext[i*keysize:(i+1)*keysize]
      chunk2 = ciphertext[(i+1)*keysize:min((i+2)*keysize, len(ciphertext))]

      nb_byte_pairs_tested, distance = hamming_distance(chunk1, chunk2)

      total_nb_byte_pairs_tested += nb_byte_pairs_tested
      total_distance += distance
      i += 1

    if (total_nb_byte_pairs_tested < hamming_min_nb_byte_pairs):
      vprint('keysize >= {} ignored'.format(keysize))
      break

    keysize_score = total_distance / total_nb_byte_pairs_tested
    vprint('keysize: {:<3d} distance: {:.3f}  averaged on {} bytes'.format(keysize, keysize_score, total_nb_byte_pairs_tested))

    if keysize_score < best_keysize_score:
      best_keysize_score = keysize_score
      best_keysize = keysize

  return best_keysize

def break_repeating_key_XOR_given_keysize(ciphertext, keysize):
  repeating_key = b''

  for keypos in range(keysize):
    score, byte_key = break_single_byte_XOR_cipher(ciphertext[keypos::keysize])
    repeating_key += byte_key

  return repeating_key

def main():
  parser = ArgumentParser(description='Break repeating-key XOR cipher')

  parser.add_argument('-v', '--verbose', action='store_true',
                      help='Display process. Output in bytes instead of string.')
  parser.add_argument('-k', '--max_keysize', type=int, required=True, 
                      help='Maximum size of the repeating-key.')
  parser.add_argument('hex_ciphertext', type=str,
                      help='Hex eq string of the ciphertext.')
  parser.add_argument('-b', '--hamming_min_nb_bytes', type=int, default=0,
                      help='Minimum number of byte pairs on which Hamming distance is averaged.')

  args = parser.parse_args()

  if args.verbose:
    _vprint = print
  else:
    _vprint = lambda *a, **k: None

  global vprint
  vprint = _vprint

  ciphertext = hex2bytes(args.hex_ciphertext)
  vprint('Ciphertext length: {}'.format(len(ciphertext)))

  max_keysize = args.max_keysize
  max_keysize = min(max_keysize, len(ciphertext))
  vprint('Max Keysize: {}'.format(max_keysize))
  
  hamming_min_nb_bytes = args.hamming_min_nb_bytes 
  if (hamming_min_nb_bytes == 0):
    hamming_min_nb_bytes = (len(ciphertext) - max_keysize) # default: max value that works for all keysizes
  vprint('Hamming distance averaged on at least {} byte pairs'.format(hamming_min_nb_bytes))

  # guess keysize
  best_keysize = guess_keysize(ciphertext, max_keysize, hamming_min_nb_bytes)
  vprint('Best keysize: {}'.format(best_keysize))

  # break repeating-key XOR chipher given keysize
  repeating_key = break_repeating_key_XOR_given_keysize(ciphertext, best_keysize)
  vprint('Key: {}'.format(repeating_key))

  # print decrypted message
  decrypted_msg = repeating_key_XOR(ciphertext, repeating_key)
  if args.verbose:
    print(decrypted_msg)
  else:
    print(decrypted_msg.decode('utf-8'))

if __name__ == '__main__':
  main()
