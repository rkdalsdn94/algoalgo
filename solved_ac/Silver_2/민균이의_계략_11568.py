# 백준 - 실버2 - 민균이의 계략 - 11568 - dp, 가장 긴 증가하는 부분 수열(LIS) 문제
'''
dp, 가장 긴 증가하는 부분 수열(LIS) 문제

dp 배열로 가장 긴 증가하는 수열을 구하면 되는 문제이다.
전에 LIS 문제 풀이들을 참고하거나 LIS 알고리즘을 보고 오면 어렵지 않게 풀 수 있다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 5
# n_list = [ 8, 9, 1, 2, 10 ] # 3
# n = 8
# n_list = [ 5, 4, 3, 2, 1, 6, 7, 8 ] # 4

dp = [1] * (n + 1)

for i in range(1, n):
    for j in range(i):
        if n_list[j] < n_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
