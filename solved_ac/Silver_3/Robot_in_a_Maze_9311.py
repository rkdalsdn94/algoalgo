# 백준 - 실버3 - Robot in a Maze - 9311 - 그래프, bfs 문제
'''
그래프, bfs 문제

'S' 부터 시작해서 'G'를 찾는 문제이다.
찾는 과정은 기존의 bfs로 풀듯이 똑같이 풀면 된다.
만약 못 찾았을 경우 'No Exit'을 출력하고, 찾았을 경우 몇 번째 만에 찾았는지 거리를 출력한다.

풀이 과정
    1. 입력을 받는다.
    2. bfs를 돌면서 'S'를 찾는다.
    3. 'S'를 찾았다면 bfs를 돌면서 'G'를 찾는다.
    4. 'G'를 찾았다면 몇 번째 만에 찾았는지 출력한다.
    5. 못 찾았다면 'No Exit'을 출력한다.

in
    3
    7 8
    XXXXXXXX
    XSOOXOOX
    XOXOOOOX
    XOXXXOOX
    XOXOXXOX
    XOOOXOOX
    XXXXXGXX
    4 4
    XGXX
    XSOX
    XOOX
    XGGX
    4 4
    XXXX
    XSOX
    XXXX
    XXGX
out
    Shortest Path: 11
    Shortest Path: 1
    No Exit
'''

from collections import deque

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(a, b):
    ck[a][b] = 1
    q = deque([(a, b, 0)])

    while q:
        x, y, cnt = q.popleft()

        if board[x][y] == 'G':
            return cnt
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'X' and ck[nx][ny] == 0:
                ck[nx][ny] = 1
                q.append((nx, ny, cnt + 1))

    return 0

t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]
    ck = [[0] * c for _ in range(r)]
    res = 0

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S' and ck[i][j] == 0:
                res = bfs(i, j)

    if res == 0:
        print('No Exit')
    else:
        print(f'Shortest Path: {res}')
