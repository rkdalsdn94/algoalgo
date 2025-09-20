# 프로그래머스 - Lv2 - 숫자 블록 - 수학, 시뮬레이션 문제
"""
수학, 시뮬레이션 문제

[핵심 아이디어]
    각 위치 i에서 블록 n이 설치되려면 i = n × k (k ≥ 2)를 만족해야 함.
    즉, n ≤ i/2이면서 1 ≤ n ≤ 10,000,000인 가장 큰 n이 최종 블록 번호

[풀이 과정]
    1. begin부터 end까지 각 위치를 순회
    2. 각 위치 i에 대해 i/2 이하인 약수들을 효율적으로 탐색
    3. 블록 범위(1~10,000,000)에 해당하는 약수들 중 최댓값 선택
    4. 조건을 만족하는 약수가 없으면 0을 저장
"""

def solution(begin, end):
    result = []

    for i in range(begin, end + 1):
        max_block = 0  # 해당 위치의 최종 블록 번호

        # i의 약수를 효율적으로 찾기 (sqrt(i)까지만 탐색)
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:  # j가 i의 약수인 경우

                # j가 조건을 만족하는지 확인 (j ≤ i/2 and 1 ≤ j ≤ 10,000,000)
                if j <= i // 2 and 1 <= j <= 10000000:
                    max_block = max(max_block, j)

                # i//j도 약수이므로 조건 확인
                other_divisor = i // j
                if j != other_divisor and other_divisor <= i // 2 and 1 <= other_divisor <= 10000000:
                    max_block = max(max_block, other_divisor)

        result.append(max_block)

    return result

print(solution(1, 10) == [0, 1, 1, 2, 1, 3, 1, 4, 3, 5])
