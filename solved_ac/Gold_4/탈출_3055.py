'''
bfs문제이다.
처음에 문제를 보고 물 한 번, 고슴도치 한번 이렇게 두 번씩 bfs를 돌까 생각을 했는데,
너무 단순하게 생각했었다. 구현을 하다가 '아 한번 bfs를 돌면 forest의 값들이 다 물로 되거나 다 고슴도치로 되겠구나' 싶어서 바로 수정했다.
수정한 방식은 고슴도치('S')의 위치를 먼저 q에 넣은 다음에, 물('*')의 위치를 q에 넣는다
고슴도치가 상하좌우로 이동할 수 있는 곳을 고슴도치('S')로 만들고, 그다음에 들어있는 물 위치 값을 가지고 상하좌우로 물로 만든다.
문제 조건에서 물이 고슴도치를 잡아먹을 수 있기 때문에 물의 상하좌우를 고슴도치보다 뒤에 실행시켰다.
그리고 q를 계속 돌면서 비버 굴('D')의 위치(final_x, final_y)에 도착하면(해당 위치가 S로 바뀌면 고슴도치가 도착했다는 뜻)
res로 + 1 해주면서 최종 거리 값을 리턴한다
q가 빌 때까지 도착을 못하면 'KAKTUS'를 반환한다.
'''
from collections import deque

r, c = map(int, input().split())
forest = [ list(input()) for _ in range(r) ]

# 테스트
r, c, forest = 3, 3, [['D', '.', '*'], ['.', '.', '.'], ['.', 'S', '.']] # 3
r, c, forest = 3, 3, [['D', '.', '*'], ['.', '.', '.'], ['.', '.', 'S']] # KAKTUS
r, c, forest = 3, 6, [['D','.','.','.','*','.'], ['.','X','.','X','.','.'], ['.','.','.','.','S','.']] # 6
r, c, forest = 5, 4, [['.','D','.','*'], ['.','.','.','.'], ['.','.','X','.'], ['S','.','*','.'], ['.','.','.','.']] # 4

res = [[0] * c for _ in range(r)]
q = deque()

for i in range(r):
    for j in range(c):
        if forest[i][j] == 'S':
            q.append((i, j))
        elif forest[i][j] == 'D':
            final_x, final_y = i, j

for i in range(r):
    for j in range(c):
        if forest[i][j] == '*':
            q.append((i, j))

def bfs(final_x, final_y):
    dx, dy = [1,0,-1,0], [0,1,0,-1]

    while q:
        a, b = q.popleft()

        if forest[final_x][final_y] == 'S':
            return res[final_x][final_y]
        
        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < r and 0 <= ny < c:
                if (forest[nx][ny] == '.' or forest[nx][ny] == 'D') and forest[a][b] == 'S' and forest[nx][ny] != 'X':
                    forest[nx][ny] = 'S'
                    res[nx][ny] = res[a][b] + 1
                    q.append((nx, ny))
                elif (forest[nx][ny] == '.' or forest[nx][ny] == 'S') and forest[a][b] == '*' and forest[nx][ny] != 'X':
                    forest[nx][ny] = '*'
                    q.append((nx, ny))

    return 'KAKTUS'

print(bfs(final_x, final_y))