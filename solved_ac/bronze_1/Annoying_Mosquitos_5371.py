# 백준 - 브론즈1 - Annoying Mosquitos - 5371 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

완전 탐색 방식으로 구현하면 되는 문제이다.
input을 sys.stdin.readline으로 받거나, PyPy3로 제출해야 된다.

풀이 과정
    1. 테스트 케이스(t)를 입력받고, 테스트 케이스(t)만큼의 반복문을 돌린다.
    2. n을 입력받는다.
    3. n개의 모기의 위치를 입력받는다.
    4. m을 입력받는다.
    5. m개의 Lee가 스왓한 중간점의 위치를 입력받는다.
    6. visit을 0으로 초기화한다.
    7. res를 0으로 초기화한다.
    8. m_list를 순회하며 n_list에 있는 모기의 위치와 비교한다.
    9. 모기의 위치가 50 이내이면 visit을 1로 변경하고 res에 1을 더한다.
    10. res를 출력한다.

in
    2
    3
    15 -10
    16 40
    17 41
    1
    15 -10
    1
    100 100
    3
    90 90
    100 110
    -500 -400
out
    2
    1
'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    n_list = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    m_list = [tuple(map(int, input().split())) for _ in range(m)]

    visit = [0] * n
    res = 0

    for i, j in m_list:
        for k in range(n):
            if visit[k]:
                continue

            x, y = n_list[k]
            if i - 50 <= x <= i + 50 and j - 50 <= y <= j + 50:
                visit[k] = 1
                res += 1

    print(res)
