# 백준 - 실버3 - 피보나치 - 9711 - 수학, dp 문제
'''
수학, dp 문제

단순하게 피보나치를 구하는 문제이다.
입력의 최대 범위가 10_000 이므로 미리 10_000까지의 피보나치 수열을 구해놓고,
미리 구한 피보나치 수열에서 p번째 인덱스의 값을 q로 나누고 출력하는 방식으로 풀었다.

in
    10
    5 10
    6 25
    10 21
    32 43
    100 100
    50 50
    25 25
    45 67
    109 32
    128 128
out
    Case #1: 5
    Case #2: 8
    Case #3: 13
    Case #4: 15
    Case #5: 75
    Case #6: 25
    Case #7: 0
    Case #8: 19
    Case #9: 9
    Case #10: 69
'''

dp = [0, 1, 1]
for i in range(3, 10_000 + 1):
    dp.append(dp[i - 1] + dp[i - 2])

t = int(input())
for i in range(1, t + 1):
    p, q = map(int, input().split())
    print(f'Case #{i}: {dp[p] % q}')
