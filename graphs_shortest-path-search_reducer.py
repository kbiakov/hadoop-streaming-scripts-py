""""
Implement reducer in the problem of finding the shortest path using Hadoop Streaming.

Input and output data: as the key is the top of the number, the value is composed of two fields, separated by tabs:

The minimum distance from a given vertex (if it does not, it is written INF)
List of outgoing vertices (via "," in curly brackets).

Example reducer works on the second iteration of the processing of the following graph:
https://ucarecdn.com/4374b2bd-3993-4b61-a0f3-69d19170e871

Sample Input:
1	0	{2,3,4}
10	INF	{}
10	INF	{}
2	1	{}
2	1	{5,6}
3	1	{}
3	1	{}
4	1	{}
4	1	{7,8}
5	2	{}
5	INF	{9,10}
6	2	{}
6	INF	{}
7	2	{}
7	INF	{}
8	2	{}
8	INF	{}
9	INF	{}
9	INF	{}

Sample Output:
1	0	{2,3,4}
10	INF	{}
2	1	{5,6}
3	1	{}
4	1	{7,8}
5	2	{9,10}
6	2	{}
7	2	{}
8	2	{}
9	INF	{}
""""

import sys

dist_min = 'INF'
vs = '{{}}'
M = ''

num = ''
dist = 'INF'
verts = '{{}}'

for line in sys.stdin:
    words = line.strip().split()
    num = words[0]
    dist = words[1]
    verts = words[2]
    
    dist = 'INF' if dist == 'INF' else int(dist)
    
    if M == num:
        if len(verts) > len(vs):
            vs = verts
        elif dist != 'INF' and dist_min != 'INF' and dist < dist_min:
            dist_min = dist
    else:
        if M != '':
            print('{}\t{}\t{}'.format(M, dist_min, vs))
        dist_min = dist
        vs = verts
        M = num

if M == num:
    if dist != 'INF' and dist_min != 'INF' and dist < dist_min:
        if len(verts) > len(vs):
            vs = verts
        dist_min = dist
    print('{}\t{}\t{}'.format(M, dist_min, vs))
else:
    print('{}\t{}\t{}'.format(num, dists, verts))
