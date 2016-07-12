""""
Implement reducer for PageRank calculation algorithm using Hadoop Streaming. Use the simplified algorithm (without random transitions).

Inputs and Outputs: The number is the top of a key. The value of the compound: in tab write the value of PageRank (rounded to the third decimal place) and a list of adjacent vertices (via "," in curly brackets).

Example reducer operation for a graph is taken from lecture (the number of vertices are given without n):
https://ucarecdn.com/88aa9d54-f2e8-4010-b255-9107b4290e84

Sample Input:
1	0.067	{}
1	0.200	{2,4}
2	0.067	{}
2	0.100	{}
2	0.200	{3,5}
3	0.067	{}
3	0.100	{}
3	0.200	{4}
4	0.100	{}
4	0.200	{}
4	0.200	{5}
5	0.100	{}
5	0.200	{}
5	0.200	{1,2,3}

Sample Output:
1	0.067	{2,4}
2	0.167	{3,5}
3	0.167	{4}
4	0.300	{5}
5	0.300	{1,2,3}
""""

import sys

def add_nulls(num, size):
    num_s = str(num)
    num_len = len(num_s)
    if num_len < size:
        for i in range(size - num_len):
            num_s += '0'
    return num_s

v = M = ''
pr = pr_cur = pr_sum = 0
verts = vs = '{{}}'

for line in sys.stdin:
    words = line.strip().split()
    v = words[0]
    pr = float(words[1])
    verts = words[2]
    
    if M == v:
        if len(verts) > len(vs):
            vs = verts
        else:
            pr_sum += pr
    else:
        if M != '':
            print('{}\t{}\t{}'.format(M, add_nulls(round(pr_cur + pr_sum, 3), 5), vs))
        
        pr_sum = 0
        pr_cur = 0 if len(verts) > len('{}') else pr
        vs = verts
        M = v
        
print('{}\t{}\t{}'.format(M, add_nulls(round(pr_cur + pr_sum, 3), 5), vs))
