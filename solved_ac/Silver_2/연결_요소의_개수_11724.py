'''
in
    6 5
    1 2
    2 5
    5 1
    3 4
    4 6
out
    2
'''

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
q = deque()
ck = [0] * (n + 1)
g = [[] for _ in range(n+1)]
res = 0

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(q):
    while q:
        x = q.popleft()
        for i in g[x]:
            if ck[i] == 0:
                q.append(i)
                ck[i] = 1

for i in range(1, n+1):
    if ck[i] == 0:
        q.append(i)
        bfs(q)
        res += 1

print(res)
    
