# 백준 - 골드5 - 동전 2 - 2294 - dp 문제
'''
dp 문제

dp를 이용해서 문제를 풀었다.

dp 배열을 10001의 값으로 k + 1까지 초기화한다.
coin_list에서 값을 하나 씩 꺼낸 후 dp의 값을 더 작은 값으로 바꿔주면 된다.
바꾸는 식은 dp[i], dp[i - coin] + 1 하면 된다. 손으로 풀어보면 감이 온다.
'''

n, k = map(int, input().split())
coin_list = [ int(input()) for _ in range(n) ]

# 테스트
# n, k = 3, 15
# coin_list = [1,5,12] # 3

dp = [10001] * (k + 1)
dp[0] = 0

for coin in coin_list:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k]) if dp[k] != 10001 else print(-1)
