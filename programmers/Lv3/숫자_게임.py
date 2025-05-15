# 프로그래머스 - Lv3 - 숫자 게임 - 그리디, 정렬, 이진 탐색 문제
"""
그리디, 정렬, 이진 탐색 문제

[핵심 아이디어]
    1. B팀은 A팀의 출전 순서를 알고 있으므로 최적의 대응 전략을 세울 수 있음
    2. 각 A팀 숫자에 대해 이길 수 있는 가장 작은 B팀 숫자를 선택(자원 절약)
    3. 이길 수 없는 경우에는 가장 작은 B팀 숫자를 소모(최소 손실)

[풀이 과정]
    1. B팀의 숫자들을 오름차순으로 정렬
    2. A팀의 각 숫자에 대해 이진탐색으로 이길 수 있는 가장 작은 B팀 숫자 찾기
    3. 이길 수 있으면 승점 증가 및 해당 B팀 숫자 제거
    4. 이길 수 없으면 가장 작은 B팀 숫자 제거(최소 손실)
"""

def solution(A, B):
    answer = 0

    # B팀의 숫자들을 오름차순으로 정렬
    sorted_B = sorted(B)

    for a in A:
        # a를 이길 수 있는 B팀의 가장 작은 숫자를 이진탐색으로 찾기
        left, right = 0, len(sorted_B) - 1
        position = len(sorted_B)  # 초기값을 리스트 길이로 설정

        while left <= right:
            mid = (left + right) // 2
            if sorted_B[mid] > a:
                position = mid
                right = mid - 1
            else:
                left = mid + 1

        # a를 이길 수 있는 숫자가 있으면 승점 증가 및 해당 숫자 제거
        if position < len(sorted_B):
            answer += 1
            sorted_B.pop(position)
        else:
            # 이길 수 없으면 가장 작은 숫자 제거(어차피 질 경기)
            sorted_B.pop(0)

    return answer

A, B = [5, 1, 3, 7], [2, 2, 6, 8]
print(solution(A, B)) # 3

A, B = [2, 2, 2, 2], [1, 1, 1, 1]
print(solution(A, B)) # 0
