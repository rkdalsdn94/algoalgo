# 백준 - 골드5 - 택배 배송 - 5972 - 그래프, 다익스트라(dijkstra) 문제
'''
그래프, 다익스트라(dijkstra) 문제

뭔가 다익스트라(원래는 데이크스크라이지만)하면 아직 내가 많은 문제들을 만나지 못해서 이런 생각이 드는거 같긴 하지만, 정형화된 느낌이 있는거 같다.
어찌됐든 이 전에 풀었던 다익스트라 문제랑 똑같은 문제이다. 전에 풀었던 방식과 완전 동일하게 해도 문제가 풀린다.
'''

import heapq as hq

INF = int(1e9)

n, m = map(int, input().split())
g = [ [] for _ in range(n + 1) ]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

# 테스트
# g = [[], [[4, 4], [2, 1]], [[4, 0], [1, 1], [3, 6]],
#     [[6, 2], [2, 6], [4, 4]], [[5, 3], [2, 0], [1, 4], [3, 4]],
#     [[4, 3], [6, 1]], [[5, 1], [3, 2]]] # 5

distance = [INF] * (n + 1)

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

dijkstra(1, g, distance)
print(distance[n])
