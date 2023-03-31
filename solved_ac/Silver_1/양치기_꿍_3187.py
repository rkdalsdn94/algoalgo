# 백준 - 실버1 - 양치기 꿍 - 3187 - 그래프, dfs, bfs 문제
'''
그래프, dfs, bfs 문제

bfs 방식으로 문제를 풀었다. (나중에 dfs로도 풀어보고 싶다.)
bfs 문제 중 크게 어렵지 않은 문제이다.
조심할 부분은 '#'이 아닌 곳에서 bfs 실행 중에 v와 k의 수가 같으면 v를 더하고, k가 더 높으면 k만 더하면 된다.
위 부분만 조심하면 구현하는데 큰 어려움은 없다.
'''

from collections import deque

r, c = map(int, input().split())
board = [ input() for _ in range(r) ]

# 테스트
# r, c = 6, 6
# board = [
#     '...#..',
#     '.##v#.',
#     '#v.#.#',
#     '#.k#.#',
#     '.###.#',
#     '...###',
# ] # 0 2
# r, c = 8, 8
# board = [
#     '.######.',
#     '#..k...#',
#     '#.####.#',
#     '#.#v.#.#',
#     '#.#.k#k#',
#     '#k.##..#',
#     '#.v..v.#',
#     '.######.'
# ] # 3 1
# r, c = 9, 12
# board = [
#     '.###.#####..',
#     '#.kk#...#v#.',
#     '#..k#.#.#.#.',
#     '#..##k#...#.',
#     '#.#v#k###.#.',
#     '#..#v#....#.',
#     '#...v#v####.',
#     '.####.#vv.k#',
#     '.......####.'
# ] # 3 5

dx, dy = [0, 1, 0, -1], [1, 0 , -1, 0]
ck = [ [0] * c for _ in range(r) ]
v_cnt, k_cnt = 0, 0

def bfs(x, y):
    global v_cnt, k_cnt

    ck[x][y] = 1
    q = deque([(x, y)])
    v_temp, k_temp = 0, 0

    if board[x][y] == 'k':
        k_temp += 1
    elif board[x][y] == 'v':
        v_temp += 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != '#' and ck[nx][ny] == 0:
                ck[nx][ny] = 1
                q.append([nx, ny])

                if board[nx][ny] == 'k':
                    k_temp += 1
                elif board[nx][ny] == 'v':
                    v_temp += 1

    if v_temp >= k_temp:
        v_cnt += v_temp
    else:
        k_cnt += k_temp

for i in range(r):
    for j in range(c):
        if (board[i][j] == 'v' or board[i][j] == 'k') and ck[i][j] == 0:
            bfs(i, j)

print(k_cnt, v_cnt)
