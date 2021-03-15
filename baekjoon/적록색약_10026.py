from collections import deque

n = 5
n_list = [ ['R','R','R','B','B'],['G','G','B','B','B'],
['B','B','B','R','R'],['B','B','R','R','R'],
['R','R','R','R','R'] ]
# n = int(input())
# n_list = [ list(input()) for _ in range(n) ]

res = []
dx, dy = [1,0,-1,0], [0,1,0,-1]
bfs_cnt, rg_cnt = 0, 0
q = deque()

bfs_ck = [ [0] * n for _ in range(n) ]
rg_ck = [ [0] * n for _ in range(n) ]

def bfs(q):
    while q:
        a, b, temp = q.popleft()
        bfs_ck[a][b] = 1

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < n and n_list[nx][ny] == temp and bfs_ck[nx][ny] == 0:
                q.append((nx, ny, n_list[nx][ny]))
                bfs_ck[nx][ny] = 1

def rg_bfs(q):
    while q:
        a, b, temp = q.popleft()
        rg_ck[a][b] = 0

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < n and rg_ck[nx][ny] == temp:
                q.append((nx, ny, rg_ck[nx][ny]))
                rg_ck[nx][ny] = 0

for i in range(n):
    for j in range(n):
        if n_list[i][j] == 'G' or n_list[i][j] == 'R':
            rg_ck[i][j] = 1
        else:
            rg_ck[i][j] = 2
        

for i in range(n):
    for j in range(n):
        if bfs_ck[i][j] == 0:
            q.append((i, j, n_list[i][j]))
            bfs(q)
            bfs_cnt += 1
        if rg_ck[i][j] != 0:
            q.append((i, j, rg_ck[i][j]))
            rg_bfs(q)
            rg_cnt += 1

# print(n_list)
print(bfs_cnt, rg_cnt)
