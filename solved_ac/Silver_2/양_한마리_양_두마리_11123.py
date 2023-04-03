# 백준 - 실버2 - 양 한마리 양 두마리 - 11123 - 그래프, bfs, dfs 문제
'''
그래프, bfs, dfs 문제

단순한 그래프 문제이다. bfs 방식으로 문제를 풀었다.
bfs 문제의 전형적인 문제이다.

in
    2
    4 4
    #.#.
    .#.#
    #.##
    .#.#
    3 5
    ###.#
    ..#..
    #.###
out
    6
    3
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

'''
dfs 풀이

import sys; sys.setrecursionlimit(10**7)

t = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    ck[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '#' and ck[nx][ny] == 0:
            ck[nx][ny] = 1
            dfs(nx, ny)

for _ in range(t):
    h, w = map(int, input().split())
    board = [ input() for _ in range(h) ]
    ck = [ [0] * w for _ in range(h) ]
    res = 0

    for i in range(h):
        for j in range(w):
            if board[i][j] == '#' and ck[i][j] == 0:
                dfs(i, j)
                res += 1
    print(res)
'''
