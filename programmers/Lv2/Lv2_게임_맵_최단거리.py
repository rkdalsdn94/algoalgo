# 1 : 이동가능, 0 : 벽
from collections import deque

def solution(maps):
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    q = deque()
    q.append((0,0))
    ck = [[0] * len(maps[0]) for _ in range(len(maps))]
    ck[0][0] = 1

    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 and ck[nx][ny] == 0:
                ck[nx][ny] = ck[a][b] + 1
                q.append((nx, ny))
    
    return -1 if ck[-1][-1] == 0 else ck[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1