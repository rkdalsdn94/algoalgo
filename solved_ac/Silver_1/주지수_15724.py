# 백준 - 주지수 - 15742 - 실버1 - dp, 누적 합 문제
'''
dp, 누적 합 문제

혹시나 하는 마음으로 처음에 완전 탐색 방식으로 풀었는데 역시나 틀렸다..
그래서 dp식으론 아래와 같이 누적합을 계산해 풀었다.
dp[i][j] = board[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

풀이 과정
1. 입력값들을 잘 입력 받고, 빈 dp 배열을 행과 열 각각 1씩 크게 만들었다. -> select_list의 범위 그대로 사용하기 위해.
2. 1부터 시작하게 n과 m의 크기만큼 2중 반복문을 실행한다.
    2.1 반복문을 진행하면서 dp에 board의 누적 합을 계산한다. 식은 아래와 같다.
        dp[i][j] = board[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
3. 마지막에 선택되는 범위로 입력받은 select_list의 리스트 변수에서 값을 꺼내 해당 크기의 크기를 계산한다. 계산식은 아래에 있다.
    3.1 dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
'''

import sys; input = sys.stdin.readline

n, m = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]
k = int(input())
select_list = [ list(map(int, input().split())) for _ in range(k) ]

# 테스트
# n, m = 4, 4
# board = [ [9, 14, 29, 7], [1, 31, 6, 13], [21, 26, 40, 16], [8, 38, 11, 23] ]
# k = 3
# select_list = [ [1, 1, 3, 2], [1, 1, 1, 4], [1, 1, 4, 4]] # 102  59  293

dp = [ [0] * (m + 1) for _ in range(n + 1) ]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = board[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for i in select_list:
    x1, y1, x2, y2 = i
    print(dp[x1 - 1][y1 - 1] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x2][y2])

'''
시간 초과 코드 -> 완전 탐색 방식

n, m = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]
k = int(input())
select_list = [ list(map(int, input().split())) for _ in range(k) ]

for i in select_list:
    a, b, c, d = i
    res = 0

    for j in range(a - 1, c):
        for z in range(b - 1, d):
            res += board[j][z]

    print(res)
'''