'''
구현, dp 문제

dp배열을 board의 현재 값 + dp 배열의 (r + 1, c), (r, c + 1), (r + 1, c + 1) 셋 값중 제일 큰 값
위의 식을 한 줄로 하면 dp[i][j] = board[i][j] + max(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1]) 식이 나온다.
위의 식에서 인덱스 에러와, 입력받은 값을 그대로 사용하기 위해 board보다 r, c 각각 + 1씩 더 큰 dp 배열을 만든다.
그리고 반복문의 범위와 인덱스를 적절히 고민하면 된다.
'''

n, m = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n, m = 3, 4
# board = [ [1,2,3,4], [0,0,0,5], [9,8,7,6] ] # 31
# n, m = 3, 3
# board = [ [1,0,0], [0,1,0], [0,0,1] ] # 3
# n, m = 4, 3
# board = [ [1,2,3], [6,5,4], [7,8,9], [12,11,10] ] # 47

dp = [ [0] * (m + 1) for _ in range(n + 1) ]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = board[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[-1][-1])
