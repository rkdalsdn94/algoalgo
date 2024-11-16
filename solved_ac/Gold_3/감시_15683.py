# 백준 - 골드4 - 감시 - 15683 - 구현, 시뮬레이션, 완전 탐색 문제
'''
구현, 시뮬레이션, 완전 탐색 문제

cctv의 종류에 따라서 감시할 수 있는 영역을 체크하는 문제이다.
아래 풀이를 참고할 수 있는 자료들이 되게 많아서(유투브도 좋은 자료가 많음) 이해가 잘 안되면 검색해서 참고하면 된다.

풀이 과정
    1. cctv의 위치와 종류를 저장
    2. cctv의 종류에 따라서 4방향을 탐색하며 감시할 수 있는 영역을 체크
    3. cctv의 종류에 따라서 감시할 수 있는 영역을 체크
    4. dfs를 통해 모든 cctv의 경우의 수를 탐색
    5. 결과 출력

in
    4 6
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 1 0 6 0
    0 0 0 0 0 0
out
    20

in
    6 6
    0 0 0 0 0 0
    0 2 0 0 0 0
    0 0 0 0 6 0
    0 6 0 0 2 0
    0 0 0 0 0 0
    0 0 0 0 0 5
out
    15

in
    6 6
    1 0 0 0 0 0
    0 1 0 0 0 0
    0 0 1 0 0 0
    0 0 0 1 0 0
    0 0 0 0 1 0
    0 0 0 0 0 1
out
    6

in
    6 6
    1 0 0 0 0 0
    0 1 0 0 0 0
    0 0 1 5 0 0
    0 0 5 1 0 0
    0 0 0 0 1 0
    0 0 0 0 0 1
out
    2

in
    1 7
    0 1 2 3 4 5 6
out
    0

in
    3 7
    4 0 0 0 0 0 0
    0 0 0 2 0 0 0
    0 0 0 0 0 0 4
out
    0
'''

import copy

n, m = map(int, input().split())
cctv = []
graph = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 상, 우, 하, 좌

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])

def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y

        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = 7

def dfs(depth, arr):
    global res

    if depth == len(cctv):
        count = 0

        for i in range(n):
            count += arr[i].count(0)

        res = min(res, count)
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        fill(temp, i, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)

res = int(1e9)
dfs(0, graph)
print(res)
