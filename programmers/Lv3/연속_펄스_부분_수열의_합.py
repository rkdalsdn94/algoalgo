# 프로그래머스 - Lv3 - 연속 펄스 부분 수열의 합 - dp, 카데인 알고리즘 문제
"""
dp, 카데인 알고리즘 문제

[핵심 아이디어]
    1. 펄스 수열은 두 가지 패턴이 있다: [1, -1, 1, -1, ...] 와 [-1, 1, -1, 1, ...]
    2. 각 펄스 패턴에 대해 원래 수열과 곱한 새로운 수열을 생성한다.
    3. 카데인 알고리즘을 사용하여 각 수열의 최대 연속 부분 수열의 합을 구한다.
    4. 두 결과 중 더 큰 값을 반환한다.

[풀이 과정]
    1. 두 가지 펄스 패턴([1, -1, ...], [-1, 1, ...])을 적용한 수열을 생성한다.
    2. 각 수열에 대해 카데인 알고리즘을 적용:
       - current_max: 현재 위치까지의 최대 연속 합
       - global_max: 전체에서의 최대 연속 합
    3. 매 위치에서 current_max = max(현재값, current_max + 현재값)으로 갱신
    4. global_max를 지속적으로 업데이트하여 최종 최대값을 구한다.
"""

def solution(sequence):
    n = len(sequence)

    # 카데인 알고리즘을 구현한 함수
    def kadane_algorithm(arr):
        current_max = arr[0]  # 현재 위치까지의 최대 연속 합
        global_max = arr[0]   # 전체에서의 최대 연속 합

        for i in range(1, len(arr)):
            # 현재 원소부터 새로 시작하거나, 이전 합에 현재 원소를 더하거나
            current_max = max(arr[i], current_max + arr[i])
            # 전체 최대값 갱신
            global_max = max(global_max, current_max)

        return global_max

    # 첫 번째 펄스 패턴: [1, -1, 1, -1, ...]
    pulse1 = []
    for i in range(n):
        if i % 2 == 0:
            pulse1.append(sequence[i] * 1)
        else:
            pulse1.append(sequence[i] * -1)

    # 두 번째 펄스 패턴: [-1, 1, -1, 1, ...]
    pulse2 = []
    for i in range(n):
        if i % 2 == 0:
            pulse2.append(sequence[i] * -1)
        else:
            pulse2.append(sequence[i] * 1)

    # 각 펄스 패턴에 대해 최대 연속 부분 수열의 합을 구함
    max1 = kadane_algorithm(pulse1)
    max2 = kadane_algorithm(pulse2)

    # 두 결과 중 더 큰 값을 반환
    return max(max1, max2)

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))  # 10
