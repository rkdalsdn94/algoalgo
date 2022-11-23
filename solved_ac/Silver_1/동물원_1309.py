# 백준 - 동물원 - 실버1 - 1309 - dp 문제
'''
dp 문제

매번 dp 문제를 풀 때는 느끼지만 항상 코드가 짧은거 같다.
점화식을 어떻게 구해야 될 지에 대해서 고민이 필요하다.
대부분 손으로 n을 3 ~ 4, 많으면 5 ~ 6까지 직접 구하다 보면 감이 온다.

n = 0 -> 1
n = 1 -> 2 + 1 => 3
n = 2 -> (2 + 1) * 2 + 1 => 7
n = 3 -> (7 * 2) + 1 => 17
n = 4 -> (17 * 2) + 7 => 41

위 과정을 진행해보고 나니 점화식은 아래와 같다.
dp[n] = (dp[n - 1] * 2) + dp[n - 2] 이다. -> 이 코드로 출력하면 된다.

매번 나머지 연산 하는걸 까먹어서 한 번은 틀리는거 같다.. % 9901을 해야 된다..
'''

n = int(input())

# 테스트
# n = 4 # 41

dp = [1] * (n + 2)
dp[1] = 3
dp[2] = 7

for i in range(3, n + 1):
    dp[i] = ((dp[i - 1] * 2) + dp[i - 2]) % 9901

print(dp[n])
