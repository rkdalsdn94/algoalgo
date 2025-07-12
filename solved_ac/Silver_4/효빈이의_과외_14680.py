# 백준 - 실버4 - 효빈이의 과외 - 14680 - 수학, 구현 문제
"""
수학, 구현 문제

[핵심 아이디어]
    1. 연속된 행렬 곱셈에서 각 단계마다 차원 호환성을 확인해야 함
    2. A(m×n) * B(p×q) 곱셈이 가능하려면 n == p여야 하고, 결과는 m×q 행렬
    3. 행렬 곱셈을 순차적으로 수행하며, 중간에 곱셈이 불가능하면 즉시 -1 반환
    4. 최종 행렬의 모든 원소 합을 구하고 1,000,000,007로 모듈로 연산

[풀이 과정]
    1. N개의 행렬을 순서대로 입력받아 저장
    2. 첫 번째 행렬을 결과 행렬로 초기화
    3. 두 번째 행렬부터 순차적으로 곱셈 수행:
       - 현재 결과 행렬의 열 수와 다음 행렬의 행 수가 같은지 확인
       - 다르면 -1 출력 후 종료
       - 같으면 행렬 곱셈 수행하여 결과 행렬 업데이트
    4. 모든 곱셈 완료 후 최종 행렬의 원소 합을 구하고 모듈로 연산 적용
"""

def matrix_multiply(A, B):
    """두 행렬 A와 B를 곱하는 함수"""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # 곱셈 불가능한 경우
    if cols_A != rows_B:
        return None

    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

def solve():
    MOD = 1000000007

    n = int(input())
    matrices = []

    # 모든 행렬 입력 받기
    for _ in range(n):
        x, y = map(int, input().split())
        matrix = []
        for i in range(x):
            row = list(map(int, input().split()))
            matrix.append(row)
        matrices.append(matrix)

    # 첫 번째 행렬을 결과로 초기화
    result = matrices[0]

    # 나머지 행렬들과 순차적으로 곱셈
    for i in range(1, n):
        result = matrix_multiply(result, matrices[i])
        if result is None:
            return -1

    # 최종 행렬의 모든 원소 합 계산
    total_sum = 0
    for row in result:
        total_sum += sum(row)

    return total_sum % MOD

print(solve())
