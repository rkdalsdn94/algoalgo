# 백준 - 브론즈1 - 데칼코마니 - 23841 - 구현, 문자열 문제
'''
구현, 문자열 문제

입력으로 들어온 값(board)에서 절반을 나눈 뒤 계산해야 된다.
절반으로 나눈 값의 앞과 뒤 중 한 쪽만 '.'이면 해당 '.'을 반대편 글자로 바꾸면 된다.
'''

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 테스트
# n, m = 3, 6
# board = [list('G..R..'), list('..B...'), list('Y.....')]
# '''
#     G.RR.G
#     ..BB..
#     Y....Y
# '''

for i in range(n):
    for j in range(1, m // 2 + 1):
        if board[i][-j] == '.' and board[i][j - 1] != '.':
            board[i][-j] = board[i][j - 1]
        elif board[i][j - 1] == '.' and board[i][-j] != '.':
            board[i][j - 1] = board[i][-j]

for i in board:
    print(''.join(i))
