'''
    최근 하던 방식대로 함수로 풀려고 했는데,
    상황에 따라 다르게 해야겠다.
    pypy3로 제출해야 시간초과 안남
in
    5 3 2
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    0 0 1 0 0
    0 0 0 0 0
out
    4
in
    4 3 2
    1 1 1 1
    1 1 1 1
    1 1 1 1
    1 1 1 1
    -1 -1 -1 -1
    1 1 1 -1
out
    0
'''

from collections import deque

m, n, h = map(int, input().split())
tomato = []
q = deque()
res = -2
dx, dy, dz = [1,0,-1,0,0,0], [0,1,0,-1,0,0], [0,0,0,0,-1,1] # dz = 위아래 검사

for i in range(h):
    temp = []

    for j in range(n):
        temp.append(list(map(int, input().split())))

        for k in range(m):
            if temp[j][k] == 1:
                q.append([i, j, k])    
    tomato.append(temp)

while q:
    a, b, c = q.popleft()

    for x, y, z in zip(dx, dy, dz):
        nx, ny, nz = a + x, b + y, c + z

        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomato[nx][ny][nz] == 0:
            q.append([nx, ny, nz])
            tomato[nx][ny][nz] = tomato[a][b][c] + 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            res = max(res, tomato[i][j][k])

print(res - 1)

