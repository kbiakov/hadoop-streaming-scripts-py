""""
Implement a mapper for calculating the PageRank algorithm using Hadoop Streaming.

Inputs and Outputs: The number is the top of a key. The value of the compound: in tab write the value of PageRank (rounded to the third decimal place) and a list of adjacent vertices (via "," in curly brackets).

An example of the mapper is taken for a graph from lecture (the number of vertices are given without n):
https://ucarecdn.com/88aa9d54-f2e8-4010-b255-9107b4290e84

Sample Input:
1	0.200	{2,4}
2	0.200	{3,5}
3	0.200	{4}
4	0.200	{5}
5	0.200	{1,2,3}

Sample Output:
1	0.200	{2,4}
2	0.100	{}
4	0.100	{}
2	0.200	{3,5}
3	0.100	{}
5	0.100	{}
3	0.200	{4}
4	0.200	{}
4	0.200	{5}
5	0.200	{}
5	0.200	{1,2,3}
1	0.067	{}
2	0.067	{}
3	0.067	{}
""""

import sys

def add_nulls(num, size):
    num_s = str(num)
    num_len = len(num_s)
    if num_len < size:
        for i in range(size - num_len):
            num_s += '0'
    return num_s

for line in sys.stdin:
    words = line.strip().split()
    v = words[0]
    pr = words[1]
    verts = words[2]
    print('{}\t{}\t{}'.format(v, pr, verts))
    verts = (verts[1:-1]).split(',')
    
    for adj_v in verts:
        prob = round(float(pr) / len(verts), 3)
        prob_s = add_nulls(prob, 5)
        print('{}\t{}\t{{}}'.format(adj_v, prob_s))
        