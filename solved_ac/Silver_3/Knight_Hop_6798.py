# 백준 - 실버3 - Knight Hop - 6798 - 그래프, bfs 문제
'''
그래프, bfs 문제
기존에 풀던 bfs 방식과 동일하게 bfs로 풀었다. (dfs도 가능할 것 같음)

풀이 과정
1. 나이트가 이동할 수 있는 방향을 dx, dy에 저장한다.
2. 시작점에서 bfs를 시작한다.
3. 목표 지점에 도달하면 결과값을 출력하고 종료한다.
'''

start_x, start_y = map(int, input().split())
end_x, end_y = map(int, input().split())

# 테스트
# start_x, start_y = 2, 1
# end_x, end_y = 3, 3 # 1
# start_x, start_y = 4, 2
# end_x, end_y = 7, 5 # 2

board = [[0] * 9 for _ in range(9)]
dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]

q = [(start_x, start_y, 0)]
board[start_x][start_y] = 1
res = 0

while q:
    x, y, cnt = q.pop(0)

    if x == end_x and y == end_y:
        res = cnt
        break

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 1 or nx >= 9 or ny < 1 or ny >= 9:
            continue

        if board[nx][ny] == 0:
            board[nx][ny] = 1
            q.append((nx, ny, cnt + 1))

print(res)
