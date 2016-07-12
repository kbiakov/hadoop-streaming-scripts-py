""""
Implement an Dijkstra's algorithm for searching shortest path in the graph.

Input: the number of vertices and the number of edges: two numbers in the first line. Next come the line with the description of the ribs. Their number is equal to the number of edges. Each line contains 3 numbers: the top of the outgoing, incoming vertex weight of the edge. The last line contains two vertex numbers: start and end vertex, the shortest path between them must be found.

Output: The minimum distance between the given vertices. If there is no way, then you need to return -1.

Example: https://ucarecdn.com/56a66a36-361d-4b6b-836f-9a18e751eddd

Sample Input:
4 8
1 2 6
1 3 2
1 4 10
2 4 4
3 1 5
3 2 3
3 4 8
4 2 1
1 4

Sample Output:
9
""""

from collections import defaultdict
from heapq import heapify, heappush, heappop
import sys

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for v,p,c in edges:
        g[v].append((c,p))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
            	return cost
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))
    return -1

i = 0
lines = {}
for line in sys.stdin:
    lines[i] = line.strip().split()
    i = i + 1

count_v = 0
count_e = 0
v_beg = 0
v_end = 0
edges = []
for k, words in lines.items():
	if k == 0:
		count_v = int(words[0])
		count_e = int(words[1])
	elif k == len(lines) - 1:
		v_beg = words[0]
		v_end = words[1]
	else:
		v = words[0]
		path = words[1]
		cost = int(words[2])
		edges.append((v, path, cost))

vs = set()
for v,p,c in edges:
    vs.add(int(v))
    vs.add(int(p))
        
if len(edges) == 0 or len(edges) != count_e or len(vs) != count_v:
    print(-1)
elif len(edges) == 1:
	l,r,c = edges[0]
	print(c)
else:
	print(dijkstra(edges, v_beg, v_end))
