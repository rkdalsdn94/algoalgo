# 백준 - 실버5 - 속도 위반 - 11971 - 구현 문제
'''
구현 문제

풀이 과정
    1. 입력값을 받는다.
    2. 입력값을 리스트에 저장한다.
        2.1. 구간(a)에 맞춰 속도(b)를 저장한다.
    3. 두 리스트의 차이를 계산하여 최대값을 찾는다.
    4. 결과 출력

in
    3 3
    40 75
    50 35
    10 45
    40 76
    20 30
    40 40
out
    5
'''

n, m = map(int, input().split())
n_list, m_list = [], []

for i in range(n):
    a, b = map(int, input().split())

    for j in range(a):
        n_list.append(b)

for i in range(m):
    a, b = map(int, input().split())

    for j in range(a):
        m_list.append(b)

res = 0
for i in range(100):
    res = max(res, m_list[i] - n_list[i])

print(res)
