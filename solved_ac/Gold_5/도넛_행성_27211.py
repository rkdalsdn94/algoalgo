# 백준 - 골드5 - 도넛 행성 - 27211 - 그래프, bfs 문제
'''
그래프, bfs 문제

풀이 과정
    1. n, m을 입력받는다.
    2. board를 입력받는다.
    3. ck를 만들어 0으로 초기화한다.
    4. dx, dy를 만들어 각각의 값을 넣는다.
    5. res를 0으로 초기화한다.
    6. bfs를 만들어 x, y를 받는다.
        6.1. q를 만들어 (x, y)를 넣는다.
        6.2. ck[x][y]를 1로 초기화한다.
        6.3. q가 빌 때까지 다음을 반복한다.
            6.3.1. a, b를 q.popleft()로 받는다.
            6.3.2. dx, dy를 돌면서 다음을 반복한다.
        6.4. nx, ny를 만들어 범위를 벗어나지 않는지 확인한다.
        6.5. 범위를 벗어나지 않는다면 q에 (nx, ny)를 넣고 ck[nx][ny]를 1로 초기화한다.
            6.5.1. 범위를 체크할 때 상 하 좌 우 서로 끝에서 끝으로 이동할 수 있으므로 모듈러 연산을 한다.
    7. board를 돌면서 다음을 반복한다.
        7.1. ck[i][j]가 0이고 board[i][j]가 0이라면 bfs(i, j)를 실행하고 res를 1 증가시킨다.
    8. res를 출력한다.
'''

from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m = 5, 6
# board = [
#     [1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 1, 1],
#     [1, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 1, 1]
# ] # 2
# n, m = 7, 8
# board = [
#     [0, 0, 1, 1, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 0, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1, 0, 0],
#     [1, 1, 0, 0, 0, 1, 0, 0],
#     [0, 1, 0, 0, 0, 1, 0, 1],
#     [0, 0, 1, 1, 1, 1, 0, 0]
# ] # 2

ck = [[0] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
res = 0

def bfs(x, y):
    q = deque([(x, y)])
    ck[x][y] = 1

    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j
            nx, ny = (nx + n) % n, (ny + m) % m

            if ck[nx][ny] == 0 and board[nx][ny] == 0:
                q.append((nx, ny))
                ck[nx][ny] = 1


for i in range(n):
    for j in range(m):
        if ck[i][j] == 0 and board[i][j] == 0:
            bfs(i, j)
            res += 1

print(res)
