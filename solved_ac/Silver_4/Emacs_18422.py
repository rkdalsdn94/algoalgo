# 백준 - 실버4 - Emacs - 18422 - 구현, 그리디 문제
'''
구현, 그리디 문제

구현, 그리디 문제라고 하는데, bfs 방식으로 풀었다.
다른 사람 풀이를 참고해봤을 때, dx, dy 가 필요 없는걸 보면 그리디로 들어가도 괜찮을거 같기도하고..
개인적으로 편한 방식인 bfs로 풀었다.

dx, dy를 사용하지 않으려면 g의 0 번째 인덱스에 insert를 통해 '.'을 b + 1 크기로 추가해주고,
각 배열의 인덱스마다 '.'을 추가한 뒤 res를 더해주는 조건을 다음과 같이 하면 된다.
    if (g[i][j] == '*' and g[i][j - 1] != '*' and g[i - 1][j] != '*')
'''

from collections import deque

n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]

# 테스트
# n, m = 6, 7
# g = [
#     list('***....'),
#     list('***..**'),
#     list('.....**'),
#     list('.***.**'),
#     list('.***...'),
#     list('.***...')
# ] # 3
# n, m = 3, 3
# g = [
#     '*.*',
#     '...',
#     '*.*'
# ] # 4
# n, m = 1, 10
# g = ['.*.**.***.'] # 3

res = 0
ck = [[0] * m for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(x, y):
    q = deque([(x, y)])

    while q:
        a, b = q.popleft()
        ck[a][b] = 1

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and g[nx][ny] != '.':
                q.append([nx, ny])
                ck[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if g[i][j] != '.' and ck[i][j] == 0:
            bfs(i, j)
            res += 1

print(res)
