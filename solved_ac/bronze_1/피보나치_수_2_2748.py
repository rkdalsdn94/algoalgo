'''
dp 문제

기본적인 피보나치 문제이다. dp로 메모이제이션 기법을 활용해서 풀면 된다.
dp식도 문제에 나와있다. 그대로 구현하면 된다.
식은 F[n] = F[n-1] + F[n-2] (n ≥ 2) 이렇게 나온다.
'''

n = int(input())

# 테스트
# n = 10 # 55

dp = [0,1,1]

for i in range(3, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[n])
