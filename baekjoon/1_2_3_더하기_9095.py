# 백준 9095 - 1, 2, 3 더하기
'''
in
    3
    4
    7
    10
out
    7
    44
    274
'''

t = int(input())
n_list = [int(input()) for _ in range(t)]

dp=[1,2,4]

for i in range(3,max(n_list)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in n_list:
    print(dp[i-1])