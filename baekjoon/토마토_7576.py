# 백준 7526 - 토마토
from collections import deque

# m,n,g = 6, 4,[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 1]] # 8
# m,n,g = 6, 4,[[1, -1, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, -1, 1]] # 6
# m,n,g = 6, 4,[[0, -1, 0, 0, 0, 0], [-1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]] # -1
# m,n,g = 2, 2,[[1, -1],[-1, 1]] # 0
m,n,g = 5, 5, [[-1, 1, 0, 0, 0], [0, -1, -1, -1, 0], [0, -1, -1, -1, 0], [0, -1, -1, -1, 0], [0, 0, 0, 0, 0]] # 14

# m,n = map(int, input().split())
# g = [list(map(int, input().split())) for _ in range(n)]
# print(m,n,g)
q = deque()
dx, dy = [1,0,-1,0], [0,1,0,-1]
res = 0

def bfs(q, res):
    cnt = res

    while q:
        a, b, cnt = q.popleft()

        for i,j in zip(dx, dy):
            nx, ny = a+i, b+j

            if 0<=nx<n and 0<=ny<m and g[nx][ny] == 0:
                g[nx][ny] = 1
                q.append([nx,ny, cnt + 1])
    
    for i in range(n):
        if 0 in g[i]:
            return -1
    return cnt

for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            q.append((i, j, res))

print(bfs(q, res))