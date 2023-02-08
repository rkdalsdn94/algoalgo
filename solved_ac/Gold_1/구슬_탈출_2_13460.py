# 백준 - 골드1 - 구슬 탈출 2 - 13460 - 구현, 그래프, bfs, 시뮬레이션 문제
'''
구현, 그래프, bfs, 시뮬레이션 문제

bfs를 구현하는데 보통의(?) bfs라면 위, 아래, 오른쪽, 왼쪽 각각 한 칸씩 이동하겠지만
해당 문제에선 벽에 닿거나 O를 만날 때까지 진행한 방향으로 계속 이동해야 된다. (문제 조건 중 중력을 이용해서 기울여야 된다고 해서 그렇다다)
또한, 빨간 구슬, 파란 구슬 실행 시점이 같아야 되므로 ck 변수가 [0] * m으로 n 개의 리스트, 
따라서, 빨간 구슬을 움직이면 파란 구슬도 움직여야 한다. -> 기울이는 것이기 때문에 빨간 파란 구슬 모두 움직여야 한다.
중력의 기능을 move 함수를 통해 구현했고, 구현 내용은 구슬이 벽에 닿거나 구멍에 빠지기 전까지 이동한 후 해당 위치와 이동한 횟수를 반환한다.

나머지 추가 설명은 코드 옆 주석으로 적어놨다.

** 추가 **
이전까지 bfs를 풀 때 항상 dx, dy를 zip으로 묶어 각각의 방향을 검사하는 식으로 구현했는데
이 문제에서 계속 시간 초과가 나서 다른 사람 풀이를 참고해 direction으로 바꾼 후 range 4로 각각의 인덱스를 검사하니까 통과했다.
zip 함수 연산의 비용이 생각보다 더 많이 드는 거 같다...
'''

from collections import deque

n, m = map(int, input().split())
board = [ input() for _ in range(n) ]

# 테스트
# n, m = 5, 5
# board = [ '#####', '#..B#', '#.#.#', '#RO.#', '#####' ] # 1
# n, m = 7, 7
# board = [ '#######', '#...RB#', '#.#####', '#.....#', '#####.#', '#O....#', '#######' ] # 5
# n, m = 7, 7
# board = [ '#######', '#..R#B#', '#.#####', '#.....#', '#####.#', '#O....#', '#######' ] # 5
# n, m = 10, 10
# board = [
#     '##########', '#R#...##B#', '#...#.##.#', '#####.##.#',
#     '#......#.#', '#.######.#', '#.#....#.#',
#     '#.#.#.#..#', '#...#.O#.#', '##########'
# ] # -1
# n, m = 3, 7
# board = [ '#######', '#R.O.B#', '#######' ] # 1
# n, m = 10, 10
# board = [
#     '##########', '#R#...##B#', '#...#.##.#', '#####.##.#',
#     '#......#.#', '#.######.#', '#.#....#.#',
#     '#.#.##...#', '#O..#....#', '##########'
# ] # 7
# n, m = 3, 10
# board = [ '##########', '#.O....RB#', '##########' ] # -1

rx, ry, bx, by = 0, 0, 0, 0
dx, dy = [1,0,-1,0], [0,1,0,-1]
ck = set() # 방문한 곳인지 체크

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

def move(x, y, direction): # 각각의 구슬이 벽에 닿거나 구멍에 빠질 때까지 이동한 후, 마지막 도착 위치와 이동한 횟수를 반환한다.
    cnt = 0

    while board[x + dx[direction]][y + dy[direction]] != '#' and board[x][y] != 'O':
        x, y = x + dx[direction], y + dy[direction]
        cnt += 1

    return x, y, cnt

def bfs(rx, ry, bx, by):
    q = deque()
    q.append([rx, ry, bx, by, 1])

    while q:
        rx, ry, bx, by, cnt = q.popleft()
        ck.add((rx, ry, bx, by))

        if cnt > 10: # 10번이 넘어가면 -1을 출력하고 프로그램 종료
            print(-1)
            exit(0)

        for direction in range(4): # 4(상, 하, 좌, 우) 방향을 위해
            r_nx, r_ny, r_cnt = move(rx, ry, direction) # 각각의 cnt는 이동한 횟수이다.
            b_nx, b_ny, b_cnt = move(bx, by, direction)

            if board[b_nx][b_ny] == 'O': # 파란 구슬이 먼저 구멍에 빠지면 해당 경우는 무시한다.
                continue
            if board[r_nx][r_ny] == 'O': # 빨간 구슬이 구멍에 빠지면 해당 cnt를 출력한다.
                print(cnt)
                exit(0)

            if r_nx == b_nx and r_ny == b_ny:
                if r_cnt > b_cnt: # r_cnt와 b_cnt 중 값이 더 큰 cnt가 더 많이 이동한 것이므로 늦게 이동한 구슬의 한 칸 뒤로 보낸다.
                    r_nx, r_ny = r_nx - dx[direction], r_ny - dy[direction]
                else:
                    b_nx, b_ny = b_nx - dx[direction], b_ny - dy[direction]

            if (r_nx, r_ny, b_nx, b_ny) not in ck: # 새로 이동한 위치가 방문한 곳인지 체크한다. 방문을 안했으면 아래 코드 실행
                ck.add((r_nx, r_ny, b_nx, b_ny))
                q.append([r_nx, r_ny, b_nx, b_ny, cnt + 1])
    print(-1) # 구슬을 10회를 안 굴려도 구멍에 통과할 수 없을 때

bfs(rx, ry, bx, by)
