# 프로그래머스 - Lv3 - 스티커 모으기 (2) - dp 문제
"""
dp 문제

[핵심 아이디어]
    - 원형 구조: 첫 번째와 마지막 스티커가 인접하므로 동시에 선택 불가
    - 두 가지 경우로 분리
      1) 첫 번째 스티커를 선택 → 마지막 스티커 선택 불가
      2) 첫 번째 스티커를 선택 안 함 → 마지막 스티커 선택 가능
    - 각 경우에 대해 일반적인 dp 적용

[풀이 과정]
    1. 스티커가 1개 또는 2개인 예외 케이스 처리
    2. Case 1: sticker[0] 포함, sticker[n-1] 제외 (0 ~ n-2 범위)
    3. Case 2: sticker[0] 제외, sticker[n-1] 포함 가능 (1 ~ n-1 범위)
    4. 각 케이스마다 DP 배열로 최댓값 계산
       - dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
       - dp[i-1]: i번째 스티커를 선택하지 않는 경우
       - dp[i-2] + sticker[i]: i번째 스티커를 선택하는 경우
    5. 두 케이스의 최댓값 반환
"""

def solution(sticker):
    n = len(sticker)

    # 예외 처리: 스티커가 1개 또는 2개인 경우
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker[0], sticker[1])

    # Case 1: 첫 번째 스티커를 선택 (마지막 스티커 제외)
    dp1 = [0] * n
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])

    for i in range(2, n - 1):  # 마지막 스티커는 제외
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    # Case 2: 첫 번째 스티커를 선택하지 않음 (마지막 스티커 선택 가능)
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2, n):  # 마지막 스티커까지 포함
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    # 두 경우 중 최댓값 반환
    return max(dp1[n - 2], dp2[n - 1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]) == 36)  # 36
print(solution([1, 3, 2, 5, 4]) == 8)  # 8
print(solution([1, 100, 1, 1, 100]))  # 200
