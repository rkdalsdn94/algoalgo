
'''
bfs 문제

101로 곱한 이유는 입력받는 숫자 값을 인덱스로 사용하려고 그렇게 입력받고,
나머진 bfs 푸는 방식대로 q를 이용했다.
행, 열이 있는 board가 아니여서 dx, dy는 사용할 필요가 없다.
시작 위치인 1부터 q로 시작하면서 주사위 숫자인 1 ~ 6까지 반복문을 통해서 방문을 하지 않았으면 검사하는 방식으로 풀었다.
'''

from collections import deque

board = [0] * 101
ck = [0] * 101
q = deque([1])
ladder, snake = dict(), dict()
ladder_cnt, snake_cnt = map(int, input().split())

for _ in range(ladder_cnt):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(snake_cnt):
    a, b = map(int, input().split())
    snake[a] = b
# # print(ladder, snake)

# 테스트
# ladder_cnt, snake_cnt = 3, 7
# ladder = {32: 62, 42: 68, 12: 98}
# snake = {95: 13, 97: 25, 93: 37, 79: 27, 75: 19, 49: 47, 67: 17} # 3
# ladder_cnt, snake_cnt = 4, 9
# ladder = {8: 52, 6: 80, 26: 42, 2: 72}
# snake = {51: 19, 39: 11, 37: 29, 81: 3, 59: 5, 79: 23, 53: 7, 43: 33, 77: 21} # 5

while q:
    a = q.popleft()
    ck[a] = 1

    for i in range(1, 7):
        nx = a + i

        if 0 < nx <= 100 and ck[nx] == 0:
            if nx in ladder.keys():
                nx = ladder[nx]
            
            if nx in snake.keys():
                nx = snake[nx]
            
            if ck[nx] == 0:
                q.append(nx)
                ck[nx] = 1
                board[nx] = board[a] + 1

print(board[100])
