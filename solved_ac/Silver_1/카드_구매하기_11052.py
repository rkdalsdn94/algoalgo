'''
dp 문제

기본적인 dp문제이다. 주어진 예제를 손으로 풀다보면 감이 온다.
dp문제를 최근에 몇 번 풀었어서 그런지 금방 감이 왔다.
'''

n = int(input()) # 카드의 개수
p_list = list(map(int, input().split()))

# 테스트
# n, p_list = 4, [1, 5, 6, 7] # 10
# n, p_list = 5, [10, 9, 8, 7, 6] # 50
# n, p_list = 10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] # 55
# n, p_list = 10, [5, 10, 11, 12, 13, 30, 35, 40, 45, 47] # 50
# n, p_list = 4, [5, 2, 8, 10] # 20
# n, p_list = 4, [3, 5, 15, 16] # 18

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i-j] + p_list[j-1])

print(dp[n])
