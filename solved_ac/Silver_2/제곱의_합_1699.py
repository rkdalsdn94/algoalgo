# 백준 - 실버2 - 제곱의 합 - 1699 - 수학, dp 문제
'''
수학, dp 문제

dp 문제이다.
완전 탐색처럼 1부터 n + 1까지 각각의 수를 제곱해서 답이 구해지는지 확인하면 된다.
dp값을 바꿀 때는 dp[i] 가 dp[i - j ** 2] + 1보다 크면 값을 수정하면 된다.
1을 더하는 이유는 이 전의 계산했던 값들을 더해줘야 하기 때문이다.

뭔가 설명이 어려워 다음 블로그를 읽어보면 더 이해가 잘 된다.
https://jyeonnyang2.tistory.com/50
'''

n = int(input())

# 테스트
# n = 7 # 4
# n = 1 # 1
# n = 11 # 3
# n = 13 # 2

dp = [ i for i in range(n + 1) ]

for i in range(1, n + 1):
    for j in range(1, i):
        if j ** 2 > i:
            break
        if dp[i] > dp[i - j ** 2] + 1:
            dp[i] = dp[i - j ** 2] + 1

print(dp[n])
