# 프로그래머스 - Lv3 - 등굣길 - dp 문제
'''
dp 문제

풀이 과정
 1. dp 테이블을 만들어준다. (n+1) x (m+1) 크기로 만들어준다.
 2. 웅덩이가 있는 곳은 -1로 표시해준다.
 3. dp 테이블을 돌면서 웅덩이가 있는 곳은 0으로 초기화해준다.
 4. dp 테이블을 돌면서 dp[i][j]에 dp[i-1][j] + dp[i][j-1]을 더해준다.
 5. dp[n][m]을 반환한다.
'''

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i, j in puddles:
        dp[j][i] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue

            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m]

print(solution(4, 3, [[2, 2]])) # 4
