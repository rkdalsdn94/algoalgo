# 프로그래머스 - Lv2 - 연속 부분 수열 합의 개수 - 구현, 자료구조(집합)
"""
구현, 자료구조(집합)

[핵심 아이디어]
    1. 원형 수열의 모든 연속 부분 수열을 고려하기 위해 원래 배열을 두 배로 확장
    2. 각 길이별로 가능한 모든 연속 부분 수열의 합을 계산
    3. 중복을 제거하기 위해 집합(set) 자료구조 활용
    4. 불필요한 계산을 줄이기 위해 길이별 반복 범위 최적화

[풀이 과정]
    1. 원형 수열의 모든 부분 수열을 고려하기 위해 배열을 두 배로 늘림(elements * 2)
    2. 가능한 모든 부분 수열의 길이(1부터 원래 배열의 길이까지)에 대해:
       - 해당 길이의 부분 수열을 원래 배열의 길이만큼만 탐색 (시작점은 0부터 len(elements)-1까지)
       - 각 부분 수열의 합을 계산하여 집합에 추가
    3. 최종적으로 중복이 제거된 집합의 크기를 반환
"""

def solution(elements):
    n = len(elements)
    answer = set()

    # 원형 수열을 표현하기 위해 배열을 두 배로 확장
    extended_elements = elements * 2

    # 각 길이별 부분 수열의 합 계산
    for length in range(1, n + 1):
        # 원래 배열의 길이만큼만 시작점을 고려하면 모든 경우를 커버할 수 있음
        for start in range(n):
            # 현재 시작점과 길이에 해당하는 부분 수열의 합 계산
            subsequence_sum = sum(extended_elements[start:start + length])
            answer.add(subsequence_sum)

    return len(answer)

print(solution([7, 9, 1, 1, 4]) == 18)
