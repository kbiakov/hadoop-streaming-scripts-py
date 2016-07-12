""""
Modify reducer of the previous job so that it rascchityval PageRank based random transition, ie the first term in the formula:
PR (x) = alpha * (1 / N) + (1 - alpha) * sum (1..n, PR (ti) / C (ti))

For all tests, assume that N = 5, α = 0,1.

Inputs and Outputs: The number is the top of a key. The value of the compound: in tab write the value of PageRank (rounded to the third decimal place) and a list of adjacent vertices (via "," in curly brackets).

Example reducer operation for a graph is shown of lectures (the number of vertices are given without n):
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
1	0.080	{2,4}
2	0.170	{3,5}
3	0.170	{4}
4	0.290	{5}
5	0.290	{1,2,3}
""""

import sys

def add_nulls(num, size):
    num_s = str(num)
    num_len = len(num_s)
    if num_len < size:
        for i in range(size - num_len):
            num_s += '0'
    return num_s

lines = []
for line in sys.stdin:
    words = line.strip().split()
    v = words[0]
    pr = float(words[1])
    verts = words[2]
    lines.append((v, pr, verts))
    
prs = {}
for v,pr,verts in lines:
    verts = verts[1:-1].split(',')
    for vert in verts:
        prs[vert] = prs.get(vert, 0) + pr / len(verts)
    
v = M = ''
pr = pr_cur = pr_sum = 0
verts = vs = '{{}}'

for v,pr,verts in lines:    
    if M == v:
        if len(verts) > len(vs):
            vs = verts
        else:
            pr_sum += pr
    else:
        if M != '':
            prr = 0.1 / 5 + 0.9 * prs.get(M, 0)
            print('{}\t{}\t{}'.format(M, add_nulls(round(prr, 3), 5), vs))
        
        pr_sum = 0
        pr_cur = 0 if len(verts) > len('{}') else pr
        vs = verts
        M = v
        
prr = 0.1 / 5 + 0.9 * prs.get(M, 0)
print('{}\t{}\t{}'.format(M, add_nulls(round(prr, 3), 5), vs))
