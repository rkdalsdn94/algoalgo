'''
구현, dp 문제

n, n_list를 입력 받은 후에
작아지는 dp(smaller_dp), 커지는 dp(bigger_dp) 를 만든 후
 ㄴ> (입력값을 인덱스 번호 그대로 사용하기 위해서 n_list와 두 dp에 + 1 씩해서 만들었다.)
그 후에 어떤 값이 커지거나, 작아지거나(같은 경우 포함)을 한 후에 더해줬다.

문제에 주어진 요구사항을 잘 구현하면 되는 문제이다. dp 수식은 크게 계산하지 않아도 구할수 있다.
'''

n = int(input())
n_list = [0] + list(map(int, input().split()))

# 테스트
# n = 9
# n_list = [0] + [1,2,2,4,4,5,7,7,2] # 8
# n = 9
# n_list = [0] + [4,1,3,3,2,2,9,2,3] # 4
# n = 11
# n_list = [0] + [1,5,3,6,4,7,1,3,2,9,5] # 2

smaller_dp = [1] * (n + 1)
bigger_dp = [1] * (n + 1)

for i in range(2, n + 1):
    if n_list[i - 1] >= n_list[i]:
        smaller_dp[i] = smaller_dp[i-1] + smaller_dp[i]
    if n_list[i - 1] <= n_list[i]:
        bigger_dp[i] = bigger_dp[i-1] + bigger_dp[i]

print(max(max(smaller_dp), max(bigger_dp)))
