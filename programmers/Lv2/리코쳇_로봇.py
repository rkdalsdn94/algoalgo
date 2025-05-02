# 프로그래머스 - Lv2 - 리코쳇 로봇 - 그래프, bfs 문제
"""
그래프, bfs 문제

[핵심 아이디어]
    1. bfs를 사용하여 최단 경로를 찾는다
    2. 로봇이 한 방향으로 벽이나 장애물에 부딪힐 때까지 미끄러지는 특성을 구현한다
    3. 이미 방문한 위치는 다시 방문하지 않도록 처리한다
    4. 목표 지점에 도달하면 이동 횟수를 반환하고, 도달할 수 없으면 -1을 반환한다

[풀이 과정]
    1. 시작 위치(R)를 찾아 큐에 넣고 bfs 시작
    2. 현재 위치에서 4방향(상하좌우)으로 이동을 시도
    3. 각 방향으로 이동할 때, 벽이나 장애물을 만날 때까지 계속 이동 (미끄러짐 구현)
    4. 이동 후 새로운 위치가 이전에 방문하지 않은 위치라면 방문 표시 후 큐에 추가
    5. 목표 지점(G)에 도달하면 이동 횟수 반환
    6. 모든 가능한 위치를 탐색한 후에도 목표에 도달하지 못하면 -1 반환
"""

from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    start_x, start_y = find_start(board, m, n)
    q = deque([(start_x, start_y, 0)])
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 우 하 좌 상
    ck = [[0] * m for _ in range(n)]

    while q:
        a, b, cnt = q.popleft()

        if board[a][b] == 'G': # bfs는 최적해(최단 경로)를 보장하므로 'G'를 도착했을 때가 가장 작은 값
            return cnt

        for i in range(4):
            nx, ny = a, b

            while 1:
                nx, ny = nx + dx[i], ny + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 'D':
                    nx, ny = nx - dx[i], ny - dy[i]
                    break

            if (nx != a or ny != b) and ck[nx][ny] == 0:
                ck[nx][ny] = 1
                q.append((nx, ny, cnt + 1))

    return -1

def find_start(board, m, n):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                return i, j

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))# 7
print(solution([".D.R", "....", ".G..", "...D"])) # -1
