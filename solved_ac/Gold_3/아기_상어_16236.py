# 백준 - 골드3 - 아기 상어 - 16236 - 구현, 그래프, 시뮬레이션, bfs 문제
'''
구현, 그래프, 시뮬레이션, bfs 문제

꽤 많이 헤맨 문제이다. bfs 풀이인데 시뮬레이션 성향이 강하다. 소위 말하는 빡구현 문제다..

자바로 푼 https://www.youtube.com/watch?v=5uqrqHOXTJY 이 유튜브 영상을 보고 구현의 힌트를 얻을 수 있었다.
까다로웠던 아래의 조건은 정렬로 해결했다.
 - '거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.'
위 조건을 정렬로 해결했다. 정렬로 해결 가능한 이유는 x, y 모두 작은 수가 왼쪽 위를 뜻한다. - (2, 2) 보다 (1, 1)이 왼쪽 위에 있다.

다음으로 까다로운 물고기가 먹을 수 있는 크기 부분은 size와 eat_cnt로 두고 bfs가 한 번 실행할 때마다 한 마리의 물고기를 먹는다고 만든 후,
bfs 실행이 끝날 때 eat_cnt에 1을 더하고, eat_cnt 가 size 와 같아 졌을 때 size 에 1을 더한다. (eat_cnt 는 0으로 바꿔줘야 한다.)
'''

from collections import deque
INF = int(1e9)

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# from collections import deque
# INF = int(1e9)
# n = 3
# board = [ [0, 0, 0], [0, 0, 0], [0, 9, 0] ] # 0
# n = 3
# board = [ [0, 0, 1], [0, 0, 0], [0, 9, 0] ] # 3
# n = 4
# board = [ [4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 9, 0], [1, 2, 3, 4] ] # 14
# n = 6
# board = [
#     [5, 4, 3, 2, 3, 4], [4, 3, 2, 3, 4, 5],
#     [3, 2, 9, 5, 6, 6], [2, 1, 2, 3, 4, 5],
#     [3, 2, 1, 6, 5, 4], [6, 6, 6, 6, 6, 6]
# ] # 60
# n = 6
# board = [
#     [6, 0, 6, 0, 6, 1],
#     [0, 0, 0, 0, 0, 2],
#     [2, 3, 4, 5, 6, 6],
#     [0, 0, 0, 0, 0, 2],
#     [0, 2, 0, 0, 0, 0],
#     [3, 9, 3, 0, 0, 1]
# ] # 48
# n = 6
# board = [
#     [1, 1, 1, 1, 1, 1],
#     [2, 2, 6, 2, 2, 3],
#     [2, 2, 5, 2, 2, 3],
#     [2, 2, 2, 4, 6, 3],
#     [0, 0, 0, 0, 0, 6],
#     [0, 0, 0, 0, 0, 9]
# ] # 39

position_x, position_y = 0, 0
size, eat_cnt, res = 2, 0, 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(x, y):
    ck = [ [0] * n for _ in range(n) ]
    q = deque([(x, y, 0)])
    ret = []
    ck[x][y] = 1
    min_distance = INF

    while q:
        a, b, c = q.popleft()

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and ck[nx][ny] == 0 and board[nx][ny] <= size:
                ck[nx][ny] = 1

                if 0 < board[nx][ny] < size:
                    if min_distance == INF:
                        min_distance = c + 1
                    elif c + 1 > min_distance:
                        return ret
                    ret.append([nx, ny, c + 1])
                q.append([nx, ny, c + 1])

    return ret

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            position_x, position_y = i, j
            board[position_x][position_y] = 0

while 1:
    temp = bfs(position_x, position_y)
    if not temp:
        break
    
    temp.sort() # 가장 왼쪽에 있는 물고기를 먹는 상황
    position_x, position_y, step = temp[0]
    res += step
    board[position_x][position_y] = 0
    eat_cnt += 1

    if size == eat_cnt:
        size += 1
        eat_cnt = 0

print(res)
