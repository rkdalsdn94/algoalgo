# 백준 - 실버1 - 스타트링크 - 5014 - 그래프, bfs 문제
'''
그래프, bfs 문제

F : 총 건물의 층
G : 도착해야 하는 지점
S : 현재 강호가 있는 층
U : 한 번 눌렀을 때 위로 가는 층 (만약 U가 3이고, 강호가 1층에 있으면 U를 한 번 눌렀을 때 4층으로 이동)
D : 한 번 눌렀을 대 아래로 가는 층 (위의 예에서 반대로 생각하면 된다.)

위와 같은 조건으로 있을 때 문제 분류의 bfs 로 되어있는 걸 보고 금방 풀 수 있었다.
    (평소에 그래프 관련 문제를 풀 때 거의 2차원 배열로만 풀다가 1차원 배열로 푸는게 더 까다로운 느낌이다.)

ck 를 정답으로 출력하기 위해 사용. 처음 시작이 1로 시작되어서 마지막 출력해야 될 때는 1층을 빼고 시작해야 된다. (강호가 있는 층을 표시하기 위해)
올라가는 버튼 내려가는 버튼은 dx로 [U, -D] 로 만들었다.
그리고 현재 위치인 S를 q에 담고 while 문으로 bfs를 실행하면 된다.
while 문 내에서 현재 위치가 도착하는 층에 닿으면 위에 적어놨듯이 1을 빼고 출력하면 된다.

nx는 dx 와 더한 값으로 0보다 크고 F를 넘지 않고, 방문한 적이 없는 곳이면
    - q에 담고, 엘리베이터를 한 번 이동했다는 표시로 ck에 이전 값 + 1을 한다.
while 문을 다 돌고도 출력이 없으면 엘리베이터로 이동할 수 없는 곳이므로 'use the stairs' 를 출력하면 된다.
'''

from collections import deque

F, S, G, U, D = map(int, input().split())

# 테스트
# from collections import deque
# F, S, G, U, D = 10, 1, 10, 2, 1 # 6
# F, S, G, U, D = 100, 2, 1, 1, 0 # use the stairs

ck = [0] * (F + 1)
dx = [U, -D]
q = deque([S])
ck[S] = 1

while q:
    a = q.popleft()

    if a == G:
        print(ck[G] - 1)
        exit(0)
    
    for i in dx:
        nx = a + i

        if 0 < nx <= F and not ck[nx]:
            q.append(nx)
            ck[nx] = ck[a] + 1

print('use the stairs')
