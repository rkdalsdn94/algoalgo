# 프로그래머스 - Lv2 - 우박수열 정적분 - 구현, 수학 문제
"""
구현, 수학 문제

[핵심 아이디어]
    1. 우박수열(콜라츠 추측)을 생성하여 좌표 리스트로 변환
    2. 주어진 범위를 실제 좌표 인덱스로 변환 (음수 처리 포함)
    3. 사다리꼴 공식을 이용해 각 구간의 면적을 계산하여 정적분 수행

[풀이 과정]
    1. 초항 k부터 1까지 우박수열을 생성하고 각 값을 (인덱스, 값) 좌표로 저장
    2. 각 범위 [a, b]에 대해:
       - b가 음수면 실제 끝점은 (전체길이 - 1) + b로 계산
       - 시작점이 끝점보다 크거나 범위를 벗어나면 -1 반환
       - 유효한 구간에서는 연속된 두 점 사이의 사다리꼴 면적을 모두 합산
    3. 사다리꼴 면적 공식: (y1 + y2) * (x2 - x1) / 2
"""

def solution(k, ranges):
    answer = []

    # 1. 우박수열 생성
    sequence = []
    current = k
    while True:
        sequence.append(current)
        if current == 1:
            break
        if current % 2 == 0:
            current = current // 2
        else:
            current = current * 3 + 1

    n = len(sequence) - 1  # 마지막 인덱스

    # 2. 각 범위에 대해 정적분 계산
    for a, b in ranges:
        # 실제 끝점 계산 (b가 음수인 경우 처리)
        end = n + b
        start = a

        # 유효성 검사
        if start > end or start < 0 or end > n:
            answer.append(-1.0)
            continue

        # 3. 사다리꼴 면적 합계 계산
        area = 0.0
        for i in range(start, end):
            # 두 점 (i, sequence[i]), (i+1, sequence[i+1]) 사이의 사다리꼴 면적
            y1, y2 = sequence[i], sequence[i + 1]
            width = 1  # x축 간격은 항상 1
            area += (y1 + y2) * width / 2

        answer.append(area)

    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))  # [33.0, 31.5, 0.0, -1.0]
print(solution(3, [[0,0], [1,-2], [3,-3]]))       # [47.0, 36.0, 12.0]
