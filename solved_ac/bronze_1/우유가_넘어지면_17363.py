# 백준 - 브론즈1 - 우유가 넘어지면 - 17363 - 구현, 문자열 문제
'''
구현, 문자열 문제

단순한 구현 문제이다.

풀이 과정
    1. 입력을 받고, board를 만든다.
    2. res를 만든다.
    3. board를 순회하면서 방향을 바꾼다.
    4. res를 출력한다.
'''

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# n, m = 14, 7
# board = [
#     list('.......'),
#     list('...O...'),
#     list('.......'),
#     list('.-----.'),
#     list('...|...'),
#     list('...|...'),
#     list('.......'),
#     list('.......'),
#     list('...O...'),
#     list('.......'),
#     list('.-----.'),
#     list('..|.|..'),
#     list('..|.|..'),
#     list('.......')
# ]
# n, m = 7, 6
# board = [
#     list('..^...'),
#     list('/---\.'),
#     list('<...|\\'),
#     list('<.O.|>'),
#     list('<...|/'),
#     list('\---/.'),
#     list('..v...'),
# ]

res = [[] for _ in range(m)]

for i in range(n):
    for j in range(m):
        temp = board[i][j]

        if temp == '-':
            temp = '|'
        elif temp == '|':
            temp = '-'
        elif temp == '\\':
            temp = '/'
        elif temp == '/':
            temp = '\\'
        elif temp == '^':
            temp = '<'
        elif temp == '<':
            temp = 'v'
        elif temp == 'v':
            temp = '>'
        elif temp == '>':
            temp = '^'

        res[j].append(temp)

for i in res[::-1]:
    print(''.join(i))
