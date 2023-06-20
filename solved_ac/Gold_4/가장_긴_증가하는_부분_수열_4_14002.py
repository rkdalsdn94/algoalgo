# 백준 - 골드4 - 가장 긴 증가하는 부분 수열 4 - 14002 - dp, 가장 긴 증가하는 부분 수열 문제
'''
dp, 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)

전에 풀었었던 가장 긴 증가하는 부분 수열 문제로 풀면 된다.
단, 정답을 출력할 때 가장 긴 증가하는 부분 수열을 출력해야 돼서 이 부분을 좀 헤맸다.
해결하는 방법은 dp에서 길이로 출력할 max 값을 temp 변수에 담은 후,
dp 의 마지막 값 부터 0까지 역순으로 돌면서 temp와 같은 값이 dp의 값이면 해당 번째 n_list의 값을 res에 추가하면 된다.

코드가 많이 어렵지 않아 금방 이해할 수 있다.
'''

n = int(input())
n_list = list(map(int, input().split()))

# 테스트
# n = 6
# n_list = [10, 20, 10, 30, 20, 50] # 4  \  10 20 30 50

res = []
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

temp = max(dp)
for i in range(n - 1, -1, -1): # 
    if dp[i] == temp:
        res.append(n_list[i])
        temp -= 1

print(max(dp))
print(*sorted(res))
