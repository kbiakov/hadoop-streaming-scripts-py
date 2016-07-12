""""
Implement a mapper for Cross-Correlation tasks that each object from the tuple creates a stripe.

Mapper takes a tuple - row consisting of objects, separated by a space.

Mapper writes data in the form of key / value, where key - object, value - corresponding stripe (example: a: 1, b: 2, c: 3)

Sample Input:
a b
a b a c

Sample Output:
a	b:1
b	a:1
a	b:1,c:1
b	a:2,c:1
a	b:1,c:1
c	b:1,a:2
""""

import sys

def dict_to_string(d, exc_key):
    res = ""
    for k, v in d.items():
        if k != exc_key:
            if res != "":
                res += ","
            res += "{}:{}".format(k, v)
    return res

for line in sys.stdin:
    items = line.strip().split()
    for i in items:
        h = {}
        for j in items:
            h[j] = h.get(j, 0) + 1
        print("{}\t{}".format(i, dict_to_string(h, i)))
        