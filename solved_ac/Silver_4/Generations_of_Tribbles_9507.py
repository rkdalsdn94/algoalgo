# 백준 - 실버4 - Generations of Tribbles - 9507 - dp 문제
'''
dp 문제

문제에 주어진 아래 점화식을 그대로 구현하면 되는 문제이다.
n < 2 :                         1
n = 2 :                         2
n = 3 :                         4
n > 3 : koong(n − 1) + koong(n − 2) + koong(n − 3) + koong(n − 4)

미리 입력으로 들어올 수 있는 dp list의 값들을 만들어놓고, 해당 인덱스를 출력하는 방식으로 풀었다.

in
    8
    0
    1
    2
    3
    4
    5
    30
    67
out
    1
    1
    2
    4
    8
    15
    201061985
    7057305768232953720
'''

dp = [0] * 68
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 68):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
