# 백준 - 브론즈3 - 별 찍기 8 - 2445 - 구현 문제
'''
구현 문제

단순하면서 복잡한 구현 문제이다.
계속 print로 찍어보면서 감을 익히는 게 중요한 거 같다.

in
    5
out
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    ****  ****
    ***    ***
    **      **
    *        *
'''

n = int(input)

for i in range(1, n + 1):
    star = '*' * i
    space = ' ' * 2 * (n - i)
    print(star + space + star)

for i in range(1, n):
    star = '*' * (n - i)
    space = ' ' * 2 * i
    print(star + space + star)
