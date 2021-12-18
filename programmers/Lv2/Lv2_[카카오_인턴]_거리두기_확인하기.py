from collections import deque

def bfs(p, x, y):
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    q = deque()
    ck = [[0]*5 for _ in range(5)]

    q.append([x,y,0])
    ck[x][y] = 1

    while q:
        a, b, c = q.popleft()

        if 1 <= c <= 2 and p[a][b] == 'P':
            return False

        if c >= 3:
            break

        for i, j in zip(dx, dy):
            nx, ny, nz = a + i, b + j, c + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and p[nx][ny] != 'X' and ck[nx][ny] == 0:
                q.append([nx, ny, nz])
                ck[nx][ny] = 1
                
    return True

def ck(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                if bfs(p, i, j) == False:
                    return 0
    return 1

def solution(places):
    answer = []
    for i in places:
        answer.append(ck(i))

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])) # [1, 0, 1, 1, 1]