#!/usr/bin/python3

import sys
from os.path import dirname
import numpy 
from string import ascii_lowercase


def main():
  # ugly hack, f**k you Python
  sys.path.append(dirname(sys.path[0]))

  from language import english_letters_freq

  count = int(sys.argv[1]) # number of generated tuples of characters


  print('Average Hamming distance between:')

  total_distance = 0
  for c1 in ascii_lowercase:
    for c2 in ascii_lowercase:
      hamming_distance = bin(ord(c1)^ord(c2)).count('1')
      total_distance += hamming_distance

  print('- 2 <low> (u.d.): {}'.format(total_distance/(26*26)))

  average_hamming_distance = 0
  for i in range(8):
    p = 0
    for c in ascii_lowercase:
      if ((ord(c) >> i) & 1):
        p += 1/26
    average_hamming_distance += 2*p*(1-p)

  print('alternate method: {}'.format(average_hamming_distance))

  total_distance = 0
  for c1 in ascii_lowercase:
    for c2 in ascii_lowercase:
      for c3 in ascii_lowercase:
        for c4 in ascii_lowercase:
          hamming_distance = bin(ord(c1)^ord(c2)^ord(c3)^ord(c4)).count('1')
          total_distance += hamming_distance

  print('- 4 <low> (u.d.): {}'.format(total_distance/(26*26*26*26)))

  average_hamming_distance = 0
  for i in range(8):
    p = 0
    for c in ascii_lowercase:
      if ((ord(c) >> i) & 1):
        p += 1/26
    average_hamming_distance += 4*(p*(1-p)**3+p**3*(1-p))

  print('alternate method: {}'.format(average_hamming_distance))

  pool = [c for c in ascii_lowercase]

  letters_freq = english_letters_freq
  norm_letters_freq = [f/sum(letters_freq) for f in letters_freq] # for numpy.random.choice to work...

  total_distance = 0
  for i in range(count):
    c1 = numpy.random.choice(pool, p=norm_letters_freq)
    c2 = numpy.random.choice(pool, p=norm_letters_freq)
    XORed = ord(c1) ^ ord(c2)
    hamming_distance = bin(XORed).count('1')
    total_distance += hamming_distance

  print('- 2 <low> (e.l.d.): {}'.format(total_distance/count))

  total_distance = 0
  for i in range(count):
    c1 = numpy.random.choice(pool)
    c2 = numpy.random.choice(pool)
    c3 = numpy.random.choice(pool, p=norm_letters_freq)
    c4 = numpy.random.choice(pool, p=norm_letters_freq)
    XORed = ord(c1) ^ ord(c2) ^ ord(c3) ^ ord(c4)
    hamming_distance = bin(XORed).count('1')
    total_distance += hamming_distance

  print('- 2 <low> (e.l.d.), 2 <low> (u.d.): {}'.format(total_distance/count))

  total_distance = 0
  for i in range(count):
    c1 = numpy.random.choice(pool, p=norm_letters_freq)
    c2 = numpy.random.choice(pool, p=norm_letters_freq)
    c3 = numpy.random.choice(pool, p=norm_letters_freq)
    c4 = numpy.random.choice(pool, p=norm_letters_freq)
    XORed = ord(c1) ^ ord(c2) ^ ord(c3) ^ ord(c4)
    hamming_distance = bin(XORed).count('1')
    total_distance += hamming_distance

  print('- 4 <low> (e.l.d.): {}'.format(total_distance/count))

  pool_space = list(pool)
  pool_space.append(' ')

  letters_space_freq = list(letters_freq)
  letters_space_freq.append(0.24) # a bit above 19% after norm
  norm_letters_space_freq = [f/sum(letters_space_freq) for f in letters_space_freq]

  total_distance = 0
  for i in range(count):
    c1 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    c2 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    XORed = ord(c1) ^ ord(c2)
    hamming_distance = bin(XORed).count('1')
    total_distance += hamming_distance

  print('- 2 <low|space> (e.l.d.): {}'.format(total_distance/count))
  
  total_distance = 0
  for i in range(count):
    c1 = numpy.random.choice(pool)
    c2 = numpy.random.choice(pool)
    c3 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    c4 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    XORed = ord(c1) ^ ord(c2) ^ ord(c3) ^ ord(c4)
    hamming_distance = bin(XORed).count('1')
    total_distance += hamming_distance

  print('- 2 <low|space> (e.l.d.), 2 <low> (u.d.): {}'.format(total_distance/count))

  total_distance = 0
  for i in range(count):
    c1 = numpy.random.choice(pool, p=norm_letters_freq)
    c2 = numpy.random.choice(pool, p=norm_letters_freq)
    c3 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    c4 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    XORed = ord(c1) ^ ord(c2) ^ ord(c3) ^ ord(c4)
    hamming_distance = bin(XORed).count('1')
    total_distance += hamming_distance

  print('- 2 <low|space> (e.l.d.), 2 <low> (e.l.d.): {}'.format(total_distance/count))

  total_distance = 0
  for i in range(count):
    c1 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    c2 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    c3 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    c4 = numpy.random.choice(pool_space, p=norm_letters_space_freq)
    XORed = ord(c1) ^ ord(c2) ^ ord(c3) ^ ord(c4)
    hamming_distance = bin(XORed).count('1')
    total_distance += hamming_distance

  print('- 4 <low|space> (e.l.d.): {}'.format(total_distance/count))

if __name__ == '__main__':
  main()
