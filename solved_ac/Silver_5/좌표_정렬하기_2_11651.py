'''
단순 정렬 문제

x, y를 입력받고 y먼저 정렬 후 x 정렬하면 된다. --> 람다로 처리했다.
'''

# n = int(input())
# board = sorted([ list(map(int, input().split())) for _ in range(n) ], key=lambda x: (x[1], x[0]))

# 테스트
n = 5
board = [[0,4], [1,2], [1,-1], [2,2], [3,3]]
board = sorted(board, key=lambda x: (x[1], x[0]))

for i in range(len(board)):
    print(*board[i])
