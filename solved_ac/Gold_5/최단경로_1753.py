'''
다익스트라 문제

이 전에 Gold_3/파티_1238.py라는 위치에 있는 문제랑 완전히 동일하게 풀었다.

근데, 변수를 입력받을 때 식별자를 좀 더 신경 써야겠다.
예제에 주어진 값으로 테스트를 만든 후(하드코딩으로) 진행했을 때는 괜찮았는데,
input으로 입력받고 진행했을 때는 정답의 마지막인 INF가 출력이 되지 않았다.

왜 그런지 디버깅을 진행하다보니 distance값이 하나 덜 들어왔었다.
그래서 코드를 다시 살펴보니 처음 v, e로 정점과 간선을 입력 받은 후에,
그래프(g)를 초기화하는 과정에서 문제가 발생했다.

문제에 적혀져 있는 그대로 u, v, w 이런 식으로 입력받았는데,
그 후, distance를 초기화할 때 내가 원하는 정점에서 + 1의 값이 아닌
나중에 입력받은 간선 정보의 v로 바뀌어서 초기화가 잘못돼 있었다.

그래서 a, b, c로 바꾼 후에 Pypy3로 제출하니까 통과됐다.(python3는 시간 초과 나온다.)
'''

import heapq as hq
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())
g = [ [] for _ in range(v + 1) ]

for _ in range(e):
    # u, v, w = map(int, input().split()) # 이 부분에서 문제가 발생했다. 위에 v, e의 변수가 동일한 식별자로 받기 때문에 distance를 초기화 시킬때 이상하게 됐었다.
    # g[u].append((v, w))
    a, b, c = map(int, input().split())
    g[a].append((b, c))
# print(g)

# 테스트
# v, e = 5, 6
# k = 1
# g = [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]] # 0 \n 2 \n 3 \n 7 \n INF

distance = [INF] * (v + 1)

def dijkstra(k, g, distance):
    q = []
    distance[k] = 0
    hq.heappush(q, (0, k))

    while q:
        dist, now = hq.heappop(q)

        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))

dijkstra(k, g, distance)

for i in range(1, v + 1):
    print('INF' if distance[i] == INF else distance[i])
