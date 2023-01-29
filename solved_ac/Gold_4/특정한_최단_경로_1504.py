# 백준 - 골드4 - 특정한 최단 경로 - 1504 - 데이크스트라(dijkstra, 다익스트라라 문제
'''
데이크스트라(dijkstra, 다익스트라라 문제

데이크스트라 문제이다. 경로를 구하는 비용은 기존에 풀던 방식과 똑같은데, dijkstra를 실행하는 방식에 대해 고민을 해야된다.
1부터 시작해서 거쳐야 되는 지점을 방문하고, n으로 도착해야 된다.
res_1은 1부터 v1 -> v1부터 v2 -> v2부터 n 까지 가면 된다.
res_2은 1부터 v2 -> v2부터 v1 -> v1부터 n 까지 가면 된다.

제일 아래 조건에 맞으면 -1을 출력 아니면 두 값중 더 작은 값을 출력하면 된다.

input 을 sys.stdin.readline 으로 몽키패칭 해야 시간 초과가 안난다.
'''

import sys; input = sys.stdin.readline
import heapq as hq

INF = int(1e9)

n, e = map(int, input().split())
g = [ [] for _ in range(n + 1) ]

for i in range(e):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

v1, v2 = map(int, input().split())

# 테스트
# n, e = 4, 6
# g = [[], [[2, 3], [3, 5], [4, 4]], [[1, 3], [3, 3], [4, 5]], [[2, 3], [4, 1], [1, 5]], [[3, 1], [2, 5], [1, 4]]]
# v1, v2 = 2, 3 # 7

def dijkstra(start, end):
    distance = [INF] * (n + 1)
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

    return distance[end]

res_1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
res_2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if res_1 >= INF and res_2 >= INF:
    print(-1)
else:
    print(min(res_1, res_2))
