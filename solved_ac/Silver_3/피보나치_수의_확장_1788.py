# 백준 - 실버3 - 피보나치 수의 확장 - 1788 - 수학, dp 문제
'''
수학, dp 문제

문제 문류의 수학이 있어서 수학을 적긴 했지만 피보나치를 구현하면 되는 문제이다.
근데, n이 음수로 입력됐을 때도 생각해야 되지만 어렵지 않다.
n이 -1 보다 작을 때 f(n) 양수인지 음수인지 때문에 고민이 됐었는데, 아래 블로그에서 힌트를 얻고 문제를 풀었다.
이 부분은 https://star7sss.tistory.com/554 여기 블로그를 참조하면 도움이 된다.
'''

n = int(input())

if n == 0:
    print(0)
    print(0)
elif n == 1:
    print(1)
    print(1)
elif n == -1:
    print(1)
    print(1)
elif n > 1:
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp [i - 2]) % 1000000000

    print(1)
    print(dp[n])
elif n < -1:
    dp = [0] * (abs(n) + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, abs(n) + 1):
        dp[i] = (dp[i - 1] + dp [i - 2]) % 1000000000

    print(-1 if abs(n) % 2 == 0 else 1)
    print(dp[abs(n)])
