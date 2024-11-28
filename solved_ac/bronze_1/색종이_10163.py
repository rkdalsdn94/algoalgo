# 백준 - 브론즈1 - 색종이 - 10163 - 구현 문제
'''
구현 문제

색종이의 번호를 이용해 해당 색종이의 넓이를 구하면 되는 구현 문제이다.

풀이 과정
    1. 입력 받기
    2. 2차원 배열을 만들어 색종이의 번호를 넣는다.
    3. 해당 색종이의 넓이를 구하고 결과를 출력하면 된다.

in
    2
    0 0 10 10
    2 2 6 6
out
    64
    36

in
    3
    0 2 10 10
    7 9 8 4
    8 4 10 6
out
    81
    25
    60

in
    4
    0 2 10 10
    7 9 8 4
    8 4 10 6
    6 0 12 10
out
    62
    24
    0
    120
'''

n = int(input())
board = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, n + 1):
    x1, y1, w, h = map(int, input().split())

    for j in range(y1, y1 + h):
        board[j][x1 :x1 + w] = [i] * w

for i in range(1, n + 1):
    res = 0

    for j in range(1001):
        res += board[j].count(i)

    print(res)
