'''
bfs로 풀었다.
입력의 마무리가 언제 될지 몰라서 조건을 달고 반복문을 만들었다.
난이도가 높지 않아서 그런지 쉽게 풀 수 있었다.
in
    1 1
    0
    2 2
    0 1
    1 0
    3 2
    1 1 1
    1 1 1
    5 4
    1 0 1 0 0
    1 0 0 0 0
    1 0 1 0 1
    1 0 0 1 0
    5 4
    1 1 1 0 1
    1 0 1 0 1
    1 0 1 0 1
    1 0 1 1 1
    5 5
    1 0 1 0 1
    0 0 0 0 0
    1 0 1 0 1
    0 0 0 0 0
    1 0 1 0 1
    0 0
out
    0
    1
    1
    3
    1
    9
'''

from collections import deque

w, h = map(int, input().split())

while w != 0 and h != 0:
    land = [ list(map(int, input().split())) for _ in range(h) ]
    ck = [[0] * w for _ in range(h)]
    q = deque()
    dx, dy = [1,0,-1,0, 1, 1, -1, -1], [0,1,0,-1, 1, -1, 1, -1]
    res = 0

    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and ck[i][j] == 0:
                q.append([i, j])
                ck[i][j] = 1

                while q:
                    a, b = q.popleft()

                    for x, y in zip(dx, dy):
                        nx, ny = a + x, b + y

                        if 0 <= nx < h and 0 <= ny < w and ck[nx][ny] == 0 and land[nx][ny] == 1:
                            q.append([nx, ny])
                            ck[nx][ny] = 1

                res += 1

    print(res)
    w, h = map(int, input().split())

