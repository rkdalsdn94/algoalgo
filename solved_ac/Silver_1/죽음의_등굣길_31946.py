# 백준 - 실버1 - 죽음의 등굣길 - 31946 - 그래프, bfs 문제
'''
그래프, bfs 문제

풀이 과정
    - n, m을 입력받고, n x m 크기의 board를 입력받는다.
    - x를 입력받는다.
    - ck를 n x m 크기의 0으로 초기화한다.
    - ck[0][0]을 1로 초기화하고, (0, 0)을 q에 넣는다.
    - q가 빌 때까지 다음의 과정을 계산한다.
        - q에서 (a, b)를 꺼낸다.
        - i는 -x부터 x까지 반복하면서, j는 -x부터 x까지 반복하면서 다음의 과정을 계산한다.
            - abs(i) + abs(j)가 x보다 작거나 같다면, nx, ny를 a + i, b + j로 설정한다.
            - nx, ny가 board의 범위 내에 있고, board[nx][ny]가 board[a][b]와 같고,
              ck[nx][ny]가 0이라면, ck[nx][ny]를 1로 설정하고, (nx, ny)를 q에 넣는다.
    - ck[-1][-1]이 참이라면, ALIVE를 출력하고, 거짓이라면, DEAD를 출력한다.
'''

from collections import deque

n, m = int(input()), int(input())
board = [list(map(int, input().split())) for _ in range(n)]
x = int(input())

# 테스트
# n, m = 2, 3
# board = [[0, 0, 0], [0, 0, 0]]
# x = 1 # ALIVE
# n, m = 2, 2
# board = [[0, 0], [0, 1]]
# x = 5 # DEAD

ck = [[0] * m for _ in range(n)]
ck[0][0] = 1
q = deque([(0, 0)])

while q:
    a, b = q.popleft()

    for i in range(-x, x + 1):
        for j in range(-x, x + 1):
            if abs(i) + abs(j) <= x:
                nx, ny = a + i, b + j

                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == board[a][b] and ck[nx][ny] == 0:
                    ck[nx][ny] = 1
                    q.append((nx, ny))

if ck[-1][-1]:
    print('ALIVE')
else:
    print('DEAD')
