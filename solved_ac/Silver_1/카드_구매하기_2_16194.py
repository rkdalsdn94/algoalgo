# 백준 - 실버1 - 카드 구매하기 2 - 16194 - dp 문제
'''
dp 문제

dp를 초기화할 때 0으로 초기화하면 안 된다. 이 부분만 기억하고 문제를 풀면 어렵지 않게 풀 수 있다.
'''

from copy import deepcopy

n = int(input())
n_list = [0] + list(map(int, input().split()))

# 테스트
# n = 4
# n_list = [0] + [1,5,6,7] # 4
# n = 5
# n_list = [0] + [10,9,8,7,6] # 6
# n = 10
# n_list = [0] + [1,1,2,3,5,8,13,21,34,55] # 5
# n = 10
# n_list = [0] + [5,10,11,12,13,30,35,40,45,47] # 26
# n = 4
# n_list = [0] + [5,2,8,10] # 4
# n = 4
# n_list = [0] + [3,5,15,16] # 10

dp = deepcopy(n_list)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + n_list[j])

print(dp[n])
