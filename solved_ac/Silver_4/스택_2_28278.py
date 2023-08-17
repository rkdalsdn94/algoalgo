# 백준 - 실버4 - 스택 2 - 28278 - 자료 구조(스택) 문제
'''
자료 구조(스택) 문제

단순하게 스택을 구현하면 되는 문제이다.

in
    9
    4
    1 3
    1 5
    3
    2
    5
    2
    2
    5
out
    1
    2
    5
    3
    3
    -1
    -1
'''

import sys; input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] == 1:
        stack.append(a[1])
    elif a[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a[0] == 3:
        print(len(stack))
    elif a[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif a[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
