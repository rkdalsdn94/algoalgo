# 백준 - 골드5 - 동전 1 - 2293 - dp 문제
'''
dp 문제

주어진 코인의 종류를 반복하면서 dp[k] 의 범위까지 동전의 종류들로 dp[k]의 값을 몇 개를 만들 수 있는지 구하면 되는 문제다.
따라서, coin_list의 값을 하나 씩 꺼내면서 dp의 값들을 더하면 된다.
dp[i]에다 dp[j - i] 의 값들을 더하면 됩니다.
'''

n, k = map(int, input().split())
coin_list = [ int(input()) for _ in range(n) ]

# 테스트
# n, k = 3, 10
# coin_list = [1,2,5] # 10

dp = [0] * (k + 1)
dp[0] = 1

for i in coin_list:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])
