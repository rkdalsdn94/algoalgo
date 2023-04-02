# 백준 - 실버2 - 양 한마리 양 두마리 - 11123 - 그래프, bfs, dfs 문제
'''
그래프, bfs, dfs 문제

단순한 그래프 문제이다. bfs 방식으로 문제를 풀었다.
bfs 문제의 전형적인 문제이다.
'''

from collections import deque

t = int(input())

def bfs(x, y):
    dx, dy = [1, 0 ,-1, 0], [0, 1, 0, -1]
    q = deque([(x, y)])

    while q:
        a, b = q.popleft()
        ck[a][b] = 1

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < h and 0 <= ny < w and ck[nx][ny] == 0 and board[nx][ny] == '#':
                q.append([nx, ny])
                ck[nx][ny] = 1

for _ in range(t):
    h, w = map(int, input().split())
    board = [ input() for _ in range(h) ]
    ck = [ [0] * w for _ in range(h) ]
    res = 0

    for i in range(h):
        for j in range(w):
            if board[i][j] == '#' and ck[i][j] == 0:
                bfs(i, j)
                res += 1

    print(res)
