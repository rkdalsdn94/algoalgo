# 백준 - 골드3 - 모양 만들기 - 16932 - 그래프, bfs 문제
'''
그래프, bfs 문제

아래 코드는 그대로 제출했을 때 시간 초과가 날 수 있다.
따라서 검사하는 부분을 dict로 바꾸거나 시간을 줄이는 방법을 사용해야 한다.

풀이 과정
 1. 입력을 받고, 0인 좌표를 모두 저장한다.
 2. 0인 좌표를 하나씩 1로 바꾸고, bfs로 탐색한다.
 3. bfs 탐색이 끝나면 최대값을 출력한다.
'''

import sys; input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m = 3, 3
# board = [[0, 1, 1], [0, 0, 1], [0, 1, 0]] # 5
# n, m = 5, 4
# board = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]] # 10
# n, m = 3, 4
# board = [[0, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 1]] # 6

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
res = 0

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                q.append([nx, ny])
                cnt += 1

    return cnt

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            board[i][j] = 1
            res = max(res, bfs(i, j))
            board[i][j] = 0

print(res)
