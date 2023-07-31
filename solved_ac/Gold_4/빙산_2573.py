# 백준 - 골드4 - 빙산 - 2573 - 그래프, bfs, 구현 문제
'''
그래프, bfs, 구현 문제

PyPy3 로 제출해야 시간 초과를 안 받을 수 있다.

단순하게 빙산의 위치를 bfs 로 돌면서 바로 빙산이 녹게 만들었다가 몇 번 틀렸었다. (추가로 시간 초과도 몇 번 받음)
틀리다가 이해가 잘 안돼서 검색을 통해 정보를 얻었는데, 빙산 주변의 바다 즉, 빙산의 위치에서 bfs를 시작해 근처 0의 갯수를 따로 count 해주는 게 필요하다고 알게 되었다.

따라서, while 반복문을 실행하면서 n 과 m 만큼 반복하면서 빙산이 있을 경우 bfs 를 시작한다.
bfs 안에서 sea_list 라는 리스트 변수로 주변의 바다의 숫자를 체크할 수 있게 빙산에서 주변의 값이 0일 경우 더해준다.
                elif g[nx][ny] == 0:
                    sea_list[a][b] += 1
이 부분만 조심한 후 bfs 가 종료될 때는 1을 리턴하고, 그 값을 temp 에 더해준다.
리턴된 temp 의 값이 2보다 크거나 같을 경우 빙산이 나눠진 경우 이므로 몇 번 while 반복문을 반복했는지 res를 출력하고 종료하면 된다.
temp 의 값이 0이라면 빙산이 다 녹을 때까지 분리되지 않은 경우이므로 0을 출력하고 종료하면 된다.
'''

from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# from collections import deque
# n, m = 5, 7
# g = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 2, 4, 5, 3, 0, 0],
#     [0, 3, 0, 2, 5, 2, 0],
#     [0, 7, 6, 2, 4, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0]
# ] # 2

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
res = 0

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        a, b = q.popleft()
        ck[a][b] = 1

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if g[nx][ny] and ck[nx][ny] == 0: # bfs 조건으로 아직 방문하지 않은 곳이고, 이동할 곳이 방신인 경우엔 q에 담아준다.
                    ck[nx][ny] = 1
                    q.append([nx, ny])
                elif g[nx][ny] == 0: # --> 주변의 바다가 있을 경우 sea_list 의 해당 빙산의 위치를 1씩 더해준다.
                    sea_list[a][b] += 1
    return 1

while 1:
    temp = 0
    sea_list = [[0] * m for _ in range(n)]
    ck = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if g[i][j] and ck[i][j] == 0:
                temp += (bfs(i, j)) # 빙산일 때 bfs 를 실행하고, 그 결과를 출력할 때 사용

    for i in range(n):
        for j in range(m):
            g[i][j] = max(0, g[i][j] - sea_list[i][j]) # 빙산이 음수가 되는걸 방지하기 위해

    if temp >= 2: # 빙산이 분리된 경우
        print(res)
        exit(0)
    elif temp == 0: # 빙산이 모두 녹았는데, 분리되지 않은 경우
        print(0)
        exit(0)

    res += 1
