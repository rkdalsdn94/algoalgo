'''
문제를 보자마자 dp가 생각이 났다.
난이도가 높지 않아서 그런지 쉽게 풀 수 있었다.
max함수로 비교하면서 더 큰 값으로 해당 인덱스의 값을 변경하면 된다.
'''

# n = int(input())
# n_list = list(map(int, input().split()))

# 테스트
n = 10
n_list = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

dp = [0] * n
dp[0] = n_list[0]

for i in range(1, n):
    dp[i] = max(n_list[i], dp[i-1] + n_list[i])

print(max(dp))
