# 백준 - 실버4 - 덱 2 - 28279 - 자료 구조(덱) 문제
'''
자료 구조(덱) 문제

collections 모듈 안에 있는 deque를 이용해서 풀었다.
다음의 명령을 구현하면 된다. (덱을 구현하면 됨)
    1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
    2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
    3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    5: 덱에 들어있는 정수의 개수를 출력한다.
    6: 덱이 비어있으면 1, 아니면 0을 출력한다.
    7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.

in
    11
    6
    1 3
    1 8
    7
    8
    3
    2 5
    1 2
    5
    4
    4
out
    1
    8
    3
    8
    3
    5
    3
'''

from collections import deque
import sys; input=sys.stdin.readline

n = int(input())
deq = deque()

for _ in range(n):
    command = list(map(int, input().split()))

    if command[0] == 1:
        deq.appendleft(command[1])
    elif command[0] == 2:
        deq.append(command[1])
    elif command[0] == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == 5:
        print(len(deq))
    elif command[0] == 6:
        if deq:
            print(0)
        else:
            print(1)
    elif command[0] == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif command[0] == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)
