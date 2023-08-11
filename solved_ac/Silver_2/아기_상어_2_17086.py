# 백준 - 실버2 - 아기 상어 2 - 17086 - 그래프, 완전 탐색, bfs 문제
'''
그래프, 완전 탐색, bfs 문제

bfs 풀이도 쉽게 풀리는 문제이다.
상어의 위치를 미리 q에 넣어놓은 뒤 bfs로 8방향(상,하,좌,우,좌상,우상,좌하,우하)을 탐색한다.
bfs로 탐색할 때 조건으로 g의 범위를 벗어나지 않고, 그래프의 인덱스의 값이 0이라면 q에 넣는다.
또한, 원래 그래프의 값에서 1을 더한 값으로 현재 검사한 그래프의 값을 변경한다.

while 문이 다 끝났을 시점 그래프 리스트에서 제일 큰 값에서 1을 빼고 출력하면 된다.
    (처음 상어가 있는 위치가 1이므로 이 값을 빼고 몇 번 이동했는지 체크하기 위해)
'''

from collections import deque

n, m = map(int, input().split())
g = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# from collections import deque
# n, m = 5, 4
# g = [
#     [0, 0, 1, 0],
#     [0, 0, 0, 0],
#     [1, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 1],
# ] # 2
# n, m = 7, 4
# g = [
#     [0, 0, 0, 1],
#     [0, 1, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, 0, 1],
# ] # 2

q = deque()
res = 0
dx, dy = [-1, -1, -1, 0, 1, 0, 1, 1], [-1, 0, 1, 1, 1, -1, 0, -1]

for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        a, b = q.popleft()

        for i in range(8):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                q.append([nx, ny])
                g[nx][ny] = g[a][b] + 1

    temp = 0
    for i in range(n):
        temp = max(temp, max(g[i]))

    return temp - 1

res = bfs()
print(res)
