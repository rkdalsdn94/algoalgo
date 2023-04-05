# 백준 - 실버2 - 지구 온난화 - 5212 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

구현이 생각보다 조금 복잡한 시뮬레이션 문제이다.
deepcopy를 이용해 new_board로 기존의 board를 copy한다.
 - 기존 board의 값을 변경하면 처음 반복문을 돌 때 기존 board의 값이 변경돼서 안된다.

직사각형을 구하는 부분은 행(row)과 열(col)에서 'X'가 나오는 행, 해당 행에서 'X'가 나오는 열의 제일 큰 값을 구한다.
구해진 행과 열로 board를 출력하면 된다.
'''

import copy

r, c = map(int, input().split())
board = [ list(input()) for _ in range(r) ]

# 테스트
# r, c = 5, 3
# board = [
#     list('...'),
#     list('.X.'),
#     list('.X.'),
#     list('.X.'),
#     list('...')
# ] # X
# r, c = 3, 10
# board = [
#     list('..........'),
#     list('..XXX.XXX.'),
#     list('XXX.......')
# ] # .XX...X   \  XX.....

new_board = copy.deepcopy(board)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
start_col = c - 1
end_col = 0

for i in range(r):
    for j in range(c):
        if board[i][j] != '.':
            temp = 0            
            for z in range(4):
                nx, ny = i + dx[z], j + dy[z]

                if nx < 0 or nx >= r or ny < 0 or ny >= c or board[nx][ny] == '.':
                    temp += 1

            if temp >= 3:
                new_board[i][j] = '.'

for i in range(r):
    if 'X' in new_board[i]:
        start_row = i
        break

for i in range(r - 1, -1, -1):
    if 'X' in new_board[i]:
        end_row = i
        break

for i in range(start_row, end_row + 1):
    temp = [ i for i, value in enumerate(new_board[i]) if value == 'X' ]
    if not temp:
        continue
    col_start_temp = temp[0]
    col_end_temp = temp[-1]
    start_col = min(start_col, col_start_temp)
    end_col = max(end_col, col_end_temp)

for i in range(start_row, end_row + 1):
    for j in range(start_col, end_col + 1):
        print(new_board[i][j], end='')
    print()
