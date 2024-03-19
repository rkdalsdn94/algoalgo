# 백준 - 골드4 - LCS 2 - 9252 - dp, 최장 공통 수열(LCS) 문제
'''
dp, 최장 공통 수열(LCS) 문제

기존의 골드5 LCS (9251) 문제에서 풀었던 방식과 똑같은데, LCS가 만들어지는 경로를 추가하면 된다.

풀이 과정 (기존 코드와 달라진 부분)
 - 똑같은 lcs 알고리즘에서 x[i] 와 y[j] 가 같을 때 단어를 추가하기 위해 dp 배열을 빈 문자열로 초기화했다.
 - x[i]와 y[j]가 같을 때 기존 dp 배열에서 전의 값 + x[i]를 추가한다.
 - x[i]와 y[j]가 다를 때는 dp[i - 1][j]와 dp[i][j - 1] 중에 길이가 더 긴 것으로 초기화한다.
 - dp[-1][-1]에는 최종적인 LCS가 만들어진다.
 - 이후 lcs 함수의 결과를 res로 받고, 길이와 res를 출력하면 된다.
'''

x, y = [0] + list(input()), [0] + list(input())

# 테스트
# x, y = [0] + list('ACAYKP'), [0] + list('CAPCAK') # 4  \  ACAK

n, m = len(x), len(y)
dp = [[''] * m for _ in range(n)]

def lcs(x, y):
    for i in range(1, n):
        for j in range(1, m):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + x[i]
            else:
                if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    return dp[-1][-1]

res = lcs(x, y)
print(len(res))
print(res)
