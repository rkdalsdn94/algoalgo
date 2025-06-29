# 백준 - 실버1 - Feeding Time - 6031 - 그래프, bfs, dfs 문제
"""
그래프, bfs, dfs 문제

[핵심 아이디어]
    1. 8방향(상하좌우 + 대각선) 이동이 가능한 연결된 컴포넌트를 찾는 문제
    2. 각 목초지(연결된 풀밭 영역)의 크기를 구하고, 그 중 최댓값을 찾아야 함
    3. BFS를 사용하여 연결된 풀밭('.')의 개수를 카운트

[풀이 과정]
    1. 전체 농장을 순회하면서 아직 방문하지 않은 풀밭('.')을 발견하면 BFS 시작
    2. BFS로 현재 위치에서 8방향으로 연결된 모든 풀밭을 탐색하며 개수를 카운트
    3. 각 목초지별 풀밭 개수 중 최댓값을 저장하고 최종 결과로 출력
"""

from collections import deque

w, h = map(int, input().split())
graph = [input() for _ in range(h)]

# 테스트
# w, h = 10, 8
# graph = [
#     '...*....**', '..**....**', '...*....**', '...**.*.**',
#     '***.**.***', '...**.*.**', '...*.*****', '...***..**'
# ] # 21

# 8방향 이동 (상하좌우 + 대각선)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
ck = [[0] * w for _ in range(h)]
res = -1

def bfs(x, y):
    q = deque([(x, y)])
    ck[x][y] = 1
    cnt = 1

    while q:
        a, b = q.popleft()

        for i in range(8):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == '.' and ck[nx][ny] == 0:
                ck[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    return cnt

for i in range(h):
    for j in range(w):
        if graph[i][j] == '.' and ck[i][j] == 0:
            res = max(res, bfs(i, j))

print(res)
