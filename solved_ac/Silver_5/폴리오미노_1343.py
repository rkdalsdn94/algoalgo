'''
그리디, 문자열 문제
단순하게 구하면 된다. XXXX가 있으면 AAAA로 바꾸꼬 XX가 있다면 BB로 바꾸고
다 바꾼 후에 X가 남아 있다면 -1을 출력, 아니면 board 출력
'''
board = input()

# 테스트
# board = 'XXXXXX' # AAAABB
# board = 'XX.XX' # BB.BB
# board = 'XXXX....XXX.....XX' # -1
# board = 'X' # -1
# board = 'XX.XXXXXXXXXX..XXXXXXXX...XXXXXX' # BB.AAAAAAAABB..AAAAAAAA...AAAABB

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board: print(-1)
else: print(board)
