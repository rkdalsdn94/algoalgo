# 백준 - 점프 - 실버1 - dp 문제
'''
dp 문제

풀이 과정
1. N * N 판인 n_list와 dp 배열을 만들고, dp 배열의 시작인 가장 왼쪽 위의 값을 1로 초기화한다.
2. n_list의 해당 값으로 밑으로 내려가는 down, 오른쪽으로 이동하는 right 변수를 만든다.
3. down과 right의 값이 board의 크기를 벗어나지 않을 때 dp 배열을 해당 값으로 더해주면서 값을 초기화 한다.
4. 마지막으로 dp 배열의 가장 오른쪽 아래의 값을 출력하면 된다.
'''

n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 4
# n_list = [[2,3,3,1], [1,2,1,3], [1,2,3,1], [3,1,1,0]] # 3

dp = [ [0] * n for _ in range(n) ]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break

        down = n_list[i][j] + i
        right = n_list[i][j] + j

        if down < n:
            dp[down][j] += dp[i][j]
        if right < n:
            dp[i][right] += dp[i][j]

print(dp[n - 1][n - 1])
