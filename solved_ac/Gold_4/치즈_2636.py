# 백준 - 골드4 - 치즈 - 2636 - 구현, 시뮬레이션, 그래프 문제
'''
구현, 시뮬레이션, 그래프 문제

bfs 방식으로 문제를 풀었다.

풀이 방식은 bfs를 (0, 0) 부터 시작해서 board의 제일 바깥에서 안으로 들어온다고 이해하면 된다.
단, bfs를 flag 기준으로 while 반복문으로 실행해야 된다. 새로 시작할 때마다 ck를 초기화한다.
치즈 부분(1)이 닿으면 해당 보드를 0으로 바꿔준다. 그리고 temp를 1씩 더해가며 몇 개의 치즈가 녹았는지 count한다.
치즈 부분이 아니면(0) q에 append한다.
마지막에 치즈가 녹은 부분이 없으면 즉, temp가 0이면 flag의 값을 변경해 bfs를 그만 실행하게 만든다.

출력할 땐 치즈가 녹은 횟수를 담은 list의 길이와 리스트의 마지막 값을 출력하면 된다.
'''

from collections import deque

n, m = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]

# # 테스트
# n, m = 13, 12
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
#     [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ] # 3  \  5

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
res = []
flag = True

def bfs():
    global flag
    q = deque([(0, 0)])
    temp = 0

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0:
                ck[nx][ny] = 1

                if board[nx][ny] == 0:
                    q.append([nx, ny])
                elif board[nx][ny] == 1:
                    board[nx][ny] = 0
                    temp += 1
    if temp == 0:
        flag = False
        return
    res.append(temp)

while flag:
    ck = [ [0] * m for _ in range(n) ]
    bfs()

print(len(res))
print(res[-1])
