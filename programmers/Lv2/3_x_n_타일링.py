# 프로그래머스 - Lv2 - 3 x n 타일링 - dp 문제
"""
dp 문제

[핵심 아이디어]
    1. 가로 길이가 n인 3 x n 직사각형을 채우는 방법의 수를 구하는 점화식 도출
    2. 홀수 가로 길이는 채울 수 없음을 이해 (2x1 타일로는 홀수 너비를 채울 수 없음)
    3. 3xn 직사각형은 3x2 크기의 패턴과 특별한 모양의 패턴들로 분할 가능
    4. 점화식: dp[n] = dp[n-2] * 3 + dp[n-4] * 2 + dp[n-6] * 2 + ... + dp[0] * 2
    5. 위 점화식을 효율적으로 계산하기 위해 누적합을 활용

[풀이 과정]
    1. 초기값 설정: dp[0] = 1, dp[2] = 3 (홀수 인덱스는 항상 0)
    2. 누적합 변수를 사용하여 O(n) 시간 복잡도로 계산
    3. 상향식(bottom-up) 방식으로 dp 배열 채우기
    4. 모듈로 연산을 사용하여 큰 수 처리
"""

def solution(n):
    # 홀수인 경우 채울 수 없음
    if n % 2 == 1:
        return 0

    # n이 0인 경우 처리
    if n == 0:
        return 1

    MOD = 1_000_000_007
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3

    # 누적합 변수 초기화 (dp[0]의 2배, 특별한 패턴의 합)
    cumulative = dp[0] * 2

    # n=4부터 점화식 적용 (n은 짝수만 고려)
    for i in range(4, n + 1, 2):
        # 기본 패턴 + 특별한 패턴들의 누적합
        dp[i] = (dp[i-2] * 3 + cumulative) % MOD

        # 누적합 갱신 (특별한 패턴들의 합)
        cumulative = (cumulative + dp[i-2] * 2) % MOD

    return dp[n]

print(solution(4))  # 11
