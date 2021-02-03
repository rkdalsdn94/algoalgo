from collections import deque
# n, m = map(int, input().split())
# g = [list(map(int, input().split())) for _ in range(n)]
n, m, g = 6, 5, [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]] # -> 4, 9
# print(n,m,g)

def bfs(i,j):
    q = deque()
    q.append([i,j])
    ck[i][j] = 1
    cnt = 1

    while q:
        a, b = q.popleft()
        
        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and g[nx][ny] == 1:
                q.append([nx, ny])
                g[nx][ny] = g[a][b] + 1
                cnt += 1
                ck[nx][ny] = 1
    res.append(cnt)

dx, dy = [1,0,-1,0], [0,1,0,-1]
res = []
ck = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            bfs(i, j)
if res:
    print(len(res))
    print(max(res))
else:
    print(0)
    print(0)    
