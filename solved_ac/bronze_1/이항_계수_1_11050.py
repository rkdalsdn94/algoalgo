'''
단순 수학 문제이다.

이항 계수 공식으로 풀 수 있다. => n! / k!(n - k)!
'''

from math import factorial as fac

n, k = map(int, input().split())

# 테스트
# n, k = 5, 2 # 10

print(fac(n) // (fac(k) * fac(n - k)))
