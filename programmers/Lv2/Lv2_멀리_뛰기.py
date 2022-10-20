# 프로그래머스 - Lv2 - 멀리 뛰기 - dp 문제
'''
dp 문제

사실 왜 Lv2로 필터되어 있는지 잘 모르겠다.. 조금 더 난이도를 낮춰도 될거 같다.
n에 숫자를 직접 대입해서 손으로 풀다보면 피보나치 수열이랑 똑같다는걸 알 수 있다.
그래서, 피보나치 수열 풀듯이 똑같이 풀어서 통과했다.
'''

def solution(n):
    dp = [0] * (n + 3)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1234567

print(solution(4) == 5)
print(solution(3) == 3)