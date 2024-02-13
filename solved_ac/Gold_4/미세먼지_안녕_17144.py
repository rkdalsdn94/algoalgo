# 백준 - 골드4 - 미세먼지 안녕! - 17144 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

신경써야 될 조건들이 많아 문제를 잘 쪼개서 풀어야 된다.
따라서, 미세먼지가 확산, 위쪽 공기 청정기, 아래쪽 공기 청정기의 동작들을 각각의 함수로 만들어서 풀었다.

풀이 과정
 - input 데이터를 잘 입력 받고, 공기청정기의 위치를 찾는다. (나란히 들어오기 때문에 처음걸 찾은 다음 + 1을 통해 구할 수 있음)
 - 미세먼지 확산, 공기청정기 위쪽, 아래쪽을 t 만큼 실행 시킨다.
    - 각각에선 bfs를 통해 구현했다.
    - 이를 구현할 때 방향을 조심해서 구현해야 된다.
    - 이 부분은 첫 번째 예제로 https://pythontutor.com/visualize.html#mode=edit 여기서 실행해보면 된다.
 - 정답을 출력할 땐 공기 청정기가 -1로 들어오므로 2를 더한 뒤 출력해야 한다.
'''

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

# 테스트
# r, c, t = 7, 8, 1
# board = [
#     [0, 0, 0, 0 ,0 ,0 ,0, 9],
#     [0, 0, 0, 0 ,3, 0 ,0, 8],
#     [-1, 0, 5, 0, 0, 0, 22, 0],
#     [-1, 8, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 10, 43, 0],
#     [0, 0, 5, 0, 15, 0, 0, 0],
#     [0, 0, 40, 0, 0, 0, 20, 0]
# ] # 188
# r, c, t = 7, 8, 2
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 9],
#     [0, 0, 0, 0, 3, 0, 0, 8],
#     [-1, 0, 5, 0, 0, 0, 22, 0],
#     [-1, 8, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 10, 43, 0],
#     [0, 0, 5, 0, 15, 0, 0, 0],
#     [0, 0, 40, 0, 0, 0, 20, 0],
# ] # 186
# r, c, t = 7, 8, 4
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 9],
#     [0, 0, 0, 0, 3, 0, 0, 8],
#     [-1, 0, 5, 0, 0, 0, 22, 0],
#     [-1, 8, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 10, 43, 0],
#     [0, 0, 5, 0, 15, 0, 0, 0],
#     [0, 0, 40, 0, 0, 0, 20, 0],
# ] # 178
# r, c, t = 7, 8, 20
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 9],
#     [0, 0, 0, 0, 3, 0, 0, 8],
#     [-1, 0, 5, 0, 0, 0, 22, 0],
#     [-1, 8, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 10, 43, 0],
#     [0, 0, 5, 0, 15, 0, 0, 0],
#     [0, 0, 40, 0, 0, 0, 20, 0],
# ] # 71
# r, c, t = 7, 8, 30
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 9],
#     [0, 0, 0, 0, 3, 0, 0, 8],
#     [-1, 0, 5, 0, 0, 0, 22, 0],
#     [-1, 8, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 10, 43, 0],
#     [0, 0, 5, 0, 15, 0, 0, 0],
#     [0, 0, 40, 0, 0, 0, 20, 0],
# ] # 52
# r, c, t = 7, 8, 50
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 9],
#     [0, 0, 0, 0, 3, 0, 0, 8],
#     [-1, 0, 5, 0, 0, 0, 22, 0],
#     [-1, 8, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 10, 43, 0],
#     [0, 0, 5, 0, 15, 0, 0, 0],
#     [0, 0, 40, 0, 0, 0, 20, 0],
# ] # 46

air_purifier_up, air_purifier_down = 0, 0
for i in range(r): # 공기 청정기 위치 찾기
    if board[i][0] == -1:
        air_purifier_up = i
        air_purifier_down = i + 1
        break

# 미세먼지 확산
def spread():
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0] # 북, 서, 동, 남
    temp_board = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] != 0 and board[i][j] != -1:
                temp = 0

                for k in range(4):
                    nx, ny = dx[k] + i, dx[k] + j

                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        temp_board[nx][ny] += board[i][j] // 5
                        temp += board[i][j] // 5
                board[i][j] -= temp

    for i in range(r):
        for j in range(c):
            board[i][j] += temp_board[i][j]

# 공기청정기 위로
def up():
    dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]  # 동, 북, 서, 남
    direction, prev = 0, 0
    x, y = air_purifier_up, 1

    while 1:
        nx, ny = x + dx[direction], y + dy[direction]

        if x == air_purifier_up and y == 0:
            break
        if 0 <= nx < r and 0 <= ny < c:
            board[x][y], prev = prev, board[x][y]
            x, y = nx, ny
        else:
            direction += 1
            continue

# 공기청정기 아래로
def down():
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 동, 남, 서, 북
    direction, prev = 0, 0
    x, y = air_purifier_down, 1

    while 1:
        nx, ny = x + dx[direction], y + dy[direction]

        if x == air_purifier_down and y == 0:
            break
        if 0 <= nx < r and 0 <= ny < c:
            board[x][y], prev = prev, board[x][y]
            x, y = nx, ny
        else:
            direction += 1
            continue

for _ in range(t):
    spread()
    up()
    down()

res = 0
for i in range(r):
    res += sum(board[i])

print(res + 2) # 공기 청정기 위치가 -1로 표시되므로 2를 더해줘야 된다.
