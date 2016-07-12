""""
Write reducer, which makes the subtraction of the elements of B of A. At the entrance to the reducer come pairs key / value, where key - element of the set, value - sets the marker (A or B)

Sample Input:
1	A
2	A
2	B
3	B

Sample Output:
1
""""

import sys

pairs = {}

for line in sys.stdin:
    words = line.strip().split()
    num = words[0]
    s = words[1]
    
    sets = pairs.get(num, [])
    sets.append(s)
    pairs[num] = sets

vals = []
    
for num, sets in pairs.items():
    if len(sets) == 1 and sets[0] == 'A':
        vals += num
        
for num in sorted(vals):
	print(num)
