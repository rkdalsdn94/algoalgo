'''
단순하게 bfs로 풀었다.

처음 양의 숫자와 늑대의 숫자를 구해놓은 놓고, -->( *주석1* 부분 ) 
bfs 함수가 실행 될 때 while을 돌면서 하나의 울타리 안에 있는 양의 숫자와 늑대의 수를 구하고,
while문이 끝나는 지점에서 전체 구해놓은 양의 숫자와, 늑대의 숫자를 비교하며 빼준다

'''

from collections import deque

r, c = map(int, input().split())
yard = [ list(input()) for _ in range(r) ]

# 테스트
# r, c = 6, 6
# yard = [ list('...#..'), list('.##v#.'), list('#v.#.#'), list('#.o#.#'), list('.###.#'), list('...###') ] # 0 2
# r, c = 8, 8
# yard = [ list('.######.'), list('#..o...#'), list('#.####.#'), list('#.#v.#.#'), list('#.#.o#o#'), list('#o.##..#'), list('#.v..v.#'), list('.######.') ] # 3 1
# r, c = 9, 12
# yard = [ list('.###.#####..'), list('#.oo#...#v#.'), list('#..o#.#.#.#.'), list('#..##o#...#.'), list('#.#v#o###.#.'), list('#..#v#....#.'), list('#...v#v####.'), list('.####.#vv.o#'), list('.......####.') ] # 3 5

ck = [[0] * c for _ in range(r)]
o_cnt, v_cnt = 0, 0

def bfs(i, j):
    global o_cnt, v_cnt

    temp_o, temp_v = 0, 0
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    q = deque([(i, j)])
    ck[i][j] = 1

    if yard[i][j] == 'o': temp_o += 1
    else: temp_v += 1

    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < r and 0 <= ny < c and ck[nx][ny] == 0 and yard[nx][ny] != '#':
                ck[nx][ny] = 1

                if yard[nx][ny] == 'o': temp_o += 1
                elif yard[nx][ny] == 'v': temp_v += 1
                
                q.append([nx, ny])
    
    if temp_o > temp_v: v_cnt -= temp_v
    else: o_cnt -= temp_o

for i in range(r):  # 양과 늑대 숫자 구하기 ( *주석1* )
    for j in range(c):
        if yard[i][j] == 'o': o_cnt += 1
        elif yard[i][j] == 'v': v_cnt += 1

for i in range(r):
    for j in range(c):
        if yard[i][j] == 'o' or yard[i][j] == 'v':
            bfs(i, j)


print(o_cnt, v_cnt)

