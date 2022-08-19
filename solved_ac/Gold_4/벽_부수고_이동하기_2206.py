'''
bfs 문제

처음에는 2차원 배열로 flag를 하나 두고 벽을 부쉈는지 체크하면서 모든 경우의 수를 파악하려고 했었다.
역시 n의 범위 때문에 안돼서 다른 방법을 찾는데 생각이 잘 안 나 다른 사람의 풀이를 참고했는데,
벽을 부쉈는지 체크하는 부분을 3차원 배열로 해결이 가능하다는 아이디어를 보고 3차원 배열 방식으로 아래와 같이 다시 풀었다.

ck[n][m][벽을 부쉈는지 확인하는 부분] 마지막 부분이 1이면 이미 벽을 부순 상태이므로 더 이상 벽을 부수질 못한다.
그 후에 board에 범위를 넘어가지 않고 n, m의 끝까지 갈 수 있으면 ck[n][m][벽을 부쉈는지 확인하는 부분] + 1 씩 더해가며
n, m에 도착하면 해당 값 return
q가 빌 때까지 다 돌았는데 return을 못하면 -1로 풀면 된다.
'''

from collections import deque

n, m = map(int, input().split())
board = [ list(map(int, input())) for _ in range(n) ]

# 테스트
# n, m = 6, 4
# board = [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0],
#          [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]] # 15

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
ck = [ [ [0] * 2 for _ in range(m) ] for _ in range(n) ] # 3차원 배열로 벽을 부쉈는지 체크 0: 안 부숨, 1: 부숨

def bfs():
    q = deque([(0, 0, 0)])
    ck[0][0][0] = 1

    while q:
        a, b, c = q.popleft()

        if a == n - 1 and b == m - 1:
            return ck[a][b][c]
        
        for i, j in zip(dx, dy):
            nx, ny = i + a, j + b

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and ck[nx][ny][c] == 0:
                    ck[nx][ny][c] = ck[a][b][c] + 1
                    q.append([nx, ny, c])

                elif board[nx][ny] == 1 and c == 0:
                    ck[nx][ny][c + 1] = ck[a][b][c] + 1
                    q.append([nx, ny, c + 1])

    return -1

print(bfs())
