# 백준 - 골드5 - 와드 - 23747 - 구현, 시뮬레이션, 그래프, bfs 문제
'''
구현, 시뮬레이션, 그래프, bfs 문제

와드를 설치한 곳에서 해당 문자열의 bfs를 돌면서 '#'을 '.'으로 바꾸면 된다.
최종 위치에서는 최종 위치를 포함한 상하 좌우의 '#'을 '.'으로 바꾸면 된다.

han_move로 이동
    - U : 위로 이동 (행을 1 감소)
    - D : 아래로 이동 (행을 1 증가)
    - L : 왼쪽으로 이동 (열을 1 감소)
    - R : 오른쪽으로 이동 (열을 1 증가)
    - W : 와드 설치(현재 단어와 같은 문자열을 가진 곳을 '.'으로 바꾸기, 이때 bfs 사용)
정답으로 출력할 때
    - '.' : 시야가 확보된 곳
    - '#' : 시야가 확보되지 않은 곳

풀이 과정
    1. r, c를 입력받는다.
    2. g를 입력받는다.
    3. han_r, han_c를 입력받는다.
    4. han_move를 입력받는다.
    5. han_r, han_c를 각각 -1씩 해준다.
    6. res를 만들어서 '.'로 초기화한다.
    7. ck를 만들어서 0으로 초기화한다.
    8. (a, b, word)를 인자로 받는 bfs 함수를 만든다.
        8.1. q를 만들어 (a, b, word)를 넣는다.
        8.2. dx, dy를 만들어 각각 [0, 1, 0, -1], [1, 0, -1, 0]을 넣는다.
        8.3. q가 빌 때까지 다음을 반복한다.
            8.3.1. x, y, w를 q에서 꺼낸다.
            8.3.2. ck[x][y]를 1로 바꾼다.
            8.3.3. res[x][y]를 '.'로 바꾼다.
            8.3.4. nx, ny를 각각 dx, dy 더해 범위가 벗어났는지, ck가 0인지, g[nx][ny]가 w인지 확인한다.
            8.3.5. 위 조건을 만족하면 q에 (nx, ny, w)를 넣고 ck[nx][ny]를 1로 바꾸고, res[nx][ny]를 '.'로 바꾼다.
    9. han_move를 돌면서 다음을 확인한다.
        9.1. W이고, ck[han_r][han_c]의 위치를 방문하지 않았다면 bfs를 실행한다.
        9.2. U라면 han_r을 1 감소시킨다.
        9.3. D라면 han_r을 1 증가시킨다.
        9.4. L라면 han_c를 1 감소시킨다.
        9.5. R라면 han_c를 1 증가시킨다.
    10. han_r, han_c를 기준으로 현재 위치를 포함하여 상하 좌우를 '.'로 바꾼다.
    11. res를 출력한다.
'''

from collections import deque

r, c = map(int, input().split())
g = [list(input()) for _ in range(r)]
han_r, han_c = map(int, input().split())
han_move = list(input())

# 테스트
# r, c = 4, 5
# g = [
#     list('aaabc'), list('dcbbc'),
#     list('dccaa'), list('ddaaa'),
# ]
# han_r, han_c = 3, 4
# han_move = list('WLLLWUURRD')
# '''
#     ##.##
#     ....#
#     .#...
#     .....
# '''
# r, c = 3, 3
# g = [ list('abc'), list('def'), list('ghi') ]
# han_r, han_c = 2, 2
# han_move = list('LU')
# '''
#     ..#
#     .##
#     ###
# '''

han_r, han_c = han_r - 1, han_c - 1
res = [list('#' * c) for _ in range(r)]
ck = [[0] * c for _ in range(r)]

def bfs(a, b, word):
    q = deque([(a, b, word)])
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y, w = q.popleft()
        ck[x][y] = 1
        res[x][y] = '.'

        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j

            if 0 <= nx < r and 0 <= ny < c and not ck[nx][ny] and g[nx][ny] == w:
                q.append((nx, ny, w))
                ck[nx][ny] = 1
                res[nx][ny] = '.'

for i in han_move:
    if i == 'W' and ck[han_r][han_c] == 0:
        bfs(han_r, han_c, g[han_r][han_c])
    elif i == 'U':
        han_r -= 1
    elif i == 'D':
        han_r += 1
    elif i == 'L':
        han_c -= 1
    elif i == 'R':
        han_c += 1

for i, j in zip([0, 0, 1, 0, -1], [0, 1, 0, -1, 0]):
    nx, ny = han_r + i, han_c + j

    if 0 <= nx < r and 0 <= ny < c:
        res[nx][ny] = '.'

for i in res:
    print(''.join(i))
