# 백준 - 브론즈1 - Magic Squares - 10177 - 수학, 구현, 사칙연산 문제
"""
수학, 구현, 사칙연산 문제

[핵심 아이디어]
    마방진의 정의에 따라 각 행, 열, 대각선의 합이 모두 같은지 확인

[풀이 과정]
    1. 각 행의 합이 모두 같은지 확인
    2. 각 열의 합이 모두 같은지 확인
    3. 두 대각선의 합이 모두 같은지 확인
    4. 모두 같으면 마방진, 아니면 마방진 아님

in
    4
    3
    2 7 6
    9 5 1
    4 3 8
    2
    14 22
    26 10
    4
    16 2 3 13
    5 11 10 8
    9 7 6 12
    4 14 15 1
    2
    5 5
    5 5
out
    Magic square of size 3
    Not a magic square
    Magic square of size 4
    Magic square of size 2
"""

n = int(input())

def magic_square(m_list):
    n = len(m_list)
    magic_sum = sum(m_list[0])

    # 행 검사
    for row in m_list:
        if sum(row) != magic_sum:
            return False

    # 열 검사
    for col in range(n):
        if sum(m_list[row][col] for row in range(n)) != magic_sum:
            return False

    # 대각선 검사
    if sum(m_list[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(m_list[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False

    return True

for _ in range(n):
    m = int(input())
    m_list = [list(map(int, input().split())) for _ in range(m)]

    if magic_square(m_list):
        print("Magic square of size {}".format(m))
    else:
        print("Not a magic square")
