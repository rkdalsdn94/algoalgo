# 프로그래머스 - Lv1 - 과일 장수 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

[핵심 아이디어]
    - 최대 이익을 위해 사과를 점수 기준으로 내림차순 정렬
    - m개씩 묶어 상자를 구성하고, m개를 채우지 못하는 사과는 판매하지 않음
    - 상자 가격 = 상자 내 최소 점수 × m
    - 모든 유효한 상자 가격의 합 = 최대 이익

[풀이 과정]
    1. 사과를 내림차순으로 정렬
    2. m개씩 묶어 상자를 구성
    3. 각 상자의 가격(최소 점수 × m) 계산 후 합산
'''

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    # m개씩 상자 구성 (남는 사과는 버림)
    for i in range(0, len(score) // m * m, m):
        box = score[i:i+m]
        answer += min(box) * m

    return answer

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]) == 8)
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]) == 33)
