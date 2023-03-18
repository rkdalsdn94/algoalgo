# 백준 - 실버1 - 배열 돌리기 3 - 16935 - 구현 문제
'''
구현 문제

문제에 있는 예제를 구현하면 된다.
대신, 3번이랑 4번을 구현할 땐 n과 m의 값을 변경해줘야 한다.
또, 5번과 6번에서 temp를 초기화할 때 실수로 m으로 초기화해서 인덱스 에러가 많이 나왔다........
    temp = [ [] for _ in range(m) ] -> 왜 m으로 했는지는 모르겠지만... m으로 해서 인덱스에러가 많이 나왔다.
질문 게시판에도 인덱스 에러에 관한 글이 많이 보이는데, temp를 초기화할 때 조심하면 될거 같다.
'''

n, m, r = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]
command = list(map(int, input().split()))

# 테스트
# n, m, r = 6, 8, 1
# board = [
#     [3, 2, 6, 3, 1, 2, 9, 7],
#     [9, 7, 8, 2, 1, 4, 5, 3],
#     [5, 9, 2, 1, 9, 6, 1, 8],
#     [2, 1, 3, 8, 6, 3, 9, 2],
#     [1, 3, 2, 8, 7, 9, 2, 1],
#     [4, 5, 1, 9, 8, 2, 1, 3]
# ]
# command = [1]
# '''
# out
#     4 5 1 9 8 2 1 3
#     1 3 2 8 7 9 2 1
#     2 1 3 8 6 3 9 2
#     5 9 2 1 9 6 1 8
#     9 7 8 2 1 4 5 3
#     3 2 6 3 1 2 9 7
# '''
# n, m, r = 6, 8, 1
# board = [
#     [3, 2, 6, 3, 1, 2, 9, 7],
#     [9, 7, 8, 2, 1, 4, 5, 3],
#     [5, 9, 2, 1, 9, 6, 1, 8],
#     [2, 1, 3, 8, 6, 3, 9, 2],
#     [1, 3, 2, 8, 7, 9, 2, 1],
#     [4, 5, 1, 9, 8, 2, 1, 3]
# ]
# command = [2]
# '''
#     7 9 2 1 3 6 2 3
#     3 5 4 1 2 8 7 9
#     8 1 6 9 1 2 9 5
#     2 9 3 6 8 3 1 2
#     1 2 9 7 8 2 3 1
#     3 1 2 8 9 1 5 4
# '''
# n, m, r = 6, 8, 1
# board = [
#     [3, 2, 6, 3, 1, 2, 9, 7],
#     [9, 7, 8, 2, 1, 4, 5, 3],
#     [5, 9, 2, 1, 9, 6, 1, 8],
#     [2, 1, 3, 8, 6, 3, 9, 2],
#     [1, 3, 2, 8, 7, 9, 2, 1],
#     [4, 5, 1, 9, 8, 2, 1, 3]
# ]
# command = [3]
# '''
#     4 1 2 5 9 3
#     5 3 1 9 7 2
#     1 2 3 2 8 6
#     9 8 8 1 2 3
#     8 7 6 9 1 1
#     2 9 3 6 4 2
#     1 2 9 1 5 9
#     3 1 2 8 3 7
# '''
# n, m, r = 6, 8, 1
# board = [
#     [3, 2, 6, 3, 1, 2, 9, 7],
#     [9, 7, 8, 2, 1, 4, 5, 3],
#     [5, 9, 2, 1, 9, 6, 1, 8],
#     [2, 1, 3, 8, 6, 3, 9, 2],
#     [1, 3, 2, 8, 7, 9, 2, 1],
#     [4, 5, 1, 9, 8, 2, 1, 3]
# 
# command = [4]
# '''
#     7 3 8 2 1 3
#     9 5 1 9 2 1
#     2 4 6 3 9 2
#     1 1 9 6 7 8
#     3 2 1 8 8 9
#     6 8 2 3 2 1
#     2 7 9 1 3 5
#     3 9 5 2 1 4
# '''
# n, m, r = 6, 6, 1
# board = [
#     [1, 6, 2, 9, 8, 4],
#     [7, 2, 6, 9, 8, 2],
#     [1, 8, 3, 4, 2, 9],
#     [7, 4, 6, 2, 3, 1],
#     [9, 2, 3, 6, 1, 5],
#     [4, 2, 9, 3, 1, 8]
# ]
# command = [4]
# '''
# out
#     4 2 9 1 5 8
#     8 8 2 3 1 1
#     9 9 4 2 6 3
#     2 6 3 6 3 9
#     6 2 8 4 2 2
#     1 7 1 7 9 4
# '''
# n, m, r = 6, 8, 1
# board = [
#     [3, 2, 6, 3, 1, 2, 9, 7],
#     [9, 7, 8, 2, 1, 4, 5, 3],
#     [5, 9, 2, 1, 9, 6, 1, 8],
#     [2, 1, 3, 8, 6, 3, 9, 2],
#     [1, 3, 2, 8, 7, 9, 2, 1],
#     [4, 5, 1, 9, 8, 2, 1, 3]
# ]
# command = [5]
# '''
#     2 1 3 8 3 2 6 3
#     1 3 2 8 9 7 8 2
#     4 5 1 9 5 9 2 1
#     6 3 9 2 1 2 9 7
#     7 9 2 1 1 4 5 3
#     8 2 1 3 9 6 1 8
# '''
# n, m, r = 6, 8, 1
# board = [
#     [3, 2, 6, 3, 1, 2, 9, 7],
#     [9, 7, 8, 2, 1, 4, 5, 3],
#     [5, 9, 2, 1, 9, 6, 1, 8],
#     [2, 1, 3, 8, 6, 3, 9, 2],
#     [1, 3, 2, 8, 7, 9, 2, 1],
#     [4, 5, 1, 9, 8, 2, 1, 3]
# ]
# command = [6]
# '''
#     1 2 9 7 6 3 9 2
#     1 4 5 3 7 9 2 1
#     9 6 1 8 8 2 1 3
#     3 2 6 3 2 1 3 8
#     9 7 8 2 1 3 2 8
#     5 9 2 1 4 5 1 9
# '''
# n, m, r = 6, 8, 6
# board = [
#     [3, 2, 6, 3, 1, 2, 9, 7],
#     [9, 7, 8, 2, 1, 4, 5, 3],
#     [5, 9, 2, 1, 9, 6, 1, 8],
#     [2, 1, 3, 8, 6, 3, 9, 2],
#     [1, 3, 2, 8, 7, 9, 2, 1],
#     [4, 5, 1, 9, 8, 2, 1, 3]
# ]
# command = [1, 2, 3, 4, 5, 6]
# '''
#     3 1 2 8 9 1 5 4
#     1 2 9 7 8 2 3 1
#     2 9 3 6 8 3 1 2
#     8 1 6 9 1 2 9 5
#     3 5 4 1 2 8 7 9
#     7 9 2 1 3 6 2 3
# '''

