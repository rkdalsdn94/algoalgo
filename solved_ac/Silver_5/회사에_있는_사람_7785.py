# 백준 - 실버5 - 회사에 있는 사람 - 7785 - 자료 구조(dict) 문제
'''
자료 구조(dict) 문제

구현은 단순한다. n번 반복하면서 입력으로 들어온 2 번째 값이 'enter'면 append, 'leave' 면 pop 하면 된다. 근데,
문제의 분류가 자료 구조인지 인해가 안 됐는데, 처음 코드를 제출한 후 시간 초과를 받아서 어떻게 하면 되지 고민을 해다 해결했다.
dict을 활용하면 시간 초과가 나오지 않는다.

풀이 과정
1. n을 입력 받고, 정답으로 출력할 res 딕셔너리를 만든다.
2. n 만큼 반복하면서 이름(a)과 출근인지 퇴근인지(b) 입력 받는다.
    2.1. b가 출근이면 res에 해당 사람의 이름을 키로 값을 출근했다는 표시인 True를 담는다.
    2.2. b가 퇴근이면 res에 해당 사람의 이름을 키의 값을 삭제한다.
3. res를 역순으로 정렬 후 해당 이름을 출력한다.

in
    4
    Baha enter
    Askar enter
    Baha leave
    Artem enter
out
    Askar
    Artem
'''

n = int(input())
res = dict()

for _ in range(n):
    a, b = input().split()

    if b == 'enter':
        res[a] = True
    else:
        res.pop(a)

for i in sorted(res, reverse=True):
    print(i)

'''
시간 초과 코드
PyPy3와 import sys; input = sys.stdin.readline 을 하면 통과되긴 한다.

import sys; input = sys.stdin.readline

n = int(input())
res = []

for _ in range(n):
    a, b = input().split()

    if b == 'enter':
        res.append(a)
    else:
        res.pop(res.index(a))

for i in sorted(res, reverse=True):
    print(i)
'''