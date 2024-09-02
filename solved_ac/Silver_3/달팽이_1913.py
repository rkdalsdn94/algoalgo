# 백준 - 실버3 - 달팽이 - 1913 - 구현 문제
'''
구현 문제

달팽이를 구하는 문제인데, 기존에 풀었던 달팽이와는 다르게 제일 안 쪽부터 바깥 쪽으로 나간다.
  ex) 기존 달팽이    ex) 현재 달팽이
       1 2 3            9 2 3
       8 9 4            8 1 4
       7 6 5            7 6 5
그래서 이번 문제를 풀 때는 cnt를 n * n으로 초기화하고 cnt가 0이 될 때까지 구하는 방식으로 풀었다.
board[0][0] 위치부터 시작해서 방향을 정하고 범위를 벗어나지 않는지 확인하면서 이동한다.
방향은 하, 우, 상, 좌 순서로 이동한다.

풀이 과정
    1. n, m을 입력받는다.
    2. n * n의 2차원 배열을 만든다.
    3. dx, dy를 만들어 방향을 정한다.
    4. x, y, direction, cnt를 만들어 초기화한다.
    5. cnt가 0이 될 때까지 반복한다.
    6. nx, ny를 만들어 범위를 벗어나지 않는지 확인한다.
    7. 범위를 벗어나지 않는다면 nx, ny로 이동하고 cnt를 1 감소시킨다.
    8. 범위를 벗어나면 방향을 바꾸고 nx, ny로 이동한다.
    9. cnt가 m이 되면 res_x, res_y를 저장한다.
    10. 2차원 배열(board)을 출력한다.
    11. res_x, res_y를 출력한다.
'''

n, m = int(input()), int(input())

# 테스트
# n, m = 7, 35
# '''
# out
#     49 26 27 28 29 30 31
#     48 25 10 11 12 13 32
#     47 24 9 2 3 14 33
#     46 23 8 1 4 15 34
#     45 22 7 6 5 16 35
#     44 21 20 19 18 17 36
#     43 42 41 40 39 38 37
#     5 7
# '''

board = [[0] * n for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 하 우 상 좌
x, y, direction, cnt = 0, 0, 0, n * n
res_x, res_y = -1, -1

while cnt > 0:
    board[x][y] = cnt

    if cnt == m:
        res_x, res_y = x + 1, y + 1

    cnt -= 1
    nx, ny = x + dx[direction], y + dy[direction]

    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
        x, y = nx, ny
    else:
        direction = (direction + 1) % 4
        x, y = x + dx[direction], y + dy[direction]

for x in range(n):
    print(*board[x])
print(res_x, res_y)
