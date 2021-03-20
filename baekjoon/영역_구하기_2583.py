from collections import deque
m, n, k = 5, 7, 3
rectangle = [[0, 2, 4, 4], [1, 1, 2, 5], [4, 0, 6, 2]]
# m, n, k = map(int, input().split())
# rectangle = [ list(map(int, input().split())) for _ in range(k) ]
ck = [[0] * n for _ in range(m)]

dx, dy = (1,0,-1,0), (0,1,0,-1)
q = deque()
res = []

for i in rectangle:
    x1, y1, x2, y2 = i
    for j in range(y1, y2):
        for z in range(x1, x2):
            ck[j][z] = 1
# print(ck)

def bfs(q):
    cnt = 1
    while q:
        a, b = q.popleft()
        ck[a][b] = 1

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < m and 0 <= ny < n and ck[nx][ny] == 0:
                ck[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

for i in range(m):
    for j in range(n):
        if ck[i][j] == 0:
            q.append((i,j))
            temp = bfs(q)
            res.append(temp)
res.sort()
print(len(res))
print(*res)