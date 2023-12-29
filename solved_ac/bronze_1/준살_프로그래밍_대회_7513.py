# 백준 - 브론즈1 - 준살 프로그래밍 대회 - 7513 - 구현, 문자열 문제
'''
구현, 문자열 문제

단순 구현 문제이다.

in
    2
    4
    an
    bar
    doh
    mu
    2
    4 0 0 0 0
    2 3 1
    2
    a
    r
    1
    10 0 1 1 1 1 1 1 1 1 1
out
    Scenario #1:
    anananan
    mubar

    Scenario #2:
    arrrrrrrrr
'''

t = int(input())

for i in range(1, t + 1):
    m = int(input())
    m_list = [input() for _ in range(m)]
    print(f'Scenario #{i}:')

    n = int(input())
    for _ in range(n):
        n_list = list(map(int, input().split()))
        res = ''.join([m_list[i] for i in n_list[1:]])
        print(res)
    print()
