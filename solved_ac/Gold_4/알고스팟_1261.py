'''
in
    6 6
    001111
    010000
    001111
    110001
    011010
    100010
out
    2
'''
from collections import deque
from sys import stdin
input = stdin.readline

m, n = map(int, input().split())
g = [ list(map(int, input().strip())) for _ in range(n) ]
ck = [[0] * m for _ in range(n) ]
q = deque([(0,0)])
dx, dy = [1,0,-1,0], [0,1,0,-1]


while q:
    a, b = q.popleft()
    ck[a][b] = 1

    for i, j in zip(dx, dy):
        nx, ny = a + i, b + j

        if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0:
            if g[nx][ny] == 0:
                q.appendleft((nx, ny))
                ck[nx][ny] = 1
                g[nx][ny] = g[a][b]
            else:
                g[nx][ny] = g[a][b] + 1
                q.append((nx, ny))
                ck[nx][ny] = 1
print(g[-1][-1])
