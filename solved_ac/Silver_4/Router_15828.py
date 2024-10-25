# 백준 - 실버4 - Router - 15828 - 자료 구조, 큐 문제
'''
자료 구조, 큐 문제

풀이 과정
    1. n을 입력받는다.
    2. q를 deque로 선언한다.
    3. r을 입력받는다.
    4. r이 -1이면 종료한다.
    5. r이 0이면 q의 첫 번째 원소를 삭제한다.
    6. q의 길이가 n보다 작으면 q에 r을 추가한다.
    7. r을 입력받는다.
    8. r이 -1이면 종료한다.
    9. q가 비어있으면 empty를 출력하고, q가 비어있지 않으면 q를 출력한다.

in
    5
    1
    2
    0
    3
    4
    0
    5
    6
    0
    0
    -1
out
    5 6

in
    1
    1
    2
    3
    4
    5
    6
    7
    -1
out
    1

in
    1
    1
    2
    0
    3
    4
    0
    5
    6
    0
    7
    0
    -1
out
    empty
'''

import sys; input=sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
r = int(input())

while r != -1:
    if r == 0:
        q.popleft()
    else:
        if len(q) < n:
            q.append(r)

    r = int(input())

if q:
    print(*q)
else:
    print("empty")
