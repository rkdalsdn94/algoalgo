from collections import deque
'''
n, m, v = 4 5 1
g 정보
    1 2
    1 3
    1 4
    2 4
    3 4
result = 1 2 4 3 (DFS) ,  1 2 3 4 (BFS)
'''
def dfs(v):
    print(v, end=' ')
    ck[v] = 1
    for i in range(1, n+1):
        if ck[i] == 0 and g[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque([v])
    ck[v] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if ck[i] == 0 and g[v][i] == 1:
                q.append(i)
                ck[i] = 1

n, m, v = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = g[b][a] = 1
# print(g)

ck = [0] * (n+1)
dfs(v)
print()
ck = [0] * (n+1)
bfs(v)