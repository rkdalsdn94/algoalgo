# 백준 - 실버3 - 진우의 달 여행(Small) - 17484 - dp, 완전 탐색 문제
'''
dp, 완전 탐색 문제

dp와 완전 탐색을 같이 풀어야 되는 문제이다.

풀이 과정
    1. 입력값을 받는다.
    2. 2차원 리스트를 만들어 입력값을 받는다.
    3. dp 리스트를 만들어 3차원 리스트를 만든다.
    4. dp[0][j][k]에 n_list[0][j]를 넣어준다.
    5. 1부터 n까지 반복문을 돌린다.
    6. 0부터 m까지 반복문을 돌린다.
    7. j가 0일 때 dp[i][j][0]에 min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + n_list[i][j]를 넣어준다.
    8. j가 m - 1일 때 dp[i][j][1]에 dp[i - 1][j][0] + n_list[i][j]를 넣어준다.
    9. j가 m - 1일 때 dp[i][j][1]에 dp[i - 1][j][2] + n_list[i][j]를 넣어준다.
    10. 그 외의 경우에는 dp[i][j][0]에 min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + n_list[i][j]를 넣어준다.
    11. dp[i][j][1]에 min(dp[i - 1][j][0], dp[i - 1][j][2]) + n_list[i][j]를 넣어준다.
    12. dp[i][j][2]에 min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + n_list[i][j]를 넣어준다.
    13. res에 int(1e9)를 넣어준다.
    14. m까지 반복문을 돌린다.
    15. 3까지 반복문을 돌린다.
    16. res에 min(res, dp[n - 1][i][j])를 넣어준다.
    17. res를 출력한다.
'''

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m = 6, 4
# n_list = [
#     [5, 8, 5, 1], [3, 5, 8, 4], [9, 77, 65, 5],
#     [2, 1, 5, 2], [5, 98, 1, 5], [4, 95, 67, 58]
# ] # 29

dp = [[[int(1e9)] * 3 for _ in range(m)] for _ in range(n)]

for i in range(1):
    for j in range(m):
        for k in range(3):
            dp[i][j][k] = n_list[i][j]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + n_list[i][j]
            dp[i][j][1] = dp[i - 1][j][0] + n_list[i][j]
        elif j == m - 1:
            dp[i][j][1] = dp[i - 1][j][2] + n_list[i][j]
            dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + n_list[i][j]
        else:
            dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + n_list[i][j]
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + n_list[i][j]
            dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + n_list[i][j]

res = int(1e9)
for i in range(m):
    for j in range(3):
        res = min(res, dp[n - 1][i][j])

print(res)
