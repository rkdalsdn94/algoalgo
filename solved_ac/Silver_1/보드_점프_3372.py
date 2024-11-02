# 백준 - 실버1 - 보드 점프 - 3372 - dp 문제
'''
dp 문제

풀이 과정
    1. n을 입력받는다.
    2. board를 입력받는다.
    3. dp를 초기화한다.
    4. dp[0][0]을 1로 초기화한다.
    5. dp를 순회하면서 dp[i][j]가 0이 아니면 dp[i][j]만큼 이동한다.
        5.1. i + board[i][j]가 n보다 작으면 dp[i + board[i][j]][j]에 dp[i][j]를 더한다.
        5.2. j + board[i][j]가 n보다 작으면 dp[i][j + board[i][j]]에 dp[i][j]를 더한다.
    6. dp를 출력한다.
'''

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 4
# board = [
#     [2, 3, 3, 1], [1, 2, 1, 3], [1, 2, 3, 1], [3, 1, 1, 0]
# ] # 3

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue

        if i + board[i][j] < n:
            dp[i + board[i][j]][j] += dp[i][j]

        if j + board[i][j] < n:
            dp[i][j + board[i][j]] += dp[i][j]

print(dp[-1][-1])
