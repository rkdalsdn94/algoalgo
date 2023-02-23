# 백준 - 골드5 - 내려가기 - 2096 - dp, 슬라이딩 윈도우 문제
'''
dp, 슬라이딩 윈도우 문제

n_list의 값이 최대 3이여서 직접 비교를 했다.
예전에 풀어본 프로그래머스 문제와 되게 유사해서 해당 방법을 풀었듯이 인덱스 값들로 직접 비교하면서 답을 구했다.
메모리 부분만 조금 하면 될거 같다.

in
    3
    1 2 3
    4 5 6
    4 9 0
out
    18
    6

in
    3
    0 0 0
    0 0 0
    0 0 0
out
    0
    0
'''

n = int(input())
max_dp, min_dp = [0] * 3, [0] * 3
temp_max_dp, temp_min_dp = [0] * 3, [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())

    for j in range(3):
        if j == 0:
            temp_max_dp[j] = a + max(max_dp[j], max_dp[j + 1])
            temp_min_dp[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            temp_max_dp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            temp_min_dp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            temp_max_dp[j] = c + max(max_dp[j - 1], max_dp[j])
            temp_min_dp[j] = c + min(min_dp[j - 1], min_dp[j])

    for k in range(3):
        max_dp[k] = temp_max_dp[k]
        min_dp[k] = temp_min_dp[k]

print(max(max_dp), min(min_dp))

'''
메모리 초과 코드
n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 3
# board = [[1,2,3], [4,5,6], [4,9,0]] # 18  \  6
# n = 3
# board = [[0,0,0], [0,0,0], [0,0,0]] # 0  \  0

max_dp, min_dp = [0] * 3, [0] * 3
temp_max_dp, temp_min_dp = [0] * 3, [0] * 3

for i in range(n):
    for j in range(3):
        board_val = board[i][j]

        if j == 0:
            temp_max_dp[j] = board_val + max(max_dp[j], max_dp[j + 1])
            temp_min_dp[j] = board_val + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            temp_max_dp[j] = board_val + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            temp_min_dp[j] = board_val + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            temp_max_dp[j] = board_val + max(max_dp[j - 1], max_dp[j])
            temp_min_dp[j] = board_val + min(min_dp[j - 1], min_dp[j])

    for k in range(3):
        max_dp[k] = temp_max_dp[k]
        min_dp[k] = temp_min_dp[k]

print(max(max_dp), min(min_dp))
'''