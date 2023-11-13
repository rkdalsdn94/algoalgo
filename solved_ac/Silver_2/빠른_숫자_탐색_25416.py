# 백준 - 실버2 - 빠른 숫자 탐색 - 25416 - 그래프, bfs 문제
'''
그래프, bfs 문제

기본적인 bfs 문제이다.
r과 c의 위치에서 '1'을 만났을 때까지 ck를 통해 1씩 증가하면서 bfs를 실행한 뒤 횟수를 출력하면 되고,
만약 '1'을 만나지 못했다면 -1을 출력하면 된다.

마지막 입력으로 들어오는 r, c를 시작으로 bfs 시작하면 된다.
    - 처음에 문제를 잘 안 읽고 1, 1로 들어왔을 경우 (0, 0) 인 줄 알고 r - 1, c - 1 이렇게 bfs를 시작하게 했다.
    - 20% 안 쪽에서 틀렸습니다를 보고 문제를 다시 보는데 다음과 같이 되어 있었다.
        "즉, 맨 왼쪽 위 위치가 (0, 0), 맨 아래 오른쪽 위치가 (4, 4)이다."
    - 문제를 잘 읽어야 된다.
'''

from collections import deque

g = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

# 테스트
# g = [
#     [0, 0, 1, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, 0, 0],
#     [0, 0, -1, 0, 0], [0, 0, 0, -1, 0]
# ]
# r, c = 1, 1 # 2
# g = [
#     [0, 0, -1, 0, 0], [0, 0, -1, 0, 0], [0, 0, -1, 0, 0],
#     [0, 0, -1, 0, 0], [0, 0, -1, 0, 1]
# ]
# r, c = 1, 1 # -1

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
ck = [[-1] * 5 for _ in range(5)]

def bfs(x, y):
    q = deque([(x, y)])
    ck[x][y] = 0

    while q:
        a, b = q.popleft()

        if g[a][b] == 1:
            return ck[a][b]

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and ck[nx][ny] == -1 and g[nx][ny] != -1:
                q.append((nx, ny))
                ck[nx][ny] = ck[a][b] + 1

    return -1

res = bfs(r, c)  # r - 1, c - 1 이렇게 실행했다가 틀렸다.
print(res)
