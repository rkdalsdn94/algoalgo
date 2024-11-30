# 백준 - 실버1 - 현이의 로봇 청소기 - 30106 - 그래프, bfs, 플러드 필 문제
'''
그래프, bfs, 플러드 필 문제

풀이 과정
    1. 입력 받기
    2. bfs 함수를 통해 로봇 청소기가 청소할 수 있는 공간을 찾는다.
    3. bfs 함수에서 청소할 수 있는 공간을 찾을 때마다 res에 1을 더해준다.
        3.1. 공간을 찾는 방법은 bfs를 통해 상하좌우를 탐색하면서 청소할 수 있는 공간을 찾는다.
        3.2. 이때 청소할 수 있는 공간은 현재 위치와 다음 위치의 차이가 k보다 작거나 같아야 한다.
    4. res 출력
'''

from collections import deque

n, m, k = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m, k = 2, 3, 2
# n_list = [[5, 4, 6], [4, 7, 2]] # 3

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque([(0, 0)])
ck = [[0] * m for _ in range(n)]
res = 0

def bfs(x, y):
    q.append((x, y))
    ck[x][y] = 1

    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and abs(n_list[a][b] - n_list[nx][ny]) <= k:
                ck[nx][ny] = 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if ck[i][j] == 0:
            bfs(i, j)
            res += 1

print(res)
