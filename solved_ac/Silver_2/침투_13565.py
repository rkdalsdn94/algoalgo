# 백준 - 실버2 - 침투 - 13655 - 그래프, bfs 문제
'''
그래프, bfs 문제

기본적인 bfs로 풀었다. 대신 처음에 문제를 잘못 이해해서 0 일때만 검사하는 건데, 1일때만 검사하고 '왜 틀렸을까' 했었다..
다음에 dfs로도 풀어보려고 한다.

풀이 과정
1. input 값을 잘 입력 받은 후, 제일 처음 입력받은 부분에서 0일때만 bfs를 실행한다.
2. bfs를 실행할 때 해당 x, y를 ck에 방문했다는 표시를 남기기 위해 1로 바꾸고, 해당 x, y를 q에 답는다.
3. q가 빌 때까지 while 반복문을 실행하고, while 안에서 다음 방문할 곳을 남동북서(dx, dy) 순으로 진행했다. -> 어떻게 진행하던 상관없다.
4. 새로운 x(a + i), y(b + j를 nx, ny라는 이름으로 담은 후, 해당 nx, ny가 n과 m의 범위를 벗어나는지
    이미 방문한 곳인지(ck[nx][ny] == 0), board에서 방문할 수 있는 곳인지(board[nx][ny] == 0) 검사한다.
5. 통과할 수 있으면 q에 nx, ny를 담은 후 ck에 방문했다는 표시를 남긴다.
6. ck에서 마지막 행 중에 1이 있으면 board를 통과할 수 있으므로 YES를 출력하고, 1이 없으면 NO를 출력하면 된다.
'''

from collections import deque

n, m = map(int, input().split())
board = [ input() for _ in range(n) ]

# 테스트
# n, m = 5, 6
# board = [ '010101', '010000', '011101', '100011', '001011' ] # NO
# n, m = 8, 8
# board = [  '11000111', '01100000', '00011001', '11001000',
#             '10001001', '10111100',  '01010000', '00001011' ] # YES

dx, dy = [1,0,-1,0], [0,1,0,-1]
ck = [ [0] * m for _ in range(n) ]

def bfs(x, y):
    ck[x][y] = 1
    q = deque([(x, y)])

    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and board[nx][ny] == '0':
                q.append([nx, ny])
                ck[nx][ny] = 1

for i in range(1):
    for j in range(m):
        if board[i][j] == '0':
            bfs(i, j)

if 1 in ck[n - 1]:
    print('YES')
else:
    print('NO')
