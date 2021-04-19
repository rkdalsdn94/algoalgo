'''
in
    3
    2 2
    1 5
    13 29
out
    1
    5
    67863915
'''
# 조합 공식
from math import factorial
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    res = factorial(m) // (factorial(n) * factorial(m-n))
    # res = facto(m) // (facto(n) * facto(m-n))
    print(res)

# 함수로 푸는법
# def facto(n):
#     temp = 1
#     for i in range(1, n+1):
#         temp *= i
#     return temp

