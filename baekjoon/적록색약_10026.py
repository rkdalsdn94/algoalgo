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
    global bfs_cnt
    while q:
        a, b, temp = q.popleft()
        bfs_ck[a][b] = 1

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < n and n_list[nx][ny] == temp and bfs_ck[nx][ny] == 0:
                # 위치인덱스, 해당 색, 체크에서 아직 들어오지 못했을때
                bfs_ck[nx][ny] = 1
                q.append((nx, ny, n_list[nx][ny]))
    bfs_cnt += 1

def rg_bfs(q):
    global rg_cnt
    while q:
        a, b, temp = q.popleft()
        rg_ck[a][b] = 1

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < n and n_list[nx][ny] == temp and rg_ck[nx][ny] == 0:
                rg_ck[nx][ny] = 1
                q.append((nx, ny, n_list[nx][ny]))
    rg_cnt += 1

for i in range(n):
    for j in range(n):
        if n_list[i][j] == 'G':
            rg_ck[i][j] = 'R'

for i in range(n):
    for j in range(n):
        # for z in ('R','G','B')
        q.append((i, j, n_list[i][j]))
        if bfs_ck[i][j] == 0:
            bfs(q)
        q.append((i, j, n_list[i][j]))
        if rg_ck[i][j] == 0:
            rg_bfs(q)

# print(n_list)
print(bfs_cnt, rg_cnt)
