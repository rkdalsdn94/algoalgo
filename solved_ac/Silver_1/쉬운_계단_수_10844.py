# 백준 - 쉬운 계단 수 - 10844 - 실버1 - dp 문제
'''
dp 문제

점화식은 아래와 같이 나온다.
1 ~ 8 : dp[i - 1][j - 1] + dp[i - 1][j + 1]
0     : dp[i - 1][1] 
9     : dp[i - 1][8]

1 ~ 8 조건은 대각선의 위치에 있는 수들의 합이랑 같다.
0, 9 는 양쪽의 대각선이 없는 위치이므로 1, 8로만 더하면 된다.

각 자리수의 마지막 글자(?) 숫자(?)가
해당 글자의 몇 개가 올 수 있을지 손으로 구하다 보면 감이 온다.

ex) n = 2 일때
0 이 올 수 있는 경우 -> 10     -> 1
1 이 올 수 있는 경우 -> 21     -> 1
2 가 올 수 있는 경우 -> 12, 32 -> 2
3 이 올 수 있는 경우 -> 23, 43 -> 2
    .                      -> 2
    .                      -> 2
    .                      -> 2
9 가 올 수 잇는 경우 -> 89     -> 1
뒤의 결과를 다 더한 후 1000000000으로 나누면 된다.
'''

n = int(input())

# 테스트
# n = 1 # 9
# n = 2 # 17
# n = 3 # 32 

dp = [ [0] * 10 for _ in range(n + 1) ]

for i in range(1, 10):
    dp[1][i] = 1 

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)