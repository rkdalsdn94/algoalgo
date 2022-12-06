# 백준 - 1916 - 최소비용 구하기 - 골드5 - 다익스트라(dijkstra), 그래프 문제
'''
다익스트라(dijkstra), 그래프 문제

전형적인 다익스트라 문제이다. 다익스트라 알고리즘을 공부하면 쉽게 풀 수 있다.

풀이 과정
1. input 값들을 잘 입력받은 후 출력할 때 사용할 distance를 n + 1의 크기로 만든다. (입력값 그대로 사용하기 위해 + 1을 했다.)
2. 그래프(g)에다 a부터 b까지의 버스 비용을 넣어준다.
3. 시작 지점(start)으로 다익스트라를 시작하고 출력으로 distance[end]로 출력하면 된다.
    3.1. 다익스트라 안에서 시작 지점의 거리를 0으로 초기화 한 후 heapq에 0(현재 위치이므로 비용이 0이다.)과 시작 위치를 넣어준다.
    3.2. hq에서 값을 하나씩 꺼내면서 거리를 비교하면서 distance[now]의 값을 더 작은 값으로 만들어준다.
4. res를 출력한다

in
    5
    8
    1 2 2
    1 3 3
    1 4 1
    1 5 10
    2 4 2
    3 4 1
    3 5 1
    4 5 3
    1 5
out
    4
'''

import sys; input = sys.stdin.readline
import heapq as hq

INF = int(1e9)

n, m = int(input()), int(input())
g = [ [] for _ in range(n + 1) ]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])

start, end = map(int, input().split())

def dijkstra(start, g, distance):
    q = []
    distance[start] = 0
    hq.heappush(q, (0, start))

    while q:
        dist, now = hq.heappop(q)

        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))

dijkstra(start, g, distance)

print(distance[end])
