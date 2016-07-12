""""
Implement the mapper to the problem of finding the shortest path using Hadoop Streaming.

Input and output data: as the key is the top of the number, the value is composed of two fields, separated by tabs:

The minimum distance from a given vertex (if it does not, it is written INF)
List of outgoing vertices (via "," in curly brackets)

Example mapper work on the second iteration of the processing of the following graph:
https://ucarecdn.com/135a6f6d-4785-4cb8-8686-2f25d21ef463

Sample Input:
1	0	{2,3,4}
2	1	{5,6}
3	1	{}
4	1	{7,8}
5	INF	{9,10}
6	INF	{}
7	INF	{}
8	INF	{}
9	INF	{}
10	INF	{}

Sample Output:
1	0	{2,3,4}
2	1	{}
3	1	{}
4	1	{}
2	1	{5,6}
5	2	{}
6	2	{}
3	1	{}
4	1	{7,8}
7	2	{}
8	2	{}
5	INF	{9,10}
9	INF	{}
10	INF	{}
6	INF	{}
7	INF	{}
8	INF	{}
9	INF	{}
10	INF	{}
""""

import sys

for line in sys.stdin:
    words = line.strip().split()
    num = words[0]
    dist = words[1]
    verts = (words[2][1:-1]).split(',')
    print('{}\t{}\t{}'.format(num, dist, words[2]))
    
    dist = 'INF' if dist == 'INF' else int(dist) + 1
    
    for v in verts:
        if v != '':
            print('{}\t{}\t{{}}'.format(v, dist))
            