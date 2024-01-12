# 백준 - 브론즈3 - 수학적 호기심 - 9094 - 수학, 완전 탐색 문제
'''
수학, 완전 탐색 문제

간단한 수학과 해당 범위를 완전 탐색으로 아래의 조건을 만족하는 수의 개수를 찾으면 되는 문제이다.
    - (a^2 + b^2 + m) / (ab) 의 식을 적용했을 때 정수인 값의 개수

PyPy3로 제출하거나
Python3라면 import sys; input=sys.stdin.readline 을 해야 된다.

in
    3
    10 1
    20 3
    30 4
out
    2
    4
    5
'''

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    res = 0

    for i in range(1, n):
        for j in range(i + 1, n):
            if (i ** 2 + j ** 2 + m) % (i * j) == 0:
                res += 1

    print(res)
