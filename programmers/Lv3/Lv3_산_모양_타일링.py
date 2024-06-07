# 프로그래머스 - Lv3 - 산 모양 타일링 - dp 문제
'''
dp 문제

아래 코드만 보면 이해가 어려울 수 있으니, 그려보는 것이 좋다.
n이 1 ~ 3 까지만 그려보면 된다.
처음에는 top이 없이 생각하고, 그 다음에 top이 있는 경우를 생각하면 된다.
dp에서 0번째는 타일에서 오른쪽 끝이 기본 삼각형으로 생각했고, 1번째는 타일에서 오른쪽 끝이 다른 모양의 타일로 덮여진다고 생각했다.

풀이 과정
 1. 입력을 받고, dp를 2차원 리스트로 만든다.
 2. dp[0]은 i번째 수를 포함하는 연속합, dp[1]은 i번째 수를 포함하지 않는 연속합으로 초기화한다.
 3. dp[0]과 dp[1]을 계산하고, 최대값을 출력한다.
'''

def solution(n, tops):
    res = 0
    dp = [[0, 0] for _ in range(n)]
    MOD = 10007

    if tops[0] == 1:
        dp[0][0] = 3
        dp[0][1] = 1
    else:
        dp[0][0] = 2
        dp[0][1] = 1

    for i in range(1, n):
        if tops[i] == 1:
            dp[i][0] = (dp[i - 1][0] * 3) + (dp[i - 1][1] * 2) % MOD
        else:
            dp[i][0] = (dp[i - 1][0] * 2 + dp[i - 1][1]) % MOD
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD

    res = (dp[-1][0] + dp[-1][1]) % MOD
    return res

print(solution(1, [0])) # 3
print(solution(1, [1])) # 4
print(solution(2, [0, 0])) # 8
print(solution(3, [0, 0, 0])) # 21
print(solution(4, [1, 1, 0, 1])) # 149
print(solution(2, [0, 1])) # 11
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # 7704