def board_rotation_1(board):
    for i in range(1, n // 2 + 1):
        board[i - 1], board[-i] = board[-i], board[i - 1]
    return board

def board_rotation_2(board):
    for i in range(n):
        for j in range(1, m // 2 + 1):
            board[i][j - 1], board[i][-j] = board[i][-j], board[i][j - 1]
    return board

def board_rotation_3(board):
    temp = [ [] for _ in range(m) ]
        
    for i in range(m):
        for j in range(n - 1, -1, -1):
            temp[i].append(board[j][i])
    return temp

def board_rotation_4(board):
    temp = [ [] for _ in range(m) ]
    idx = 0

    for i in range(m - 1, -1, -1):
        for j in range(n):
            temp[idx].append(board[j][i])
        idx += 1
    return temp

def board_rotation_5(board):
    temp = [ [] for _ in range(n) ]

    for i in range(n // 2, n): # 4 -> 1
        for j in range(m // 2):
            temp[i - (n // 2)].append(board[i][j])

    for i in range(n // 2): # 1 -> 2
        for j in range(m // 2):
            temp[i].append(board[i][j])

    for i in range(n // 2, n): # 3 -> 4
        for j in range(m // 2, m):
            temp[i].append(board[i][j])

    for i in range(n // 2): # 2 -> 3
        for j in range(m // 2, m):
            temp[(n // 2) + i].append(board[i][j])

    return temp

def board_rotation_6(board):
    temp = [ [] for _ in range(n) ]

    for i in range(n // 2): # 2 -> 1
        for j in range(m // 2, m):
            temp[i].append(board[i][j])

    for i in range(n // 2, n): # 3 -> 2
        for j in range(m // 2, m):
            temp[i - (n // 2)].append(board[i][j])

    for i in range(n // 2): # 1 -> 4
        for j in range(m // 2):
            temp[n - (n // 2) + i].append(board[i][j])

    for i in range(n // 2, n): # 4 -> 3
        for j in range(m // 2):
            temp[i].append(board[i][j])

    return temp

def board_rotation_calculation(x):
    global board, n, m

    if x == 1:
        board = board_rotation_1(board)
    elif x == 2:
        board = board_rotation_2(board)
    elif x == 3:
        board = board_rotation_3(board)
        n, m = m, n
    elif x == 4:
        board = board_rotation_4(board)
        n, m = m, n
    elif x == 5:
        board = board_rotation_5(board)
    elif x == 6:
        board = board_rotation_6(board)

for i in command:
    board_rotation_calculation(i)

for i in board:
    print(*i)