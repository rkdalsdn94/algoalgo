# 프로그래머스 - Lv2 - n^2 배열 자르기 - 수학, 구현 문제
"""
수학, 구현 문제

[핵심 아이디어]
    1. n x n 배열의 각 위치 (row, col)의 값은 max(row, col) + 1임을 파악
    2. 2차원 배열을 실제로 생성하지 않고, 인덱스 변환을 통해 직접 값 계산
    3. 1차원 인덱스를 행과 열로 변환하는 공식: row = i // n, col = i % n

[풀이 과정]
    1. left부터 right까지의 각 인덱스 i에 대해:
       - 2차원 배열에서의 행(row)과 열(col) 계산: row = i // n, col = i % n
       - 해당 위치의 값 계산: max(row, col) + 1
       - 계산된 값을 결과 배열에 추가
    2. 최종 결과 배열 반환
"""

def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        row, col = i // n, i % n
        answer.append(max(row, col) + 1)

    return answer

print(solution(3, 2, 5) == [3, 2, 2, 3])
print(solution(4, 7, 14) == [4, 3, 3, 3, 4, 4, 4, 4])
