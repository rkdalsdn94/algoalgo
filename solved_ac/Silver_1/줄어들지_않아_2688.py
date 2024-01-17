# 백준 - 실버1 - 줄어들지 않아 - 2688 - dp 문제
'''
dp 문제

n이 3일 때까지 손으로 풀어보면 규칙이 보인다.
n = 1, [1] * 10 = 10
n = 2, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] = 55
n = 3, [55, 45, 36, 28, 21, 15, 10, 6, 3, 1] = 220

즉, 이 전의 총 합을 0번째 인덱스 그 다음부터 이 전 값을 빼면 된다.
계산을 편하게 하기 위해 이전 값들의 합을 dp의 마지막 인덱스로 만들었다.

in
    3
    2
    3
    4
out
    55
    220
    715
'''

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0] * 11 for _ in range(n + 1)]
    dp[1] = [1] * 10 + [10]

    if n == 1:
        print(10)
        continue

    for i in range(2, n + 1):
        for j in range(11):
            if j == 10:
                dp[i][-1] = sum(dp[i])
            elif j == 0:
                dp[i][0] = dp[i - 1][-1]
            else:
                dp[i][j] = dp[i][j - 1] - dp[i - 1][j - 1]

    print(dp[n][-1])
