# 프로그래머스 - Lv3 - 보석 쇼핑 - 투 포인터, 슬라이딩 윈도우 문제
"""
투 포인터, 슬라이딩 윈도우 문제

[핵심 아이디어]
    1. 투 포인터 기법으로 윈도우를 확장하고 축소하며 최적 구간을 찾는다.
    2. 해시맵으로 각 보석의 개수를 관리하여 모든 종류의 보석이 포함되었는지 빠르게 확인한다.
    3. 윈도우가 모든 보석을 포함하면 왼쪽 포인터를 이동하여 최소 길이를 찾고,
       포함하지 않으면 오른쪽 포인터를 이동하여 윈도우를 확장한다.

[풀이 과정]
    1. 전체 보석 종류 개수를 계산하여 목표 조건을 설정한다.
    2. 오른쪽 포인터(right)로 윈도우를 확장하며 새로운 보석을 추가한다.
    3. 현재 윈도우가 모든 종류의 보석을 포함하면:
       a. 현재 길이가 최소 길이보다 짧으면 결과를 업데이트한다.
       b. 왼쪽 포인터(left)를 이동하여 윈도우를 축소하며 더 짧은 구간을 탐색한다.
    4. 모든 구간을 탐색 완료 후 최소 길이의 구간을 반환한다.
"""

def solution(gems):
    gem_types = len(set(gems))
    gem_count = {}
    left = 0
    min_length = len(gems)
    answer = [1, len(gems)]

    for right in range(len(gems)):
        # 오른쪽 포인터로 윈도우 확장
        gem_count[gems[right]] = gem_count.get(gems[right], 0) + 1

        # 모든 보석을 포함했다면 왼쪽 포인터로 윈도우 축소
        while len(gem_count) == gem_types:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                answer = [left + 1, right + 1]  # 1-based 인덱스

            gem_count[gems[left]] -= 1
            if gem_count[gems[left]] == 0:
                del gem_count[gems[left]]
            left += 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) # [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) #  [1, 5]
