# Set 1: Basics
__Challenge 1:__

./convert.py hex 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d b64

__Challenge 2:__

./repeating\_key\_XOR.py hex 1c0111001f010100061a024b53535009181c hex 686974207468652062756c6c277320657965

__Challenge 3:__

./break\_single\_byte\_XOR\_cipher.py 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

__Challenge 4:__

./detect\_single\_byte\_XOR\_cipher.py 4.txt

__Challenge 5:__

./repeating\_key\_XOR.py str "$(cat 5.txt)" str "ICE" hex

__Challenge 6:__

./break\_repeating\_key\_XOR\_cipher.py "$(./convert.py b64 $(cat 6.txt | tr -d '\n') hex)" -k 42 -v

See Bonus for some insight.

__Challenge 7:__

openssl enc -d -aes-128-ecb -K $(./convert.py str "YELLOW SUBMARINE" hex) -a -in 7.txt  
(add -A if the base64 string is on a single line)

TODO: Python version

__Challenge 8:__

TODO

