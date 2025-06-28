# 백준 - 실버2 - The Chivalrous Cow - 6004 - bfs 문제
"""
bfs 문제

[핵심 아이디어]
    1. 체스의 나이트 이동 패턴(L자 형태)을 8방향으로 구현
    2. BFS를 사용하여 최단 경로 탐색
    3. 맵의 좌표계가 아래에서 위로 읽히므로 이를 고려한 좌표 변환

[풀이 과정]
    1. 입력을 받아 맵을 구성하고 시작점(K)과 목표점(H)의 위치를 찾는다
    2. 나이트의 8가지 이동 방향을 정의한다 (L자 형태: ±2,±1 또는 ±1,±2)
    3. BFS를 사용하여 시작점에서 목표점까지의 최단 거리를 구한다
    4. 장애물(*)을 피하고 맵 범위를 벗어나지 않도록 체크한다
"""

from collections import deque

x, y = map(int, input().split())
y_list = [input() for _ in range(y)]

# 테스트
# x, y = 10, 11
# y_list = [
#     '..........', '....*.....', '..........',
#     '...*.*....', '.......*..', '..*..*...H',
#     '*.........', '...*...*..', '.K........',
#     '...*.....*', '..*....*..'
# ] # 5

# 나이트의 8가지 이동 방향 (L자 형태)
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# 시작점과 목표점 찾기
for i in range(y):
    for j in range(x):
        if y_list[i][j] == 'K':
            start = (i, j, 0)
        elif y_list[i][j] == 'H':
            end = (i, j)

def bfs(start, end):
    q = deque([start])
    ck = [[0] * x for _ in range(y)]
    ck[start[0]][start[1]] = 1

    while q:
        a, b, cnt = q.popleft()

        # 목표점에 도달했을 때
        if (a, b) == end:
            return cnt

        # 나이트의 8가지 이동 방향 탐색
        for i in range(8):
            nx, ny = a + dx[i], b + dy[i]

            # 맵 범위 내에 있고, 장애물이 아니며, 방문하지 않은 곳
            if 0 <= nx < y and 0 <= ny < x and y_list[nx][ny] != '*' and ck[nx][ny] == 0:
                ck[nx][ny] = 1
                q.append((nx, ny, cnt + 1))

print(bfs(start, end))
