# 백준 - 실버4 - Hexagonal Tiles - 5705 - dp 문제
'''
dp 문제

단순한 dp 문제이다.

풀이 과정
    1. dp[1] = 1, dp[2] = 2로 초기화한다.
    2. dp[i] = dp[i-1] + dp[i-2]로 dp를 채운다.
    3. n이 0이면 종료한다.
    4. dp[n]을 출력한다.

in
    1
    4
    2
    10
    0
out
    1
    5
    2
    89
'''

dp = [0] * 50
dp[1] = 1
dp[2] = 2

for i in range(3, 50):
    dp[i] = dp[i - 1] + dp[i - 2]

while 1:
    n = int(input())

    if n == 0:
        break

    print(dp[n])
