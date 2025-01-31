# 백준 - 실버5 - 자동차 주차 - 30993 - 수학, 조합론 문제
'''
수학, 조합론 문제

[핵심 아이디어]
    이 문제는 중복이 있는 순열(Permutation with repetition) 문제입니다.
    N개의 주차 공간에 서로 다른 색상의 자동차를 배치하되, 같은 색상의 자동차는
    서로 구별하지 않습니다. 따라서 전체 순열을 구한 후, 각 색상별 중복되는
    경우의 수로 나누어 주어야 합니다.

    계산 공식: N! / (A! * B! * C!)
    - N!: 전체 주차 공간에 대한 순열
    - A!, B!, C!: 각 색상별 자동차의 중복 순열

[풀이 과정]
    1. 입력값 처리
       - N(전체 주차 공간), A(빨간 자동차), B(초록 자동차), C(파란 자동차) 입력

    2. factorial 함수 구현
       - 재귀를 사용하여 팩토리얼 값을 계산
       - 0과 1의 경우 1을 반환하는 기저 조건 처리

    3. solve_parking 함수 구현
       - N!을 계산하여 전체 순열 구함
       - A!, B!, C!를 각각 계산하여 중복되는 경우의 수 처리
       - 최종 결과 반환: N! / (A! * B! * C!)
'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def solve_parking(N, A, B, C):
    # 전체 순열을 구한 후, 같은 색상의 자동차 수의 팩토리얼로 나눔
    total = factorial(N)
    result = total // (factorial(A) * factorial(B) * factorial(C))
    return result

N, A, B, C = map(int, input().split())

# 테스트
# N, A, B, C = 7, 2, 2, 3 # 210
# N, A, B, C = 8, 1, 2, 5 # 168

print(solve_parking(N, A, B, C))
