# 백준 - 실버2 - 특정 거리의 도시 찾기 - 18352 - 그래프, bfs, 다익스트라(dijkstra) 문제
'''
그래프, bfs, 다익스트라(dijkstra) 문제

전형적인 다익스트라(데이크스트라라 문제이다.
정답을 출력하는 방식만 다를 뿐 프로그래머스 'Lv2. 배달' 문제와 풀이와 거의 유사하다. (기존 다익스트라 문제는 거의 비슷하게 풀었다..)

풀이 과정
 - input 값을 잘 입력 받고, 그래프로 사용할 g 변수를 n + 1 크기로 빈 리스트를 만든다.
 - A번 도시에서 B번 도시까지(road 변수) 거리 비용을 그래프(g) 변수에 1로 비용을 추가한다.  -> g[a].append([b, 1])
 - 정답으로 출력하고 거리 비용을 계산할 distance 변수를 n + 1 크기로 엄청 큰 숫자로 만들어 놓는다.
 - 다익스트라 함수를 실행 시키는 데 함수의 구조는 다음과 같다.
    - 함수의 인자로는 처음 위치를 정하기 위한 s, 초기화한 그래프인 g, 정답 출력을 위한 거리 비용 계산을 위한 distance
    - heap으로 사용하기 위해 빈 리스트를 생성해 놓고, 해당 거리를 0, 힙에 거리 비용과 출발 위치를 추가한다. -> 출발 위치의 거리 비용은 0이다.
    - q에서 거리 비용과, 현재 위치를 꺼내면서 거리 비용을 더 작은 값으로 바꿔나간다. 거리 비용을 더 작은 값으로 바꿀 때마다 q에 담는다.
        - 여기 안에서 조건문으로 거리 비용을 구하는 건데 해당 부분은 코드로 확인해도 어렵지 않을거 같다.

다익스트라를 잘 모른다면 나동빈님 유튜브나 다른 강의 영상들이 많이 있어서 다익스트라를 이해하고 오면 쉽게 풀 수 있다.
'''

import sys;input=sys.stdin.readline
import heapq as hq

INF = int(1e9)

n, m, k, x = map(int, input().split())
road = [ list(map(int, input().split())) for _ in range(m) ]
g = [ [] for _ in range(n + 1) ]

# 테스트
# import heapq as hq
# INF = int(1e9)
# n, m, k, x = 4, 4, 2, 1
# g = [ [] for _ in range(n + 1) ]
# road = [ [1, 2], [1, 3], [2, 3], [2, 4] ] # $
#############################################################################
# n, m, k, x = 4, 3, 2, 1
# g = [ [] for _ in range(n + 1) ]
# road = [ [1, 2], [1, 3], [1, 4] ] # -1
#############################################################################
# n, m, k, x = 4, 4, 1, 1
# g = [ [] for _ in range(n + 1) ]
# road = [ [1, 2], [1, 3], [2, 3], [2, 4] ] # 2  \  3

distance = [INF] * (n + 1)
flag = True

for i in road:
    a, b = i
    g[a].append([b, 1]) # 그래프 비용 1로 초기화

def dijkstra(s, g, distance):
    q = []
    distance[s] = 0
    hq.heappush(q, (0, s))

    while q:
        dist, now = hq.heappop(q)

        if distance[now] < dist: # 현재 거리 비용이 이전 거리 비용보다 작을 경우 갱신할 필요가 없다. (더 작은 거리 비용이 필요)
            continue

        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))

dijkstra(x, g, distance)

for i in range(1, len(distance)):
    if distance[i] == k:
        flag = False
        print(i)

if flag:
    print(-1)
