'''
구현, dfs, 완전 탐색 문제이다.
'''

# import sys; input = sys.stdin.readline

# n, m = map(int, input().split())
# board = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
n, m = 5, 5
board = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6],
        [6, 5, 4, 3, 2], [1, 2, 1, 2, 1]] # 19
n, m = 4, 5
board = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]] # 20
n, m = 4, 10
board = [[1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]] # 7

derivative = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
ck = [ [0] * m for _ in range(n) ]
res = 0

def dfs(x, y, temp, cnt):
    global res

    if cnt == 4:
        res = max(res, temp)
        return
    
    for i in range(4):
        nx, ny = x + derivative[i][0], y + derivative[i][1]

        if 0 <= nx < n and 0 <= ny < m and not ck[nx][ny]:
            ck[nx][ny] = 1
            dfs(nx, ny, temp + board[nx][ny], cnt + 1)
            ck[nx][ny] = 0

def h_dfs(x, y):
    global res

    for i in range(4):
        tmp = board[x][y]

        for j in range(3):
            idx = (i + j) % 4
            nx, ny = x + derivative[idx][0], y + derivative[idx][1]

            if not (0 <= nx < n and 0 <= ny < m):
                tmp = 0
                break
            tmp += board[nx][ny]
        res = max(res, tmp)

for i in range(n):
    for j in range(m):
        ck[i][j] = 1
        dfs(i, j, board[i][j], 1)
        ck[i][j] = 0
        h_dfs(i, j)

print(res)
