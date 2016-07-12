""""
Write a program that implements the In-mapper combining v.2 for WordCount problem in Hadoop Streaming.

Sample Input:
aut Caesar aut nihil
aut aut
de mortuis aut bene aut nihil

Sample Output:
aut	6
mortuis	1
bene	1
Caesar	1
de	1
nihil	2

""""

import sys

h = {}

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        h[word] = h.get(word, 0) + 1

for word, count in h.items():
    print('{}\t{}'.format(word, count))
