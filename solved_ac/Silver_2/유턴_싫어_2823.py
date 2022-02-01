'''
도로를 지나다가 주변(상하좌우)에 지나갈 수 있는 도로의 수가 2이상이 되면 무조건 유턴을 해야된다(지나온 방향을 건너야 된다.)
그때 res(==flag)를 수정한 다음 그 값을 리턴한다.
'''

from collections import deque

r, c = map(int, input().split())
road = [ list(input()) for _ in range(r) ]

# 테스트
# r, c = 4, 3
# road = [ list('XXX'), list('X.X'), list('X.X'), list('XXX') ] # 1
# r, c = 5, 5
# road = [list('XX.XX'), list('X...X'), list('.....'), list('X...X'), list('XX.XX')] # 1 
# r, c = 3, 9
# road = [ list('...XXX...'), list('.X.....X.'), list('...XXX...') ] # 0

ck = [ [0] * c for _ in range(r) ]
res = False

def bfs(i, j):
    global res
    q = deque([(i, j)])
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    ck[i][j] = 1

    while q:
        cnt = 0
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < r and 0 <= ny < c and road[nx][ny] != 'X':
                cnt += 1
                
                if ck[nx][ny] == 0:
                    ck[nx][ny] = 1
                    q.append([nx, ny])

        if cnt < 2:
            res = True
            return res

for i in range(r):
    for j in range(c):
        if road[i][j] == '.':
            bfs(i, j)
        
        if res: break
    if res: break

print(int(res))


