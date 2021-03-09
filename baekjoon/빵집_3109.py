# 처음에 x가 대문자 X 인줄 알았는데 소문자 x여서 틀림;;

# r, c = 5, 5
# pipe_list = [ ['.','X','X','.','.'], ['.','.','X','.','.'],
# ['.','.','.','.','.'], ['.','.','.','X','.'],['.','.','.','X','.']  ]  # 2
# ck = [[0] * c for _ in range(c)]
r, c = map(int, input().split())
pipe_list = [ list(input()) for _ in range(r) ]
# ck = [[0] * c for _ in range(c)]

dx, dy = [-1,0,1], [1,1,1]
res = 0

def bfs(a, b):
    if b == c - 1:
        return True
    pipe_list[a][b] = 'x'
    for i, j in zip(dx, dy):
        nx, ny = i + a, j + b

        if 0 <= nx < r and 0 <= ny < c and pipe_list[nx][ny] != 'x':
            if bfs(nx, ny):
                pipe_list[nx][ny] = 'x'
                return True
    return False

for i in range(r):
    if bfs(i, 0):
        res += 1
    

print(res)