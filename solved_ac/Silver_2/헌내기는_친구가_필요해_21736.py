# 백준 - 실버2 - 헌내기는 친구가 필요해 - 21736 - 그래프, bfs 문제
'''
그래프, bfs 문제

bfs 풀이로 풀면 된다.
    [상, 하, 좌, 우] 로 이동하면서 이동하려고 하는 위치가 'X'가 아니고, n과 m의 범위만 벗어나지 않으면 q에 계속 담는다.
    이동하려고 하는 위치(nx, ny)가 'P'이면 res를 1씩 더해주고, 최종적으로 res의 값이 있으면 res를 출력하고, 없으면 'TT'를 출력하면 된다.
    'P'이면 1씩 더하는 부분을 제대로 안 읽고 풀다가 틀렸었다. (그냥 1만 출력하는 줄...)
'''

from collections import deque

n, m = map(int, input().split())
g = [input() for _ in range(n)]

# 테스트
# n, m = 3, 5
# g = [
#     'OOOPO',
#     'OIOOX',
#     'OOOXP'
# ] # 1
# n, m = 3, 3
# g = [
#     'IOX',
#     'OXP',
#     'XPP'
# ] # TT

ck = [[0] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # [우, 하, 좌, 상] 으로 이동
res = 0

def bfs(x, y):
    global res
    q = deque([(x, y)])
    ck[x][y] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and g[nx][ny] != 'X':
                if g[nx][ny] == 'P':
                    res += 1
                ck[nx][ny] = 1
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if g[i][j] == 'I':
            bfs(i, j)

if res:
    print(res)
else:
    print('TT')
