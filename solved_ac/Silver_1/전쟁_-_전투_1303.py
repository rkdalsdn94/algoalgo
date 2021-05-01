from sys import stdin
from collections import deque

input = stdin.readline
n, m = map(int, input().split())
dx, dy = [1,0,-1,0], [0,1,0,-1]
ck = [[0] * n for _ in range(m)]
res = [0, 0]
g = [ list(input().strip()) for _ in range(m) ]

# print(g)

def bfs(x, y, word):
    q = deque([(x, y)])
    num = 1

    while q:
        a, b = q.popleft()
        ck[a][b] = 1
        
        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < m and 0 <= ny < n and ck[nx][ny] == 0 and g[nx][ny] == word:
                q.append((nx, ny))
                ck[nx][ny] = 1
                num += 1
    return num

for i in range(m):
    for j in range(n):
        if ck[i][j] == 0:
            if g[i][j] == 'W':
                res[0] += bfs(i, j, 'W') ** 2
            else:
                res[1] += bfs(i, j, 'B') ** 2

print(*res)