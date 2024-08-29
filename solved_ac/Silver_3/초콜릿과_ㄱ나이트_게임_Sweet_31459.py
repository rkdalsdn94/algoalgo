# 백준 - 실버3 - 초콜릿과 ㄱ나이트 게임 Sweet - 31459 - 그리디 문제
'''
그리디 문제

단순하고 그리디하게 풀었다.
board의 크기를 입력보다 넓게 잡고,
현재 위치(i, j)와 x2, y2를 더해 방문하지 않은 곳이면 방문했다는 표시와 res를 1 증가시킨다.
이러한 방식으로 풀면 된다.


풀이 과정
    1. 테스트 케이스와 테스트 케이스를 반복하면서 x1, y1, x2, y2를 입력을 받는다.
    2. board의 크기를 입력보다 크게(100 * 100) 설정하고, board를 만들어 준다.
    3. res를 0으로 초기화한다.
    4. y1를 행으로 x1을 열로 2중 반복문을 만든다.
        4.1. 현재 방문중인 i와 j의 각각 y2, x2를 더해 nx, ny를 만든다.
        4.2. board[nx][ny]와 board[i][j]가 0이면 방문하지 않은 곳이므로 방문했다는 표시를 하고 res를 1 증가시킨다.
    5. res를 출력한다.

in
    4
    4 4 1 1
    5 5 1 1
    6 6 1 2
    10 10 50 50
out
    10
    15
    24
    100
'''

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    board = [[0] * 100 for _ in range(100)]
    res = 0

    for i in range(y1):
        for j in range(x1):
            nx, ny = i + y2, j + x2

            if board[nx][ny] == 0 and board[i][j] == 0:
                board[i][j] = 1
                board[nx][ny] = 1
                res += 1

    print(res)
