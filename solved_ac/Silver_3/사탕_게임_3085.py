'''
구현, 완전 탐색 문제

board로 받은 값들을 2중 반복문으로 값을 바꿔가며(두 값이 서로 다를 때만)
완전 탐색을 한다. 값들을 바꾼 후에 원래 값으로 다시 바꿔주고
cnt를 통해 max값을 구해주기
'''

n = int(input())
board = [list(input()) for _ in range(n)]

# 테스트
# n, board = 3, [ list('CCP'), list('CCP'), list('PPC') ] # 3
# n, board = 4, [ list('PPPP'), list('CYZY'), list('CCPY'), list('PPCC') ] # 4
# n = 5
# board = [ list('YCPZY'), list('CYZZP'), list('CCPPP'), list('YCYZC'), list('CPPZZ') ] # 4

res = 0

def count(board):
    max_num = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_num = max(max_num, cnt)
        cnt = 1
        for j in range(1,n):
            if  board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_num = max(max_num, cnt)

    return max_num

for i in range(n):
    for j in range(n):
        if j+1 < n and (board[i][j] != board[i][j+1]):
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            temp = count(board)
            res = max(res,temp)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i+1 < n and (board[i+1][j] != board[i][j]):
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            temp = count(board)
            res = max(res,temp)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(res)

