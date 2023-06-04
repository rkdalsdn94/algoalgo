# 백준 - 실버1 - 현수막 - 14716 - 그래프, bfs, dfs 문제
'''
그래프, bfs, dfs 문제

단순한 그래프 문제이다.
graph 에서 1일 때 [상,하,좌,우, 대각선]으로 bfs, dfs를 실행하면 된다.
[상,하,좌,우, 대각선]으로 그래프 탐색할 때 연결이 종료되면 res를 1 증가시킨 후 출력하면 된다.

처음에 bfs로 먼저 풀었고, dfs 도 연습해야 돼서 파일 제일 아래 dfs 풀이도 적어놨다.
'''

from collections import deque

n, m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n, m = 8, 19
# graph = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0],
#     [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ] # 3

ck = [ [0] * m for _ in range(n) ]
dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]
res = 0

def bfs(x, y):
    q = deque([(x, y)])
    ck[x][y] = 1

    while q:
        a, b = q.popleft()

        for i in range(8):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append([nx, ny])
                ck[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and ck[i][j] == 0:
            bfs(i, j)
            res += 1

print(res)

'''
# dfs 풀이

n과 m만큼 반복하는 2중 for 문에서 dfs(i, j) 를 실행하면 된다.

import sys; sys.setrecursionlimit(10**7)
def dfs(x, y):
    ck[x][y] = 1
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and graph[nx][ny] == 1:
            dfs(nx, ny)
            ck[nx][ny] = 1
'''