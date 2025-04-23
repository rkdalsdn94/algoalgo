# 프로그래머스 - Lv2 - 테이블 해시 함수 - 정렬, 해시, 구현 문제
"""
정렬, 해시, 구현 문제

[핵심 아이디어]
    1. 주어진 조건대로 테이블을 정렬한다 (col번째 컬럼 기준 오름차순, 같으면 첫 번째 컬럼 기준 내림차순)
    2. row_begin부터 row_end까지 각 행(i)에 대해 S_i값을 계산한다 (각 원소를 i로 나눈 나머지의 합)
    3. 계산된 S_i값들에 대해 비트 XOR 연산을 누적해서 수행한다

[풀이 과정]
    1. col-1번째와 0번째 컬럼을 기준으로 데이터를 정렬한다 (col-1은 오름차순, 0은 내림차순)
    2. row_begin부터 row_end까지 순회하면서:
       a. 각 행의 원소들을 현재 인덱스(i)로 나눈 나머지를 구한다
       b. 나머지들의 합을 계산하여 S_i를 구한다
    3. 모든 S_i값에 대해 누적 XOR 연산을 수행하여 최종 해시값을 반환한다
"""

def solution(data, col, row_begin, row_end):
    # col은 1부터 시작하므로 인덱스로 변환
    col_idx = col - 1

    # 정렬 조건: col번째 컬럼 오름차순, 같으면 첫 번째 컬럼 내림차순
    sorted_data = sorted(data, key=lambda x: (x[col_idx], -x[0]))

    # 해시값 계산
    hash_value = 0

    # row_begin부터 row_end까지 순회
    for i in range(row_begin, row_end + 1):
        # 인덱스는 0부터 시작하므로 i-1로 접근
        row = sorted_data[i-1]

        # S_i 계산: 현재 행의 모든 원소를 i로 나눈 나머지의 합
        s_i = sum(value % i for value in row)

        # XOR 연산 누적
        hash_value ^= s_i

    return hash_value

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))  # 4
