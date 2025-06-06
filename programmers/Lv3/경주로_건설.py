# 프로그래머스 - Lv3 - 경주로 건설 - 그래프, bfs, 다익스트라
"""
그래프, bfs, 다익스트라

[핵심 아이디어]
    1. 같은 좌표에 도달하더라도 어느 방향에서 왔는지에 따라 비용이 달라질 수 있음
    2. 3차원 방문 배열 사용: visited[x][y][direction]로 각 방향별 최소 비용 관리
    3. 직선 도로는 100원, 코너(방향 전환)는 500원 추가
    4. BFS로 모든 경로를 탐색하되, 더 적은 비용으로 도달할 수 있는 경우만 큐에 추가

[풀이 과정]
    1. 시작점 (0,0)에서 우측(0), 하측(1) 두 방향으로 동시에 시작
    2. 각 위치에서 4방향으로 이동 가능성 확인:
       - 같은 방향으로 직진: 직선 도로 비용(100) 추가
       - 방향 전환: 코너 비용(500) + 직선 도로 비용(100) 추가
    3. 해당 방향에서 그 위치에 더 적은 비용으로 도달 가능한 경우만 탐색 진행
    4. 목적지 (N-1, N-1)에 도달했을 때 모든 방향 중 최소 비용 반환
"""

from collections import deque

def solution(board):
    n = len(board)
    # 방향: 0(우), 1(하), 2(좌), 3(상)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    # 3차원 방문 배열: [x][y][direction] = 최소비용
    visited = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]

    # BFS 큐: (x, y, direction, cost)
    queue = deque()

    # 시작점에서 우측(0), 하측(1) 방향으로 시작
    if n > 1:  # 우측으로 이동 가능한 경우
        if board[0][1] == 0:
            queue.append((0, 1, 0, 100))
            visited[0][1][0] = 100
        # 하측으로 이동 가능한 경우
        if board[1][0] == 0:
            queue.append((1, 0, 1, 100))
            visited[1][0][1] = 100

    while queue:
        x, y, direction, cost = queue.popleft()

        # 현재 비용이 이미 기록된 최소 비용보다 크면 스킵
        if cost > visited[x][y][direction]:
            continue

        # 4방향으로 이동 시도
        for next_dir in range(4):
            nx = x + dx[next_dir]
            ny = y + dy[next_dir]

            # 범위 체크 및 벽 체크
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                # 같은 방향으로 직진하는 경우
                if direction == next_dir:
                    next_cost = cost + 100
                else:
                    # 방향 전환하는 경우 (코너 + 직선)
                    next_cost = cost + 600

                # 더 적은 비용으로 도달 가능한 경우만 큐에 추가
                if next_cost < visited[nx][ny][next_dir]:
                    visited[nx][ny][next_dir] = next_cost
                    queue.append((nx, ny, next_dir, next_cost))

    return min(visited[n-1][n-1])

print(solution([[0,0,0],[0,0,0],[0,0,0]]) == 900)
board = [
    [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]
]
print(solution(board) == 3800)
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]) == 2100)
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]) == 3200)
