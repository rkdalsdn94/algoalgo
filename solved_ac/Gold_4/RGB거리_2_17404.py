# 백준 - 골드4 - RGB거리 2 - 17404 - dp 문제
'''
dp 문제

주의해야 될 부분으론 다음과 같다.
    - 첫 번째 집과 마지막 집의 색이 같을 수 없다.
    - 이를 위해, 첫 번째 집을 각각 빨강, 초록, 파랑으로 칠하는 경우를 따로 계산해야 된다.

풀이 과정
    1. 입력 받기
    2. dp를 2차원 리스트로 만들어 첫 번째 집을 각각 빨강, 초록, 파랑으로 칠하는 경우를 따로 계산한다.
        2.1. dp의 첫 번째 행을 입력 받은 첫 번째 집의 색으로 초기화한다.
        2.2. 두 번째 집부터 마지막 집까지 반복문을 돌면서 dp를 채운다.
        2.3. dp의 마지막 행에서 최솟값을 구한다.
    3. dp의 마지막 행에서 최솟값을 구한다.
        3.1. 첫 번째 집과 마지막 집의 색이 같을 수 없기 때문에 사용했던 색을 INF로 바꾼다.
    4. 결과 출력
'''

# n = int(input())
# n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 3
# n_list = [
#     [26, 40, 83], [49, 60, 57], [13, 89, 99]
# ] # 110
# n = 3
# n_list = [
#     [1, 100, 100], [100, 1, 100], [100, 100, 1]
# ] # 3
# n = 3
# n_list = [
#     [1, 100, 100], [100, 100, 100], [1, 100, 100]
# ] # 201
# n = 6
# n_list = [
#     [30, 19, 5], [64, 77, 64], [15, 19, 97],
#     [4, 71, 57], [90, 86, 84], [93, 32, 91]
# ] # 208
# n = 8
# n_list = [
#     [71, 39, 44], [32, 83, 55], [51, 37, 63],
#     [89, 29, 100], [83, 58, 11], [65, 13, 15],
#     [47, 25, 29], [60, 66, 19]
# ] # 253

INF = int(1e9)
res = INF
for i in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][i] = n_list[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + n_list[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + n_list[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + n_list[j][2]

    dp[-1][i] = INF
    res = min(res, min(dp[-1]))

print(res)
