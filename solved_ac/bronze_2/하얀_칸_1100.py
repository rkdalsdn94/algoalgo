'''
단순한 구현 문제다.
8칸의 체스판에 번갈아가면서 흰색일 때에((i + j) % 2 == 0)
말(F)이 있으면 res + 1을 하면 된다.
'''

chess_board = [ list(input()) for _ in range(8) ]

# 테스트
# chess_board = [list('.F.F...F'), list('F...F.F.'), list('...F.F.F'), list('F.F...F.'),
#             list('.F...F..'), list('F...F.F.'), list('.F.F.F.F'), list('..FF..F.')] # 1
# chess_board = [list('........'), list('........'), list('........'), list('........'),
#             list('........'), list('........'), list('........'), list('........')] # 0
# chess_board = [list('FFFFFFFF'), list('FFFFFFFF'), list('FFFFFFFF'), list('FFFFFFFF'),
#             list('FFFFFFFF'), list('FFFFFFFF'), list('FFFFFFFF'), list('FFFFFFFF')] # 32
# chess_board = [list('........'), list('..F.....'), list('.....F..'), list('.....F..'),
#             list('........'), list('........'), list('.......F'), list('.F......')] # 2

res = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and chess_board[i][j] == 'F':
            res += 1

print(res)
