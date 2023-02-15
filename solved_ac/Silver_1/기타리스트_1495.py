# 백준 - 기타리스트 - 실버1 - 1495 - dp 문제
'''
dp 문제

n = 곡의 개수
s = 시작 볼륨
m = 볼륨의 최댓값

dp 배열을 0으로 초기화한 m + 1 과 n + 1의 범위로 만들어준다.
처음 스타트 부분을 2 중으로 된 dp 배열에서 0번재 s를 1로 바꾼 후 해당 값이 1이면 n_list의 값을 1로 바꾸면서 구하면 된다.
출력할 땐 dp 마지막 배열에서 역순으로 돌면서 1이 되어 있으면 해당 부분을 출력하고 종료하고, 1이 없으면 마지막 곡을 연주하지 못한 경우라서 -1을 출력하면 된다.
'''

n, s, m = map(int, input().split())
n_list = list(map(int, input().split()))

# 테스트
# n, s, m = 3, 5, 10
# n_list = [5, 3, 7] # 10
# n, s, m = 4, 8, 20
# n_list = [15, 2, 9, 10] # -1
# n, s, m = 14, 40, 243
# n_list = [74, 39, 127, 95, 63, 140, 99, 96, 154, 18, 137, 162, 14, 88] # 238

dp = [ [0] * (m + 1) for _ in range(n + 1) ]
dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == 1:
            if n_list[i] + j <= m:
                dp[i + 1][j + n_list[i]] = 1
            if j - n_list[i] >= 0:
                dp[i + 1][j - n_list[i]] = 1

for i in range(m, -1, -1):
    if dp[n][i] == 1:
        print(i)
        exit(0)
print(-1)
