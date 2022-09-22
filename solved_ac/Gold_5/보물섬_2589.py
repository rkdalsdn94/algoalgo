# 백준 - 보물섬 - 골드5 - bfs, 완전 탐색 문제
'''
bfs, 완전 탐색 문제

PyPy3로 제출해야 된다.

풀이 과정은 기본적인 bfs 문제이다.
'L'로 들어오는 모든 부분을 bfs 탐색을 해야 된다. -> 처음에 이 부분을 놓치고 전역으로 방문한 곳인지 체크를 해서 틀렸었다...
                                               -> 'L' 일때마다 새로운 ck 변수를 만들어줘야 된다.

풀이과정
1. 보물 지도(treasure_map)를 입력 받는다.
2. 보물 지도의 크기만큼 (l, w) 반복하면서 해당 인덱스가 'L'인지 찾는다.
    2.2 찾은 인덱스의 원소가 'L' 이면 보물 지도 크기만큼 방문한 곳인지 확인하기 위해 ck 변수를 만든다.
    2.3 deque에 i, j 인덱스 값을 넣어준 후 끝까지 방문했을 때 몇 번째인지 확인하기 위해 끝에 초기 값인 0을 넣어준다. -> 이게 나중에 c가 된다.
    2.4 값을 비교하기 위해 temp 변수를 만든다. -> c와 비교
    2.5 q에서 하나씩 꺼내면서 상, 하, 좌, 우로 bfs를 시작한다.
    2.6 해당 위치가(nx, ny)가 보물 지도의 크기를 벗어나지 않으며(0 <= nx < l and 0 <= ny < w)
         - 방문하지 않은 노드이고 (ck[nx][ny] == 0),
         - 'L'이면(treasure_map[nx][ny] == 'L')
    2.7 q에 새로운 위치인 (nx, ny, 이 전 값에 + 1한 값)을 넣어준 후 ck변수에 방문했다는 표시를 한다.
    2.8 bfs를 다 실행 후 res와 값을 비교한 후에 나중에 res를 출력하면 된다.
3. 'L'이 아니면 무시한다.
'''
import sys; input = sys.stdin.readline
from collections import deque

l, w = map(int, input().split())
treasure_map = [ input() for _ in range(l) ]

# 테스트
# l, w = 5, 7
# treasure_map = ['WLLWWWL', 'LLLWLLL', 'LWLWLWW', 'LWLWLLL', 'WLLWLWW'] # 8

dx, dy = [1,0,-1,0], [0,1,0,-1]
res = 0
q = deque()

def bfs(q):
    temp = -1

    while q:
        a, b, c = q.popleft()
        ck[a][b] = 1
        temp = max(temp, c)

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < l and 0 <= ny < w and ck[nx][ny] == 0 and treasure_map[nx][ny] == 'L':
                ck[nx][ny] = 1
                q.append([nx, ny, c + 1])

    return temp

for i in range(l):
    for j in range(w):
        # if treasure_map[i][j] == 'L' and ck[i][j] == 0: # 이렇게 했었어서 틀렸었다....
        if treasure_map[i][j] == 'L':
            ck = [ [0] * w for _ in range(l) ]
            q.append([i, j, 0])
            res = max(res, bfs(q))

print(res)