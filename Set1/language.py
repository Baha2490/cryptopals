#!/usr/bin/python3

english_letters_freq = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, # A-G
                        0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, # H-N
                        0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, # O-U
                        0.00978, 0.02360, 0.00150, 0.01974, 0.00074];                  # V-Z

def english_letter_freq_score(msg):
  count_letters = [0] * 26
  total_nb_letters = 0

  for b in msg:
    if (b >= 65) and (b <= 90):
      count_letters[b - 65] += 1
      total_nb_letters += 1
    elif (b >= 97) and (b <= 122):
      count_letters[b - 97] += 1
      total_nb_letters += 1

  score = 0
  for l in range(26):
    count = count_letters[l]
    expected_count = english_letters_freq[l] * total_nb_letters
    difference = count - expected_count

    score += (difference * difference / expected_count) 

  return score

# basic version, just count the ratio of alphabetic or space characters
def english_score(msg):
  score = 0
  for b in msg:
    if (b == 32) or ((b >= 65) and (b <= 90)) or ((b >= 97) and (b <= 122)):
      score += 1
  score /= len(msg)
  return score

