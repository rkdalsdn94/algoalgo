'''
처음에 비트마스크을 생각하지 못하고 문제를 풀려고 하다가
인터넷에 검색해보니 비트마스크를 사용하면 좀 더 쉽게 풀 수 있었던거 같다
https://yabmoons.tistory.com/102 이 분의 글을 참고해서 비트마스크 공부도 했었다
위에 글에선 cpp로 풀었지만 설명을 너무 잘 적어놔서 읽을때도, 이해할때도 편하게 볼 수 있었다
'''

from collections import deque

n, m = map(int, input().split())
maze = list(list(input()) for _ in range(n))
# 테스트
# n, m = 1, 7
# maze = [list('f0.F..1')] 7
# n, m = 5, 5
# maze = [list('....1'), list('#1###'), list('.1.#0'), list('....A'), list('.1.#.')] # -1
# n, m = 7, 8
# maze = [list('a#c#eF.1'), list('.#.#.#..'), list('.#B#D###'), list('0....F.1'), list('C#E#A###'), list('.#.#.#..'), list('d#f#bF.1')] # 55
ck = [[[0] * 64 for _ in range(m)] for _ in range(n)]

def bfs(maze, i, j, ck):
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    ck[i][j][0] = 1
    q = deque([(i, j, 0, 0)])

    while q:
        a, b, cnt, key = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#' and ck[nx][ny][key] == 0:
                if maze[nx][ny] == '.':
                    ck[nx][ny][key] = 1
                    q.append([nx, ny, cnt + 1, key])
            
                if maze[nx][ny] == '1':
                    cnt += 1
                    return cnt
                
                if maze[nx][ny].isupper():
                    if key & 1 << (ord(maze[nx][ny]) - ord('A')):
                        ck[nx][ny][key] = 1
                        q.append([nx, ny, cnt + 1, key])
                
                if maze[nx][ny].islower():
                    newKey = key | (1 << ord(maze[nx][ny]) - ord('a'))
                    if ck[nx][ny][newKey] == 0:
                        ck[nx][ny][newKey] = 1
                        q.append([nx, ny, cnt + 1, newKey])

    return -1

for i in range(n):
    for j in range(m):
        if maze[i][j] == '0':
            maze[i][j] = '.'
            res = bfs(maze, i, j, ck)
            break

print(res)
