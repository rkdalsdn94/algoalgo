# 프로그래머스 - Lv2 - 시소 짝꿍 - 자료구조(해시), 수학, 조합 문제
"""
자료구조(해시), 수학, 조합 문제

[핵심 아이디어]
    1. 두 사람이 시소 짝꿍이 되려면 (무게 × 거리)가 같아야 함
    2. 가능한 거리 조합은 (2,2), (2,3), (2,4), (3,3), (3,4), (4,4)
    3. 이를 무게 비율로 변환하면 1:1, 2:3, 1:2, 1:1, 3:4, 1:1
    4. 중복을 제거하면 1:1, 2:3, 1:2, 3:4 네 가지 비율만 확인하면 됨
    5. 각 무게의 등장 횟수를 기록하여 O(n) 시간 복잡도로 해결

[풀이 과정]
    1. 각 무게별 등장 횟수를 딕셔너리에 저장
    2. 같은 무게를 가진 사람들 중 2명을 선택하는 경우의 수 계산 (nC2)
    3. 서로 다른 무게를 가진 사람들 중 가능한 비율(1:2, 2:3, 3:4)에 해당하는 쌍 계산
    4. 모든 경우의 수를 합산하여 반환
"""

from collections import Counter

def solution(weights):
    answer = 0
    weight_counter = Counter(weights)

    # 같은 무게인 경우 (1:1 비율)
    for weight, count in weight_counter.items():
        # 같은 무게인 사람 중 2명을 선택하는 경우의 수: nC2 = n*(n-1)/2
        if count >= 2:
            answer += count * (count - 1) // 2

    # 서로 다른 무게인 경우, 가능한 비율 검사
    # 가능한 비율: 1:2, 2:3, 3:4 (또는 역으로 2:1, 3:2, 4:3)
    for weight in weight_counter:
        # 비율 1:2 확인 (2m와 4m 위치)
        if weight * 2 in weight_counter:
            answer += weight_counter[weight] * weight_counter[weight * 2]

        # 비율 2:3 확인 (2m와 3m 위치)
        if weight * 3 % 2 == 0 and weight * 3 // 2 in weight_counter:
            answer += weight_counter[weight] * weight_counter[weight * 3 // 2]

        # 비율 3:4 확인 (3m와 4m 위치)
        if weight * 4 % 3 == 0 and weight * 4 // 3 in weight_counter:
            answer += weight_counter[weight] * weight_counter[weight * 4 // 3]

    return answer

print(solution([100, 180, 360, 100, 270]))  # 4
