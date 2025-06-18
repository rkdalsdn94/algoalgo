# 프로그래머스 - Lv2 - 점 찍기 - 수학, 구현 문제
"""
수학, 구현 문제

[핵심 아이디어]
    1. 원점과의 거리 조건을 수식으로 변형: a² + b² ≤ (d/k)²
    2. a값을 고정하고 조건을 만족하는 b의 최대값을 계산
    3. 각 a에 대해 가능한 b의 개수를 누적하여 총 점의 개수 구하기

[풀이 과정]
    1. a를 0부터 d//k까지 반복 (a×k가 d를 넘지 않는 범위)
    2. 각 a에 대해 거리 조건 (a×k)² + (b×k)² ≤ d²를 만족하는 b의 최대값 계산
    3. b는 0부터 시작하므로 가능한 b의 개수는 (최대 b값 + 1)개
    4. 모든 a에 대한 b의 개수를 합산하여 총 점의 개수 반환
"""

import math

def solution(k, d):
    count = 0

    # a*k가 d를 넘지 않는 범위에서 반복
    for a in range(d // k + 1):
        # (a*k)^2 + (b*k)^2 <= d^2를 만족하는 b의 최대값 계산
        max_b_squared = d * d - (a * k) * (a * k)

        if max_b_squared >= 0:
            # b*k <= sqrt(max_b_squared)이므로 b <= sqrt(max_b_squared) / k
            max_b = int(math.sqrt(max_b_squared)) // k
            count += max_b + 1  # b=0부터 max_b까지의 개수

    return count
