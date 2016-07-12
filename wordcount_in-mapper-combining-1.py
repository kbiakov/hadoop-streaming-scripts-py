""""
Write a program that implements the In-mapper combining v.1 for WordCount problem in Hadoop Streaming.

Sample Input:
aut Caesar aut nihil
aut aut
de mortuis aut bene aut nihil

Sample Output:
nihil	1
aut	2
Caesar	1
aut	2
nihil	1
aut	2
de	1
bene	1
mortuis	1
""""

import sys

for line in sys.stdin:
    h = {}
    words = line.strip().split()
    for word in words:
        h[word] = h.get(word, 0) + 1
    for word, count in h.items():
        print('{}\t{}'.format(word, count))
        