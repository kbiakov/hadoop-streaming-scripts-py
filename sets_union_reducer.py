""""
Write reducer, which combines elements of the sets A and B. At the entrance to the reducer come pairs key / value, where key - element of the set, value - sets the marker (A or B)

Sample Input:
1	A
2	A
2	B
3	B

Sample Output:
1
2
3
""""

import sys

keys = []

for line in sys.stdin:
    words = line.strip().split()
    k = words[0]
    v = words[1]
    
    if keys.count(k) == 0:
        keys.append(k)
    
for k in keys:
    print(k)
