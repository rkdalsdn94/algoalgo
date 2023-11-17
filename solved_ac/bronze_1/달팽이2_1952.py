# 백준 - 브론즈1 - 달팽이2 - 1952 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

수학으로 푸려면 2 * min(n, m) - 2 + (n > m) 이렇게 풀면 되지만 달팽이를 구현해보고 싶어 달팽이를 만들어서 풀었다.
달팽이를 만들 때 방향을 바뀌는 부분이 꺾어지는 부분이므로 그때 res를 1씩 증가시키면 된다.
dx, dy를 [우 하 좌 상] 으로 만들고 범위에서 벗어날 때 방향을 다시 수정하면 된다.

https://pythontutor.com/visualize.html#mode=edit 여기서 한 단계씩 돌려면 된다.
'''

n, m = map(int, input().split())

# 테스트
# n, m = 5, 3 # 5

board = [[0] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
i, j, direction, cnt = 0, 0, 0, 1
board[i][j] = cnt
cnt += 1
res = 0

while cnt <= n * m:
    nx, ny = i + dx[direction], j + dy[direction]

    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
        i, j = nx, ny
        board[nx][ny] = cnt
        cnt += 1
    else:
        direction = (direction + 1) % 4
        res += 1

print(res)
