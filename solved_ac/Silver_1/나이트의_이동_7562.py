# 백준 - 나이트의 이동 - 실버1 - 7562 - bfs 문제
'''
bfs 문제

기본적인 bfs 문제이다.
문제에 나온 그림을 보고 나이트의 이동 경로(dx, dy)를 파악한 후
출발 지점(now_x, now_y)의 x, y 좌표와 도착 지점(end_x, end_y)의 x, y를 입력 받는다.
체스판의 크기 만큼(l * l) 체스판을 벗어났는지 확인하기 위한 ck를 만든 후에,
출발 지점과 몇 번 이동했는지 확인하기 위한 res를 기본 값을 0인 상태로 q에 넣는다.
q가 빌 때까지 반복하면서 도착 지점과 같아졌을 때 res를 출력하면 된다.
현재 문제에선 없었지만 만약, 도착할 수 없는 조건이 있었다면 q가 빌 때까지 다 돌아도 완료를 못하면 해당하는 조건을 출력하면 된다.

원래는 while q: 하는 부분을 따로 함수로 만드는데, 현재 문제는 좀 간단해서 바로 구현했다.

in
    3
    8
    0 0
    7 0
    100
    0 0
    30 50
    10
    1 1
    1 1
out
    5
    28
    0
'''

from collections import deque

t = int(input())

dx, dy = [-2, -2, 2, 2, -1, 1,-1, 1], [-1, 1,-1, 1, -2, -2, 2, 2] # 나이트의 이동 범위

for _ in range(t):
    l = int(input())
    now_x, now_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    ck = [ [0] * l for _ in range(l) ]

    q = deque([(now_x, now_y, 0)])

    while q:
        a, b, res = q.popleft()

        if a == end_x and b == end_y:
            print(res)
            break

        for i, j in zip(dx, dy):
            nx, ny = i + a, b + j

            if 0 <= nx < l and 0 <= ny < l and ck[nx][ny] == 0:
                ck[nx][ny] = 1
                q.append([nx, ny, res + 1])
