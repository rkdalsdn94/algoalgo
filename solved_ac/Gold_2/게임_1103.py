'''
구현, dfs, dp 문제

dp배열로 경로(cnt)를 체크하는 조건이 없으면 (메모이제이션)
시간 초과(python3), 메모리 초과(pypy3)가 나온다.
재귀 깊이 설정 하지 않으면 RecursionError가 나온다.

문제 조건 중 0, 0은 무조건 실행할 수 있어서 cnt를 로 설정해도 된다.
나머진 위, 아래, 왼쪽, 오른쪽 board판을 돌아다닐 수 있거나
해당 글자가 'H'가 아니면 dfs를 실행할 수 있게 만들었다.

그러다 ck변수를 참인 곳에 또 도착할 시 사이클이 발생하는 경우라서 무한 루프 상황이라
-1을 리턴하고 프로그램 실행을 종료했다.

아래 예제들로 디버그를 하거나, 손으로 풀다보면 감이 온다.
'''

import sys; sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
board = [ list(map(str, input())) for _ in range(n) ]

# 테스트
# n, m = 3, 7
# board = [
#     ['3', '9', '4', '2', '1', '7', '8'],
#     ['1', '2', '3', '4', '5', '6', '7'],
#     ['9', '1', '2', '3', '5', '3', '2']
# ] # 5
# n, m = 1, 1
# board = [['2', 'H', '3', 'H', 'H', '4', 'H', 'H', 'H', '5']] # 4
# n, m = 4, 4
# board = [
#     ['3','9','9','4'],
#     ['9','9','9','9'],
#     ['9','9','9','9'],
#     ['2','9','2','4']
# ] # -1
# n, m = 4, 6
# board = [
#     ['1','2','3','4','5','6']
#     ['2','3','4','5','6','7']
#     ['3','4','5','6','7','8']
#     ['4','5','6','7','8','9']
# ] # 4
# n, m = 1, 1
# board = [['1']] # 1
# n, m = 3, 7
# board = [
#     ['2','H','9','H','H','1','1'],
#     ['H','H','H','H','H','1','1'],
#     ['9','H','H','H','H','1','1']
# ] # 2

ck = [ [0] * m for _ in range(n) ]
dp = [ [0] * m for _ in range(n) ]
res = 1

def dfs(x, y, cnt):
    global res
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    res = max(res, cnt)

    for i in range(4):
        nx, ny = x + int(board[x][y]) * dx[i], y + int(board[x][y]) * dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'H' and cnt + 1 > dp[nx][ny]:
            if ck[nx][ny]:
                print(-1)
                exit()
            dp[nx][ny] = cnt + 1
            ck[nx][ny] = 1
            dfs(nx, ny, cnt + 1)
            ck[nx][ny] = 0

dfs(0, 0, 1)
print(res)