# 백준 - 실버2 - 로봇 - 13901 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

robot 위치 : 2
장애문 위치 : 1
빈칸 위치 : 0
방향 정보
    1 : 상 (-1, 0)
    2 : 하 (1, 0)
    3 : 좌 (0, -1)
    4 : 우 (0, 1)

위와 같은 정보를 토대로 구현해야 하는 문제이다.
 - 만약 7%에서 '틀렸습니다.' 가 나온다면 인덱스 에러 부분을 조심하자.
 - 범위 검사하는 로직에서 반복문을 빠져나올 때 방문 여부를 먼저 체크하고, 범위 계산을 해서 인덱스 에러가 나옴.

풀이 과정
 - 입력값들을 잘 입력받고, board에 장애물 위치는 1로 시작 위치는 2로 표시한다.
 - ck 리스트를 만들어서 방문 여부를 체크한다. (시작 위치와 장애물 위치는 방문한 것으로 처리한다.)
 - 방향에 관한 정보는 위를 토대로 direction이라는 각 숫자(상하좌우)에 맞춰 준비한다.
 - 범위를 벗어나지 않거나 장애물이 아니면 이동하고, 범위를 벗어나거나 장애물이면 방향을 바꾼다.
 - 범위를 벗어나지 않는 상황이면 flag 값을 True 수정해 다음 반복문을 실행할 수 있게 한다.
 - 만약 범위를 계속해서 벗어난다면 flag 값이 False로 유지되어 반복문을 빠져나온다.
 - 최종적인 nx와 ny의 위치를 출력하면 된다. (이것을 rex_x, res_y로 저장했으니 이를 출력하면 된다.)
'''

r, c = map(int, input().split())
k = int(input())
k_list = [list(map(int, input().split())) for _ in range(k)]
start_x, start_y = map(int, input().split())
direction = list(map(int, input().split()))

# 테스트
# r, c = 3, 3
# k = 1
# k_list = [[1, 0]]
# start_x, start_y = 1, 1
# direction = [1, 2, 3, 4] # 0 0

direction_info = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [[0] * c for _ in range(r)]
res_x, res_y = -1, -1
board[start_x][start_y] = 2
ck = [[0] * c for _ in range(r)]
ck[start_x][start_y] = 1

for i in range(k):
    board[k_list[i][0]][k_list[i][1]] = 1
    ck[k_list[i][0]][k_list[i][1]] = 1

x, y = start_x, start_y
while 1:
    flag = False

    for i in range(len(direction)):
        while 1:
            dx, dy = direction_info[direction[i] - 1]
            nx, ny = x + dx, y + dy

            # 범위 계산을 먼저 한 뒤 방문 여부를 체크해야 한다. 그렇지 않으면 인덱스 에러
            if nx < 0 or ny < 0 or nx >= r or ny >= c or board[nx][ny] != 0 or ck[nx][ny] == 1:
                break

            ck[nx][ny] = 1
            board[nx][ny] = 1
            flag = True
            x, y = nx, ny
            res_x, res_y = nx, ny

    if not flag:
        break

print(res_x, res_y)
