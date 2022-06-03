'''
dp, 완전 탐색 문제

아래 코드로 제출하려면 Pypy3로 제출해야 된다. Python3로 하면 시간 초과가 나온다.
'''

import math

# n = int(input())

# 테스트
n = 25 # 1
n = 26 # 2
n = 11339 # 3
n = 34567 # 4

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    temp = n + 2

    for j in range(1, int(math.sqrt(i)) + 1):
        temp = min(temp, dp[i - j ** 2])
    
    dp[i] = temp + 1

print(dp[n])
