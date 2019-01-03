# Detecting the key length with Hamming distance

## Theory

Hamming distance between 2 binary words of equal length **X** and **Y** can be written as

![](https://latex.codecogs.com/gif.latex?wt(X&space;\oplus&space;Y))

where ![](https://latex.codecogs.com/gif.latex?wt) (weight) is the number of bits set to 1, and ![](https://latex.codecogs.com/gif.latex?\oplus) is the XOR operator.

Let's call the key **K**.

If you cut your ciphertext into chunks of len(**K**) bytes (except the last), then any chunk **C** can actually be written as ![](https://latex.codecogs.com/gif.latex?C&space;=&space;P&space;\oplus&space;K) where **P** is the corresponding plaintext, and the Hamming distance between 2 chunks is therefore:

![](https://latex.codecogs.com/gif.latex?wt(C1\oplus&space;C2)&space;=)  
![](https://latex.codecogs.com/gif.latex?wt((P1\oplus&space;K)\oplus(P2\oplus&space;K))&space;=)  
![](https://latex.codecogs.com/gif.latex?wt(P1\oplus&space;K\oplus&space;P2\oplus&space;K)&space;=)  
![](https://latex.codecogs.com/gif.latex?wt(P1\oplus&space;P2\oplus&space;K\oplus&space;K)&space;=)  
![](https://latex.codecogs.com/gif.latex?wt(P1\oplus&space;P2))

i.e. the Hamming distance between the corresponding chunks of plaintext.

If you cut your ciphertext into chunks of n != len(**K**) bytes, then the Hamming distance between 2 chunks is:

![](https://latex.codecogs.com/gif.latex?wt(C1\oplus&space;C2)&space;=&space;wt(P1\oplus&space;K1\oplus&space;P2\oplus&space;K2))

where **K1** and **K2** are some substrings of the repeating-key, and have no reason to be similar a priori (unless of course if n is a multiple of len(**K**)).

Cool.

But is there any reason why ![](https://latex.codecogs.com/gif.latex?wt(P1\oplus&space;P2)) would be smaller than ![](https://latex.codecogs.com/gif.latex?wt(P1\oplus&space;K1\oplus&space;P2\oplus&space;K2)) ?

Let's assume that the plaintext (resp. the key)'s characters have been generated with an alphabet **A** (resp. **A'**) and a probability distribution for this alphabet **D<sub>A</sub>** (resp. **D<sub>A'</sub>**) (e.g. lower case letters and [english letter distribution](https://en.wikipedia.org/wiki/Letter_frequency#Relative_frequencies_of_letters_in_the_English_language)).

This allows us to write the **expected normalized Hamming distance** as:  
![](https://latex.codecogs.com/gif.latex?H_R=E[wt(X_{1}\oplus&space;X_{2})]) if the key length is correctly guessed  
![](https://latex.codecogs.com/gif.latex?H_W=E[wt(X_{1}\oplus&space;X_{2}\oplus&space;X'_{1}\oplus&space;X'_{2})]) otherwise  
where **X<sub>i</sub>** (resp. **X'<sub>i</sub>**) are independent random variables with distribution **D<sub>A</sub>** (resp. **D'<sub>A</sub>**).

Now, let's zoom in on bits.

**Fact 1:**  
The probability p<sub>k</sub> that the k<sup>th</sup> bit b<sub>i,k</sub> of random variable **X<sub>i</sub>** is set to 1 is the probability of drawing a character from **D<sub>A</sub>** whose k<sup>th</sup> bit is 1, so the sum of the probability of all such characters.  
(e.g. letters [q-z] have the 5th bit set to 1, so p<sub>5</sub> is 10/26 for a uniform distribution).

**Fact 2:**  
The XOR of n bits will have value 1 if bit 1 appears an odd number of times, and value 0 otherwise.

From these 2 facts, we can compute the **expected Hamming distance for the k<sup>th</sup> bit**:

- when we XOR **X<sub>1</sub>** and **X<sub>2</sub>**:

![](https://latex.codecogs.com/gif.latex?h_{R,k}=h_{2,k}&space;=)  
![](https://latex.codecogs.com/gif.latex?E[wt(b_{1,k}\oplus&space;b_{2,k})]&space;=)  
![](https://latex.codecogs.com/gif.latex?E[b_{1,k}\oplus&space;b_{2,k}]&space;=)  
![](https://latex.codecogs.com/gif.latex?p(1.bit.set)&space;=)  
![](https://latex.codecogs.com/gif.latex?2p_k(1-p_k))

(and similarly)

![](https://latex.codecogs.com/gif.latex?h'_{2,k}&space;=)  
![](https://latex.codecogs.com/gif.latex?E[b'_{1,k}\oplus&space;b'_{2,k}]&space;=)  
![](https://latex.codecogs.com/gif.latex?2p'_k(1-p'_k))

- when we XOR **X<sub>1</sub>**, **X<sub>2</sub>**, **X'<sub>1</sub>** and **X'<sub>2</sub>**, noticing that to have an odd number of 1, you must have (an odd number of 1 in the first 2 bits AND an even number in the last 2) OR (an even number in the first 2 AND an odd number in the last 2):

![](https://latex.codecogs.com/gif.latex?h_{W,k}&space;=)  
![](https://latex.codecogs.com/gif.latex?E[b_{1,k}\oplus&space;b_{2,k}\oplus&space;b'_{1,k}\oplus&space;b'_{2,k}]&space;=)  
![](https://latex.codecogs.com/gif.latex?h_{2,k}(1-h'_{2,k})&plus;h'_{2,k}(1-h_{2,k})&space;=)  
![](https://latex.codecogs.com/gif.latex?h_{2,k}&plus;h'_{2,k}(1-2h_{2,k}))

If you plot [h<sub>2,k</sub>](http://fooplot.com/#W3sidHlwZSI6MCwiZXEiOiIyKngqKDEteCkiLCJjb2xvciI6IiMwMDAwMDAifSx7InR5cGUiOjEwMDAsIndpbmRvdyI6WyIwIiwiMSIsIjAiLCIwLjYiXX1d), you can see that it does not exceed 0.5, so (1 - 2h<sub>2,k</sub>) is positive, and thus **h<sub>W,k</sub> >= h<sub>R,k</sub>**.

Since the expected normalized Hamming distance H<sub>R</sub> (resp. H<sub>W</sub>) is just the sum of the expected distances h<sub>R,k</sub> (resp. h<sub>W,k</sub>) for each bit, we have proven why it is lower when the key length is guessed correctly.

***Note 1.** You can now compute the expected Hamming distance when key length is correctly guessed or not for any (**A**, **D<sub>A</sub>**) and (**A'**, **D<sub>A'</sub>**).*

***Note 2.** h<sub>W,k</sub> cannot exceed 0.5, so if h<sub>R,k</sub> is close to 0.5 for all bits, key length detection won't work well. And the good thing is that "h<sub>R,k</sub> is close to 0.5 for all bits" does NOT mean there is no statistical information in the text. For a given (**A**, **D<sub>A</sub>**), you can maybe devise a set of distinct bytes for each charcater that maximizes h<sub>R,k</sub>.* **TODIG**

## Experimentation

I went ahead and computed the average Hamming distance, when key length is correctly guessed or not, for several models (Monte Carlo style, except for the first 2 models where I also used the method above).

Corresponding script is:  
```./hamming_distance_stats.py count```  
where 'count' is the number of sampled Hamming distances for each model.  
(you can use 100000 for a reasonable approximation)

### Nomenclature:

**R** = "Right key length", **W** = "Wrong"  
{low} = lower case character  
u.d. = "uniformly distributed"  
e.l.d. = "english letter frequency distribution"  

### Results:

**Random text, random key**  
Average Hamming distance of  
**R** :  2 {low} (u.d.): **2.473 bits**  
**W**: 4 {low} (u.d.): **2.499 bits**  
=> **0.03 bits** *(basic example of hard to detect)*

**Text in english, random key**:  
**R** : 2 {low} (e.l.d.): **~2.36 bits**  
**W**: 2 {low} (e.l.d.), 2 {low} (u.d.): **~2.50 bits**  
=> **0.14 bits**

**Text in english, key in english** (provided key is big enough to have statistical info):  
**R** : 2 {low} (e.l.d.): **~2.36 bits**  
**W**: 4 {low} (e.l.d.): **~2.49 bits**  
=> **0.13 bits** *(=> no use in making a gibberish key you won't remember)*

**Text in english with spaces, random key**:  
**R** : 2 {low|space} (e.l.d.): **~2.54 bits**  
**W**: 2 {low|space} (e.l.d.), 2 {low} (u.d.): **~2.81 bits**  
=> **0.27 bits** *(=> spaces improve readability for the receiver but also for the attacker)*

**Text in english with spaces, key in english**:  
**R** : 2 {low|space} (e.l.d.): **~2.54 bits**  
**W**: 2 {low|space} (e.l.d.), 2 {low} (e.l.d.): **~2.79 bits**  
=> **0.25 bits** *(still no use making a gibberish key)*

**Text in english with spaces, key in english with spaces**:  
**R** : 2 {low|space} (e.l.d.): **~2.54 bits**  
**W**: 4 {low|space} (e.l.d.): **~2.88 bits**  
=> **0.34 bits** *(yup, spaces)*

Feel free to test more models if you're curious.
