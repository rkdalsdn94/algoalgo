# 백준 - 골드5 - 맥주 마시면서 걸어가기 - 9205 - 그래프, bfs 문제
'''
그래프, bfs 문제

bfs로 풀면 되는데 시뮬레이션 성격이 강한 문제이다.
50미터 단위로 20병의 맥주를 마시므로 도착지까지 거리 차이가 (편의점은 따로 계산)
    1000이 넘어가면 'sad'를 출력하고, 넘어가지 않으면 'happy'를 출력하면 된다.
중간의 편의점을 계산하는 경우를 bfs로 풀면 된다.

store_list로 nx, ny를 만든 후, 현재 출발 좌표인 q에 담아놓은 좌표를 a, b로 꺼낸다.
이 값으로 도착지까지의 거리가 1000이 안넘는지 확인해본 후, 1000 보다 크다면 편의점을 방문할 수 있는지 검사한다.
nx, ny의 값으로 편의점 좌표를 꺼낸 뒤 해당 편의점을 방문했는지 체크한다. (체크를 위해 ck 변수 활용)
거리를 계산하는 함수인 distance_check 를 이용해 편의과의 거리가 1000 이하이면 q와 ck 변수에 해당 편의점 좌표를 담고, bfs를 반복하면 된다.

distance_check 함수 : 편의점이나, 도착지까지의 거리 계산을 위한 함수
bfs 함수 : 편의점을 방문을 체크하기 위한 함수

in
    2
    2
    0 0
    1000 0
    1000 1000
    2000 1000
    2
    0 0
    1000 0
    2000 1000
    2000 2000
out
    happy
    sad
'''

from collections import deque

def distance_check(start_x, start_y, end_x, end_y):
    return abs(start_x - end_x) + abs(start_y - end_y)

def bfs(x, y):
    q = deque([(x, y)])
    ck = []

    while q:
        a, b = q.popleft()

        if distance_check(a, b, end_x, end_y) <= 1000:
            return True

        for i in store_list:
            nx, ny = i

            if [nx, ny] not in ck:
                if distance_check(a, b, nx, ny) <= 1000:
                    ck.append([nx, ny])
                    q.append([nx, ny])

t = int(input())
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    store_list = [ list(map(int, input().split())) for _ in range(n) ]
    end_x, end_y = map(int, input().split())

    res = bfs(start_x, start_y)
    print('happy' if res else 'sad')
