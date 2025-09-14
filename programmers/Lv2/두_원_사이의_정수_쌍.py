# 프로그래머스 - Lv2 - 두 원 사이의 정수 쌍 - 수학 문제
"""
수학 문제

[핵심 아이디어]
    반지름 r인 원 내부의 정수점 개수를 구하는 함수를 만들고, 큰 원의 정수점 개수에서 작은 원 내부(경계 제외)의 정수점 개수를 빼는 것.
    대칭성을 활용하여 계산량을 최적화해야 함

[풀이 과정]
    1. x² + y² ≤ bound인 정수점 개수를 구하는 함수 countPointsBound(bound) 구현
    2. x좌표가 변할 때, 각 x에 대해 y의 범위는 -√(bound-x²) ≤ y ≤ √(bound-x²)
    3. 따라서 각 x에 대해 가능한 y값의 개수는 2 * floor(√(bound-x²)) + 1개
    4. 최종 답은 countPointsBound(r2²) - countPointsBound(r1² - 1)
       (r1² ≤ x² + y² ≤ r2² 조건을 만족하는 점들을 구하기 위함)
"""

import math

def solution(r1, r2):
    """x² + y² ≤ bound인 정수점 개수를 반환"""
    def countPointsBound(bound):
        if bound < 0:
            return 0
        count = 0
        max_x = int(math.sqrt(bound))

        for x in range(-max_x, max_x + 1):
            if x * x <= bound:
                max_y = int(math.sqrt(bound - x * x))
                count += 2 * max_y + 1
        return count

    # 큰 원 내부의 점들에서 작은 원 내부(경계 제외)의 점들을 뺌
    return countPointsBound(r2 * r2) - countPointsBound(r1 * r1 - 1)

print(solution(2, 3) == 20)
