# 백준 - 실버1 - Paint bucket - 15240 - 그래프, bfs, 플러드 필 문제
'''
그래프, bfs, 플러드 필 문제

핵심 아이디어
    - bfs를 통해 같은 색상을 가진 영역을 찾는다.
    - 해당 영역을 새로운 색상으로 변경한다.

풀이 과정
    1. n, m, c를 입력받는다.
    2. n x m 크기의 board를 입력받는다.
    3. x, y, k를 입력받는다.
    4. bfs를 통해 같은 색상을 가진 영역을 찾는다.
    5. 해당 영역을 새로운 색상으로 변경한다.
    6. 결과를 출력한다.
'''

from collections import deque

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
x, y, k = map(int, input().split())

# r, c = 4, 7
# board = [
#     list('0000000'), list('0111000'), list('0111010'), list('0000000')
# ]
# x, y, k = 0, 0, 3
# '''
# out
#     3333333
#     3111333
#     3111313
#     3333333
# '''
# r, c = 9, 9
# board = [
#     list('000000000'), list('011101110'), list('011101110'),
#     list('011011110'), list('000111000'), list('011110110'),
#     list('011101110'), list('011101110'), list('000000000')
# ]
# x, y, k = 4, 4, 2
# '''
# out
#     000000000
#     011102220
#     011102220
#     011022220
#     000222000
#     022220110
#     022201110
#     022201110
#     000000000
# '''

k = str(k)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque([(x, y)])
ck = [[0] * c for _ in range(r)]
origin = board[x][y]

while q:
    a, b = q.popleft()
    ck[a][b] = 1
    board[a][b] = k

    for i in range(4):
        nx, ny = a + dx[i], b + dy[i]

        if 0 <= nx < r and 0 <= ny < c and ck[nx][ny] == 0 and origin == board[nx][ny]:
            q.append([nx, ny])
            board[nx][ny] = k

for i in range(r):
    print(''.join(board[i]))
