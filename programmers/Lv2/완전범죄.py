# 프로그래머스 - Lv2 - 완전범죄 - dp 문제
"""
dp 문제

[핵심 아이디어]
    1. 두 명의 도둑 A, B가 물건을 훔치는 상황에서 DP를 활용
    2. dp[i][j] = i번째 물건까지 고려했을 때, B도둑이 j만큼 훔쳤을 때 A도둑이 훔친 최소량
    3. 각 물건에 대해 A도둑이 훔치거나 B도둑이 훔치는 두 가지 선택지 고려
    4. B도둑이 훔친 양이 m 미만이어야 하는 제약 조건 존재

[풀이 과정]
    1. DP 테이블 초기화 - dp[i][j]를 n(최대값)으로 초기화, dp[0][0] = 0
    2. 각 물건에 대해 다음 두 가지 경우를 고려
       a. A도둑이 해당 물건을 훔치는 경우: dp[i][j] = min(dp[i][j], dp[i-1][j] + a)
       b. B도둑이 해당 물건을 훔치는 경우: dp[i][j+b] = min(dp[i][j+b], dp[i-1][j])
    3. 모든 물건을 고려한 후, B도둑이 훔친 양이 m 미만인 경우들 중 A도둑이 훔친 최소량 반환
    4. 조건을 만족하는 경우가 없으면 -1 반환
"""

def solution(info, n, m):
    # DP 테이블 초기화
    dp = [[n] * m for _ in range(len(info) + 1)]
    dp[0][0] = 0

    for i in range(1, len(info) + 1):
        a = info[i - 1][0]  # A도둑이 훔치는 양
        b = info[i - 1][1]  # B도둑이 훔치는 양

        for j in range(m):
            # A도둑이 물건을 훔치는 경우
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + a)

            # B도둑이 물건을 훔치는 경우
            if j + b < m:
                dp[i][j + b] = min(dp[i][j + b], dp[i - 1][j])

    answer = n
    for j in range(m):
        answer = min(answer, dp[len(info)][j])

    return -1 if answer >= n else answer

print(solution([[1, 2], [2, 3], [2, 1]], 4, 4)) # 2
print(solution([[1, 2], [2, 3], [2, 1]], 1, 7)) # 0
print(solution([[3, 3], [3, 3]], 7, 1)) # 6
print(solution([[3, 3], [3, 3]], 6, 1)) # -1
