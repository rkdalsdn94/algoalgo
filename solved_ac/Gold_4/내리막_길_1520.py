'''
처음에 bfs로 접근해서 (개인적인 습관이 탐색 문제를 만났을 때 항상 bfs로 먼저 생각한다.. 앞으로 조심해야지...)
해결 방안이 마땅히 떠오르지 않았다. --> bfs를 여러번 실행해야 되는데 그 실행 방법에 대해 어떻게 둬야할지에 대한 의문..? (bfs로 풀 수 있으려나..?)
그래서 방식을 dfs로 바꾼 후 해당 부분의 끝까지 갈 수 있을 때 1반환 아래 코드 상에서 첫 번째 탈출 조건
그다음 재귀 함수를 빠져나갈 때, 바로 전에 들어왔던 인덱스에 1을 더하면서 총 방문할 수 있는 경로 설정하는 방식으로 접근하니 해결할 수 있었다.
그래도 아직 dfs는 어색하다. dfs에 친해져야겠다
'''

# import sys
# sys.setrecursionlimit(10 ** 6)

# m, n = map(int, input().split())
# board = [ list(map(int, input().split())) for _ in range(m) ]
# # print(m, n, board)

# 테스트
m, n = 4, 5
board = [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]] # 3

ck = [ [-1] * n for _ in range(m) ]


def dfs(x, y):
    dx, dy = [1,0,-1,0], [0,1,0,-1]

    if x == len(board) - 1 and y == len(board[0]) - 1:
        return 1

    if ck[x][y] != -1:
        return ck[x][y]

    ck[x][y] = 0

    for i, j in zip(dx, dy):
        nx, ny = x + i, y + j

        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] < board[x][y]:
            ck[x][y] += dfs(nx, ny)

    return ck[x][y]

print(dfs(0, 0))

