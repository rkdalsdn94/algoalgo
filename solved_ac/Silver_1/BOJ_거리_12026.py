# 백준 - 실버1 - BOJ 거리 - 12026 - dp 문제
'''
dp 문제

풀이 과정
    1. n을 입력받는다.
    2. arr를 입력받는다.
    3. dp를 초기화한다.
    4. arr를 순회하며 dp를 계산한다.
        4.1. dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        4.2. dp[j]가 B이고 dp[i]가 O일 때, dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        4.3. dp[j]가 O이고 dp[i]가 J일 때, dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        4.4. dp[j]가 J이고 dp[i]가 B일 때, dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
    5. dp를 출력한다.
'''

n = int(input())
arr = input()

# 테스트
# n = 9
# arr = 'BOJBOJBOJ' # 8
# n = 8
# arr = 'BJJOOOBB' # -1
# n = 13
# arr = 'BJBBJOOOJJJB' # 50
# n = 2
# arr = 'BO' # 1
# n = 15
# arr = 'BJBOJOJOOJOBOOO' # 52

dp = [0] + [float('inf')] * (n - 1)

for i in range(1, n):
    for j in range(i):
        if arr[j] == 'B' and arr[i] == 'O':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

        if arr[j] == 'O' and arr[i] == 'J':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

        if arr[j] == 'J' and arr[i] == 'B':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
