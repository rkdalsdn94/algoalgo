# 백준 - 골드5 - 연속합 2 - 13398 - dp 문제
'''
dp 문제

풀이 과정
 1. 입력을 받고, dp를 2차원 리스트로 만든다.
 2. dp[0]은 i번째 수를 포함하는 연속합, dp[1]은 i번째 수를 포함하지 않는 연속합으로 초기화한다.
 3. dp[0]과 dp[1]을 계산하고, 최대값을 출력한다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 10
# n_list = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1] # 54

dp = [[i for i in n_list] for _ in range(2)]

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + n_list[i], n_list[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + n_list[i])

print(max(map(max, dp)))
