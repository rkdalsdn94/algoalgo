'''
bfs 문제

문제중 쩰리는 오른쪽 또는 아래쪽으로만 이동할 수 있어서 dx, dy는 (0, 1) (1, 0)로만 만들면 된다.
그리고 다음칸에서 이동할 수 있는지만 검사하면 되는 문제라서 조건만 잘 생각하고 구현하면 된다.
'''

from collections import deque

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 3
# board = [ [1,1,10], [1,5,1], [2,2,-1] ] # HaruHaru
# n = 3
# board = [ [2,2,1], [2,2,2], [1,2,-1] ] # Hing

ck = [ [0] * n for _ in range(n) ]
res = True

def bfs(x, y):
    q = deque([(x, y)])
    dx, dy = [0,1], [1,0]
    ck[x][y] = 1

    while q:
        a, b = q.popleft()

        if a == n - 1 and b == n - 1:
            return True

        for i, j in zip(dx, dy):
            nx, ny = a + i * board[a][b], b + j * board[a][b]

            if 0 <= nx < n and 0 <= ny < n and ck[nx][ny] == 0:
                q.append((nx, ny))
                ck[nx][ny] = 1

    return False

res = bfs(0, 0)

if res:
    print('HaruHaru')
else:
    print('Hing')
