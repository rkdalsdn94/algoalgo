# 백준 - 골드5 - Cow Beauty Pageant - 5931 - 그래프, bfs 문제
'''
그래프, bfs 문제

두 개의 bfs를 만들어서 풀었다.
첫 번째 bfs는 영역을 구분하기 위해 사용하고, 두 번째 bfs는 영역을 구분한 후 최단 거리를 만들기 위해 사용했다.

풀이 과정
    1. 입력을 받고, 영역을 구분하기 위해 bfs를 사용한다.
    2. 영역을 구분한 후 각 영역의 좌표를 저장한다.
    3. 각 영역의 좌표를 이용하여 최단 거리를 만든다.
    4. 최단 거리를 만들 때, 최단 거리를 만들 수 있는 영역을 찾는다.
    5. 최단 거리를 만들 때, 최단 거리의 길이를 저장한다.
    6. 최단 거리의 길이를 저장한 후 최소 값을 출력한다.
'''

from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 테스트
# n, m = 6, 16
# board = [
#     list('................'), list('..XXXX....XXX...'),
#     list('...XXXX....XX...'), list('.XXXX......XXX..'),
#     list('........XXXXX...'), list('.........XXX....')
# ] # 3
# n, m = 3, 3
# board = [
#     list('..X'),
#     list('XX.'),
#     list('..X')
# ] # 1

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]
map_cnt = 1
res = int(1e9)

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = map_cnt

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 'X':
                    q.append((nx, ny))
                    visited[nx][ny] = map_cnt

for i in range(n):
    for j in range(m):
        if board[i][j] == 'X' and visited[i][j] == 0:
            bfs(i, j)
            map_cnt += 1

def bfs2(a):
    q = deque()
    dist = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == a:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 'X' and visited[nx][ny] != a:
                    return dist[x][y]
                elif board[nx][ny] == '.' and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return int(1e9)

for i in range(1, map_cnt):
    res = min(res, bfs2(i))
print(res)
