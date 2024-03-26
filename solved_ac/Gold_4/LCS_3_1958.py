# 백준 - 골드4 - LCS 3 - 1958 - dp, 최장 공통 수열(LCS), 문자열 문제
'''
dp, 최장 공통 수열(LCS), 문자열 문제

기존의 골드5 LCS (9251) 문제에서 풀었던 방식과 비슷하다,
    - LCS 2(9252)는 경로를 추가했어야 됐는데 현재 문제는 길이만 구하면 되므로 LCS(9251) 문제를 응용했다.
단, 이 문제에선 3개의 문자열이 주어지고, 3개의 문자열의 LCS를 구해야 된다. 그래서 3차원 배열을 사용했다.

풀이 과정 (기존 코드와 달라진 부분)
 - 기존 골드5 문제에 있는 LCS (9251) 문제와 같은 방식으로 풀면 된다.
    - 다만 3차원 배열을 사용해서 dp를 만들어야 된다.
 - 이후로는 똑같이 풀면 되서 기존의 코드를 보면 이해가 된다.
'''

x, y, z = [0] + list(input()), [0] + list(input()), [0] + list(input())

# 테스트
# x, y, z = [0] + list('abcdefghijklmn'), [0]  + list('bdefg'), [0] + list('efg')

n, m, l = len(x), len(y), len(z)
dp = [[[0] * l for _ in range(m)] for _ in range(n)]

def lcs(x, y, z):
    for i in range(1, n):
        for j in range(1, m):
            for k in range(1, l):
                if x[i] == y[j] and y[j] == z[k]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[-1][-1][-1]

res = lcs(x, y, z)
print(res)
