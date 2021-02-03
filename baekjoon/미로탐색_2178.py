# 백준 2178 - 미로탐색
from collections import deque

# n,m,g = 4, 6, [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]] # 15
# n,m,g = 4, 6, [[1,1,0,1,1,0], [1,1,0,1,1,0], [1,1,1,1,1,1], [1,1,1,1,0,1]] # 9
# n,m = 2, 25
# g = [[1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1], [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1]] # 38
# n,m = 7, 7
# g = [[1,0,1,1,1,1,1],[1,1,1,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]] # 13

n, m = map(int,input().split())
g = [list(map(int,input())) for _ in range(n)]
# print(n,m,g)
dx, dy = [1,0,-1,0], [0,1,0,-1]
ck = [[False] * m for _ in range(n)]
def bfs(x, y):
    q = deque()
    q.append([x,y])
    ck[x][y] = True
    while q:
        a, b = q.popleft()
        for i, j in zip(dx, dy):
            nx, ny = a+i, b+j
            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == False and g[nx][ny] == 1:
                g[nx][ny] = g[a][b] + 1
                ck[nx][ny] = True
                q.append([nx,ny])

bfs(0, 0)
print(g[n-1][m-1])