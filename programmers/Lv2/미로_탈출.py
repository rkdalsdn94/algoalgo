# 프로그래머스 - Lv2 - 미로 탈출 - 그래프, bfs 문제
"""
그래프, bfs 문제

[핵심 아이디어]
    1. 미로 탈출은 두 단계로 나뉨: 시작점 → 레버, 레버 → 출구
    2. 각 단계별로 bfs를 사용하여 최단 경로를 찾음
    3. 두 단계의 최단 경로 합이 총 이동 시간
    4. 어느 한 단계라도 도달할 수 없다면 미로 탈출 불가능

[풀이 과정]
    1. 미로에서 시작점('S'), 레버('L'), 출구('E')의 위치를 찾음
    2. bfs를 사용하여 시작점에서 레버까지의 최단 거리 계산
    3. bfs를 사용하여 레버에서 출구까지의 최단 거리 계산
    4. 두 거리의 합이 최종 결과, 어느 경로든 도달할 수 없으면 -1 반환
"""

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    # 시작점, 레버, 출구 위치 찾기
    start, lever = None, None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)

    # 시작점에서 레버까지의 최단 거리 계산
    dist_to_lever = bfs(maps, start, 'L', n, m)
    if dist_to_lever == -1:  # 레버까지 도달할 수 없으면 탈출 불가
        return -1

    # 레버에서 출구까지의 최단 거리 계산
    dist_to_exit = bfs(maps, lever, 'E', n, m)
    if dist_to_exit == -1:  # 출구까지 도달할 수 없으면 탈출 불가
        return -1

    # 총 이동 시간 = (시작 'S' -> 레버 'L') + (레버 'L' -> 출구 'E')
    return dist_to_lever + dist_to_exit

def bfs(maps, start, target, n, m):
    x, y = start[0], start[1]
    q = deque([(x, y, 0)])
    ck = [[0] * m for _ in range(n)]
    ck[x][y] = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        a, b, dist = q.popleft()

        if maps[a][b] == target:
            return dist

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and not ck[nx][ny]:
                ck[nx][ny] = 1
                q.append((nx, ny, dist + 1))

    return -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])) # 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])) # -1
