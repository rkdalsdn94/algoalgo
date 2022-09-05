# 백준 실버2 - 크로스워드 - 1706 - 구현, 문자열 문제
'''
구현, 문자열 문제

입력된 퍼즐(board)의 크기 만큼(r, c) 반복하면서
반복하는 중에 '#'이 아니면 temp에 해당 board[i][j] 글자를 추가한다.
반복문이 끝나거나 또는 '#' 을 만났을 때 temp의 길이가 2이상 이면 res에 추가해 놓고,
res를 정렬 후 0번째 인덱스에 있는걸 출력하면 된다.
'''

r, c = map(int, input().split())
board = [ input() for _ in range(r) ]

# 테스트
# r, c = 4, 5
# board = [ 'adaca', 'da##b', 'abb#b', 'abbac' ] # abb
# r, c = 5, 5
# board = [ 'good#', 'an##b', 'messy', 'e##it', '#late' ] # an

res = set()

for i in range(r): # 가로 체크
    temp = ''
    
    for j in range(c):
        if board[i][j] != '#':
            temp += board[i][j]
        elif board[i][j] == '#' and len(temp) >= 2:
            res.add(temp)
            temp = ''
        else:
            temp = ''
    if len(temp) >= 2:
        res.add(temp)

for i in range(c): # 세로 체크
    temp = ''
    
    for j in range(r):
        if board[j][i] != '#':
            temp += board[j][i]
        elif board[j][i] == '#' and len(temp) >= 2:
            res.add(temp)
            temp = ''
        else:
            temp = ''
    if len(temp) >= 2:
        res.add(temp)

print(sorted(res)[0])
