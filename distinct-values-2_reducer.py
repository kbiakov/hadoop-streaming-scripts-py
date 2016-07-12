""""
Implement a reducer of tasks Distinct Values v2.

Reducer accepts input lines, each of which consists of a tab-delimited values, and the group name.

Sample Input:
1	a
1	b
1	b
2	a
2	d
2	e
3	a
3	b

Sample Output:
a	3
d	1
b	2
e	1
""""

import sys

uni_cats = set()
h = {}

for line in sys.stdin:
    uni_cats.add(line)

for c in uni_cats:
    words = c.strip().split()
    val = words[0]
    cat = words[1]
    h[cat] = h.get(cat, 0) + 1
    
for cat, count in h.items():
    print('{}\t{}'.format(cat, count))
    