'''
구현, 완전 탐색 문제

bfs 풀던 방식을 좀 응용해서 문제를 풀었다.
'o'가 입력되는 순간 q에 담은 후, while 반복문으로 q가 빌 때까지 하나씩 꺼낸다.
그리고 수직(vertical)으로 움직일 때, 수평(horizontal)으로 움직일 때를 각각 검사했다.

검사하는 방식은 수직일 땐 각 좌표값이 (-1, 0)을 한 후에 (1, 0)으로 진행했다.
(-1, 0)을 했을 때 'v'이 값이 맞으면 vertical_temp의 값을 + 1 하고,
(1, 0)을 검사할 때 해당 candy_factory의 값이 '^'이고, vertical_temp의 값이 1이면 res에 1을 더한다.

수평일 땐 수직이랑 똑같이 하면서 (0, -1), (0, 1)로 좌표값만 바꾸면 된다.
'''

from collections import deque


t = int(input())

for _ in range(t):
    input()
    r, c = map(int, input().split())
    candy_factory = [ list(input()) for _ in range(r) ]

    # r, c = 5, 4
    # candy_factory = [['.','>','o','<'],
    # ['v','.','^','.'],
    # ['o','o','o','.'],
    # ['^','.','^','.'],
    # ['>','o','<','<']] # 3

    q = deque()
    res = 0
    vertical_dx, vertical_dy = [-1, 1], [0, 0]
    horizontal_dx, horizontal_dy = [0, 0], [-1, 1]
    flag = False

    for i in range(r):
        for j in range(c):
            if candy_factory[i][j] == 'o':
                q.append([i, j])

    while q:
        x, y = q.popleft()
        vertical_temp = 0
        horizontal_temp = 0

        for a, b, aa, bb in zip(vertical_dx, vertical_dy, horizontal_dx, horizontal_dy):
            a_nx, b_ny = x + a, y + b
            aa_nx, bb_ny = x + aa, y + bb

            if 0 <= a_nx < r and 0 <= b_ny < c:
                if candy_factory[a_nx][b_ny] == 'v':
                    vertical_temp += 1

                if vertical_temp == 1 and candy_factory[a_nx][b_ny] == '^':
                    res += 1

            if 0 <= aa_nx < r and 0 <= bb_ny < c:
                if candy_factory[aa_nx][bb_ny] == '>':
                    horizontal_temp += 1

                if horizontal_temp == 1 and candy_factory[aa_nx][bb_ny] == '<':
                    res += 1

    print(res)
