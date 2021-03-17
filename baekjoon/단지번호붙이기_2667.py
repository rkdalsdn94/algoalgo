# 백준 단지번호붙이기 - 2667
from collections import deque
# n = 7
# n_list = [list('0110100'),list('0110101'),list('1110101'),
# list('0000111'),list('0100000'),list('0111110'),list('0111000')]
'''
out
3
7
8
9
'''
n = int(input())
n_list = [list(input()) for _ in range(n)]

res = []
ck = [[0] * n for _ in range(n)]
dx, dy = (1,0,-1,0), (0,1,0,-1)
q = deque()

def bfs(x, y, cnt):
    q.append((x,y))
    cnt = cnt
    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < n and n_list[nx][ny] == '1' and ck[nx][ny] == 0:
                cnt += 1
                q.append((nx, ny))
                ck[nx][ny] = 1

    res.append(cnt)


for i in range(n):
    for j in range(n):
        if n_list[i][j] == '1' and ck[i][j] == 0:
            cnt = 1
            ck[i][j] = 1
            bfs(i, j, cnt)
print(len(res))
for i in sorted(res):
    print(i)