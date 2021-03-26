'''
in
    2
    3 3
    1 2
    2 3
    1 3
    5 4
    2 1
    2 3
    4 3
    4 5
out
    2
    4
'''
from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    ck[x] = 1
    cnt = 0
    while q:
        x = q.popleft()
        for nx in a[x]:
            if ck[nx] == 0:
                ck[nx] = 1
                cnt += 1
                q.append(nx)
    return cnt

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [[] for _ in range(n)]
    ck = [0 for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        a[x-1].append(y-1)
        a[y-1].append(x-1)
        
    res = 0
    for i in range(n):
        if ck[i] == 0:
            res += bfs(i)
    print(res)