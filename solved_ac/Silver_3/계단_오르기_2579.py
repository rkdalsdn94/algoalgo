'''
dp문제인데, 실버1에 있는 포도주 시식(2156)이랑 비슷하다.
dp식도 똑같이 세워도 된다.
근데 이 문제에선 계단의 끝을(dp의 마지막) 꼭 가야 된다고 해서 마지막 반환할 때 dp[-1]로 반환하면 된다.
'''

# n = int(input())
# n_list = [ int(input()) for _ in range(n) ]

# 테스트
n = 6
n_list = [10, 20, 15, 25, 10, 20]

dp = [0] * n
dp[0] = n_list[0]

if n > 1:
    dp[1] = n_list[0] + n_list[1]

    if n > 2:
        dp[2] = max(n_list[2] + n_list[0], n_list[1] + n_list[2], dp[1])

        for i in range(3, n):
            dp[i] = max(n_list[i] + dp[i-2], dp[i-3] + n_list[i] + n_list[i-1], dp[-1])



print(dp[-1])
