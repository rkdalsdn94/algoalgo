'''
in
    6 8 10
    25 52 60
    5 12 13
    0 0 0
out
    right
    wrong
    right

단순 수학 문제이다.

입력으로 들어온 a, b, c가 직각삼각형이면 right 아니면 wrong을 출력하면 된다.
a^2 + b^2 = c^2 이면 right 아니면 wrong

a, b, c 정렬되어 있는줄 알고 정렬을 따로 하지 않았는데 틀렸다....
정렬을 하고 다시 제출하니 통과됐다.
'''

while 1:
    a, b, c = sorted(map(int, input().split()))

    if a == 0 and b == 0 and c == 0:
        break

    if a ** 2 + b ** 2 == c ** 2:
        print('right')
    else:
        print('wrong')
