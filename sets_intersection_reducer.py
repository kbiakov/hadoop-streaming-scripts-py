""""
Write reducer, which makes crossing the elements of the sets A and B. At the entrance to the reducer come pairs key / value, where key - element of the set, value - sets the marker (A or B)

Sample Input:
1	A
2	A
2	B
3	B

Sample Output:
2
""""

import sys

pairs = {}

for line in sys.stdin:
    words = line.strip().split()
    k = words[0]
    v = words[1]
    pairs[k] = pairs.get(k, 0) + 1
    
    if pairs.get(k, 0) == 2:
        print(k)
