def dfs(a, b):
    global flag
    dx, dy = [0, -1, 0, 1, -1, -1, 1, 1], [1, 0, -1, 0, -1, 1, -1, 1]
    ck[a][b] = 1

    for i, j in zip(dx, dy):
        nx, ny = a + i, b + j

        if 0 <= nx < n and 0 <= ny < m:
            if mountain_peaks[nx][ny] > mountain_peaks[a][b]:
                flag = False
            
            if not ck[nx][ny] and mountain_peaks[a][b] == mountain_peaks[nx][ny]:
                dfs(nx, ny)

def solution():
    res = 0

    for i in range(n):
        for j in range(m):
            if mountain_peaks[i][j] > 0 and not ck[i][j]:
                flag = True
                dfs(i, j)

                if flag:
                    res += 1

    return res

# n, m = map(int, input().split())
# mountain_peaks = [list(map(int, input().split())) for _ in range(n)]
# ck = [[0] * m for _ in range(n)]
# print(solution())

# 테스트
n, m = 8, 7
mountain_peaks = [[4, 3, 2, 2, 1, 0, 1], [3, 3, 3, 2, 1, 0, 1], [2, 2, 2, 2, 1, 0, 0], [2, 1, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 1, 0], [0, 1, 2, 2, 1, 1, 0], [0, 1, 1, 1, 2, 1, 0]]
ck = [[0] * m for _ in range(n)]
print(solution())


