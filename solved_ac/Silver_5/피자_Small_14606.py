# 백준 - 실버5 - 피자 Small - 14606 - 수학, dp 문제
'''
수학, dp 문제

수학을 활용한 dp 문제이다.
다음의 점화식으로 풀면 된다.
 - dp [n] = (n - 1) + dp [n - 1]
'''

n = int(input())

# 테스트
# n = 1 # 0
# n = 3 # 3
# n = 5 # 10
# n = 8 # 28

dp = [0] * 11
dp[1] = 0
dp[2] = 1

for i in range(3, n + 1):
    m = i // 2
    dp[i] = m * (i - m) + dp[m] + dp[i - m]

print(dp[n])
