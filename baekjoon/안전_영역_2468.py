# 백준 안전 영역 - 2468 --- 지금 bfs 로만 품, 나중에 dfs로 해보자
'''
물의 높이가 0 일수도 있음
0 생각 못하고 전체 for 문 1 부터 시작하다가 81%에서 틀림
81% 쯤 예제에서 물 0 일때에 관한 예제가 나오나봄
'''
from collections import deque

# n = 5
# n_list = [ [6,8,2,6,2],[3,2,3,4,6],
# [6,7,3,3,2],[7,2,5,3,6],[8,9,5,2,7] ]  # 5
n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

dx, dy = [1, 0, -1, 0], [0,1,0,-1]

res = []

def bfs(q):
    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a+i, b+j

            if 0 <= nx < n and 0 <= ny < n and ck[nx][ny] == 1:
                ck[nx][ny] = 0
                q.append((nx, ny))

# print(n, n_list, ck, cnt)

for z in range(101):
    ck = [[0]*n for _ in range(n)]
    cnt = 0
    q = deque()
    
    # 물에 안 잠기는 지역 - 이 지역으로 bfs 실행
    for i in range(n):
        for j in range(n):
            if n_list[i][j] > z:
                ck[i][j] = 1
            else:
                ck[i][j] = 0

    for i in range(n):
        for j in range(n):
            if ck[i][j]:
                ck[i][j] = 0
                q.append((i, j))
                bfs(q)
                cnt += 1
    res.append(cnt)
    

print(max(res))




