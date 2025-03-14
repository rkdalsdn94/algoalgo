# 프로그래머스 - Lv2 - 귤 고르기 - 해시, 그리디, 정렬 문제
"""
해시, 그리디, 정렬 문제

[핵심 아이디어]
    1. 각 크기별 귤의 개수를 해시맵(딕셔너리)으로 카운팅
    2. 개수가 많은 크기의 귤부터 선택하여 종류의 수를 최소화
    3. 필요한 개수(k)를 채울 때까지 크기별로 선택

[풀이 과정]
    1. 딕셔너리를 사용하여 각 크기별 귤의 개수를 카운팅
    2. 개수를 기준으로 내림차순 정렬하여 가장 많은 개수의 귤부터 선택
    3. 선택한 귤의 총 개수가 k 이상이 될 때까지 서로 다른 크기의 귤을 하나씩 추가
    4. 선택한 크기의 종류 수(answer) 반환
"""

def solution(k, tangerine):
    answer = 0
    size_counts = {}
    selected_count = 0

    for size in tangerine:
        if size in size_counts:
            size_counts[size] += 1
        else:
            size_counts[size] = 1

    # 개수 기준 내림차순 정렬 후 선택
    for size, count in sorted(size_counts.items(), key=lambda x: x[1], reverse=True):
        selected_count += count
        answer += 1

        # 필요한 개수를 채웠으면 종료
        if selected_count >= k:
            break

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]) == 3)
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]) == 2)
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]) == 1)
