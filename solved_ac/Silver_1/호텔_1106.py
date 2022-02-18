'''
각 각의 n_list들을 순회하면서 dp를 갱신한다
dp[z] = min(dp[z], dp[z - j] + i) 이 점화식만 세우면 구현은 간단하게 진행된다.
'''

INF = int(1e9)

c, n = map(int, input().split())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# c, n, n_list = 12, 2, [[3, 5], [1, 1]] # 8
# c, n, n_list = 10, 3, [[3, 1], [2, 2], [1, 1]] # 4
# c, n, n_list = 10, 10, [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]] # 10
# c, n, n_list = 100, 6, [[4, 9], [9, 11], [3, 4], [8, 7], [1, 2], [9, 8]] # 45
# print(c, n, n_list)

dp = [INF] * (c + 100)
dp[0] = 0

for i, j in n_list:
    for z in range(j, c + 100):
        dp[z] = min(dp[z], dp[z - j] + i)

print(min(dp[c:c + 100]))

