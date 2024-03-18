# 프로그래머스 - Lv2 - PCCP 기출문제 2번 석유 시추 - bfs 문제
'''
bfs 문제

풀이 과정
 - res를 land의 가로 줄만 기준으로 만들어둔다. (아래 코드에선 중복 제거를 위해 m으로 초기화 함)
 - bfs 방식으로 각 덩어리의 크기를 구한 뒤 한 번의 bfs가 끝날 때마다 res의 해당 컬럼의 값을 덩어리의 값으로 바꿔준다.
    - ex) 3 * 3 덩어리
            1 1 0
            0 1 0    ->  한 번의 bfs 가 끝났을 때 res의 배열은 [3, 3, 0]이 된다.
            0 0 1
 - bfs가 끝났을 때 마다 열을 기준으로 0으로 초기화한 res 배열에 덩어리 값들을 더해준다. (이때 min_m, max_m이 사용됨)
    - n은 행, m은 열이다.
 - 최종 res 배열에 최댓값을 return 하면 된다.
'''

from collections import deque

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y, land):
    num = 0
    q = deque([(x, y)])
    ck[x][y] = 1
    min_m, max_m = int(1e9), -int(1e9)

    while q:
        a, b = q.popleft()
        min_m, max_m = min(min_m, b), max(max_m, b) # 가로 줄을 기준으로 가장 작은 값과 큰 값을 구해야 된다.
        num += 1

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and land[nx][ny] == 1:
                q.append([nx, ny])
                ck[nx][ny] = 1

    for i in range(min_m, max_m + 1):
        res[i] += num

def solution(land):
    global res, n, m, ck

    res = [0] * len(land[0])
    n, m = len(land), len(land[0])
    ck = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if ck[i][j] == 0 and land[i][j] == 1:
                bfs(i, j, land)

    return max(res)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])) # 9
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])) # 16
