# 백준 - 실버1 - 봄버맨 - 16918 - 구현, 그래프(bfs), 시뮬레이션 문제
'''
구현, 그래프(bfs), 시뮬레이션 문제

문제에서 적혀 있는 아래의 조건들을 구현하면 된다.
1. 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해 놓는다. 모든 폭탄이 설치된 시간은 같다.
2. 다음 1초 동안 봄버맨은 아무것도 하지 않는다.
3. 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
4. 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
5. 3과 4를 반복한다.
6. board 출력

in
    6 7 3
    .......
    ...O...
    ....O..
    .......
    OO.....
    OO.....
out
    OOO.OOO
    OO...OO
    OOO...O
    ..OO.OO
    ...OOOO
    ...OOOO

in
    6 7 4
    .......
    ...O...
    ....O..
    .......
    OO.....
    OO.....
out
    OOOOOOO
    OOOOOOO
    OOOOOOO
    OOOOOOO
    OOOOOOO
    OOOOOOO

in
    6 7 5
    .......
    ...O...
    ....O..
    .......
    OO.....
    OO.....
out
    .......
    ...O...
    ....O..
    .......
    OO.....
    OO.....
'''

from collections import deque

r, c, n = map(int, input().split())
board = [ list(input()) for _ in range(r) ] # 1. - 입력으로 들어온 값으로 폭탄 설치

dx, dy = [1,0,-1,0], [0,1,0,-1]
n -= 1 # 2. - 1 초동안 아무것도 하지 않기

while n: # 5. - 반복
    bomb_place = deque()

    for i in range(r): # 폭탄을 설치한 위치 기억
        for j in range(c):
            if board[i][j] == 'O':
                bomb_place.append([i, j])

    for i in range(r): # 3. - 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다. 즉, 모든 칸은 폭탄을 가지고 있게 된다. 폭탄은 모두 동시에 설치했다고 가정한다.
        for j in range(c):
            if board[i][j] != 'O':
                board[i][j] = 'O'

    n -= 1 # 4.1. - 1초 지난 후
    if n == 0:
        break

    while bomb_place: # 4.2. - 위에서 설치한 폭탄 기억으로 폭탄 터트리기
        aaa, bbb = bomb_place.popleft()
        board[aaa][bbb] = '.'

        for i, j in zip(dx, dy):
            nx, ny = aaa + i, bbb + j

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'O':
                board[nx][ny] = '.'
    n -= 1

for i in board: # 6. - board 출력
    print(''.join(i))
