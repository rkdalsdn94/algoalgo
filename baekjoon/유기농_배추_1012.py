from collections import deque
'''
int(input()) = 2
n, m, k = 10, 8, 17
cabbage_list = [ [0, 0], [1, 0], [1, 1], [4, 2], [4, 3], [4, 5], [2, 4],[3, 4]
[7, 4],[8, 4],[9, 4],[7, 5],[8, 5],[9, 5],[7, 6],[8, 6],[9, 6]  # 5
n, m, k = 10, 10, 1
[5, 5] # 1
'''
q = deque()
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def bfs(q):
    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < m and cabbage_list[nx][ny] == 1:
                cabbage_list[nx][ny] = 0
                q.append((nx, ny))

for _ in range(int(input())):
    res = 0
    # 가로, 세로, 배추 위치 개수
    m, n, k = map(int, input().split())
    cabbage_list = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        cabbage_list[y][x] = 1

    for i in range(n):
        for j in range(m):
            if cabbage_list[i][j] == 1:
                cabbage_list[i][j] = 0
                q.append((i, j))
                bfs(q)
                res += 1
    print(res)
