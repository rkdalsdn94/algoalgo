# 백준 - 골드4 - 스도쿠 - 2580 - 백 트래킹, dfs 문제
'''
백 트래킹, dfs 문제

PyPy3로 제출해야 된다.

풀이 과정
 1. 입력을 받고, 빈 칸의 좌표를 temp에 저장한다.
 2. 빈 칸에 1부터 9까지 넣을 수 있는지 확인하고, dfs로 탐색한다.
 3. dfs 탐색이 끝나면 출력한다.
'''

board = [list(map(int, input().split())) for _ in range(9)]

# 테스트
# board = [
#     [0, 3, 5, 4, 6, 9, 2, 7, 8],
#     [7, 8, 2, 1, 0, 5, 6, 0, 9],
#     [0, 6, 0, 2, 7, 8, 1, 3, 5],
#     [3, 2, 1, 0, 4, 6, 8, 9, 7],
#     [8, 0, 4, 9, 1, 3, 5, 0, 6],
#     [5, 9, 6, 8, 2, 0, 4, 1, 3],
#     [9, 1, 7, 6, 5, 2, 0, 8, 0],
#     [6, 0, 3, 7, 0, 1, 9, 5, 2],
#     [2, 5, 8, 3, 9, 4, 7, 6, 0]
# ]
'''
out
    1 3 5 4 6 9 2 7 8
    7 8 2 1 3 5 6 4 9
    4 6 9 2 7 8 1 3 5
    3 2 1 5 4 6 8 9 7
    8 7 4 9 1 3 5 2 6
    5 9 6 8 2 7 4 1 3
    9 1 7 6 5 2 3 8 4
    6 4 3 7 8 1 9 5 2
    2 5 8 3 9 4 7 6 1
'''

temp = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            temp.append([i, j]) # 빈 칸을 모두 temp에 담고, 여기에 있는 빈 칸을 기준으로 백 트래킹 실행

def check(x, y, num):
    # row, column 검증
    for i in range(9):
        if board[x][i] == num or board[i][y] == num:
            return False

    # 3 * 3 검증
    nx, ny = x // 3 * 3, y // 3 * 3
    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if board[i][j] == num:
                return False
    return True

def dfs(cnt):
    if cnt == len(temp):
        for i in board:
            print(*i)
        exit(0) # print 이후에 종료되지 않으면 list index out of range 에러

    x, y = temp[cnt]
    for i in range(1, 10):
        if check(x, y, i):
            board[x][y] = i
            dfs(cnt + 1)
            board[x][y] = 0

dfs(0)
