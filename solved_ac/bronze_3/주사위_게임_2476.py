# 백준 - 브론즈3 - 주사위 게임 - 2476 - 단순 구현, 수학, 사칙연산 문제
'''
단순 구현, 수학, 사칙연산 문제

if 문으로 구현하면 되는 단순한 사칙연산 구현 문제이다.

in
    3
    3 3 6
    2 2 2
    6 2 5
out
    12000
'''

n = int(input())
res = 0

for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        res = max(res, 10000 + a * 1000)
    elif a == b or b == c or a == c:
        if b == c:
            a = b
        res = max(res, 1000 + a * 100)
    else:
        a = max(a, b, c)
        res = max(res, a * 100)

print(res)
