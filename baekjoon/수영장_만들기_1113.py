# 백준 수영장 만들기 - 1113
'''
첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 땅의 높이가 주어진다.
높이는 1보다 크거나 같고, 9보다 작거나 같은 자연수이다.
'''
'''
in
    3 5
    16661
    61116
    16661
out
    15
'''
from collections import deque

n, m = 3, 5
g = [ [1,6,6,6,1],
    [6,1,1,1,6],
    [1,6,6,6,1] ]
# n, m = map(int, input().split())
# g = [ list(map(int, list(input()))) for _ in range(n) ]
dx, dy = [1,0,-1,0], [0, 1, 0, -1]
q = deque()
res = 0

def bfs(j, z, i):
    global ck, res, q
    flag = False
    num = 1
    ck[j][z] = 1
    q.append((j, z))

    while 1:
        a, b = q.popleft()
        for j, z in zip(dx, dy):
            nx, ny = a + j, b + z
            if nx == -1 or nx == n or ny == -1 or ny == m:
                flag = True
                continue
            if g[nx][ny] <= i and ck[nx][ny] == 0:
                ck[nx][ny] = 1
                q.append((nx, ny))
                num += 1
                    
        if not q:
            if not flag:
                res += num
            return

for i in range(1, 9):
    ck = [ [0] * m for _ in range(n) ]
    for j in range(n):
        for z in range(m):
            if g[j][z] <= i and ck[j][z] == 0:
                bfs(j, z, i)

print(res)