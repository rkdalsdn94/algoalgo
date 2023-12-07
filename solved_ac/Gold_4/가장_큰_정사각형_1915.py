# 백준 - 골드4 - 가장 큰 정사각형 - 1915 - dp 문제
'''
dp 문제

0 번째 행과 열이 아닐때, 이 전의 인덱스들을 검사하는 방식이다.
글로 설명하기 어려워 다음의 블로그를 첨부한다. 해당 블로그의 설명을 보면 이해하기 더 쉬워진다.
    - https://kyun2da.github.io/2021/04/09/biggestSquare/
'''

n, m = map(int, input().split())
n_list = [list(map(int, list(input()))) for _ in range(n)]

# 테스트
# n, m = 4, 4
# n_list = [[0, 0, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 1, 0]] # 4

dp = [[0] * m for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = n_list[i][j]
        elif n_list[i][j] != 0:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        res = max(dp[i][j], res)
print(res * res)
