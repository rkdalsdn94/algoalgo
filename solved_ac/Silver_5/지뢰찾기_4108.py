# 백준 - 실버5 - 지뢰찾기 - 4108 - 구현 문제
'''
구현 문제

지뢰찾기를 구현하는 문제이다.

풀이 과정
    1. r, c를 입력받는다.
    2. board를 입력받는다.
    3. 8방향을 탐색하며 지뢰의 개수를 센다.
    4. 지뢰의 개수를 board에 저장한다.
    5. board를 출력한다.

in
    3 2
    ..
    .*
    ..
    5 5
    *.*.*
    ..*..
    *****
    .....
    ..**.
    0 0
out
    11
    1*
    11
    *3*3*
    36*63
    *****
    24553
    01**1
'''

while 1:
    r, c = map(int, input().split())
    board = [list(input()) for _ in range(r)]

    if r == 0 and c == 0:
        break

    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                cnt = 0

                for k in range(8):
                    nx, ny = i + dx[k], j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '*':
                        cnt += 1

                board[i][j] = cnt

    for i in board:
        print(''.join(map(str, i)))
