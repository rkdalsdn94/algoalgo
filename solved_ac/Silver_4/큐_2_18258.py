'''
단순 구현, 자료 구조, 큐 문제

문제에 주어진 조건을 구현만 하면 된다. 연산 속도를 위해 deque 자료 구조를 활용했다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

in
    15
    push 1
    push 2
    front
    back
    size
    empty
    pop
    pop
    pop
    size
    empty
    pop
    push 3
    empty
    front
out
    1
    2
    2
    0
    1
    2
    -1
    0
    1
    -1
    0
    3
'''

import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
res = deque()

for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        res.append(int(command[1]))
    
    elif command[0] == 'pop':
        if res:
            print(res.popleft())
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(res))
    
    elif command[0] == 'empty':
        if res:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if res:
            print(res[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if res:
            print(res[-1])
        else:
            print(-1)
