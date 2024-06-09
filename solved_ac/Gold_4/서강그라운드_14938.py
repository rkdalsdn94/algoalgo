# 백준 - 골드4 - 서강그라운드 - 14938 - 그래프, 다익스트라(*), 최단 경로, 플로이드 와샬 문제
'''
그래프, 다익스트라, 최단 경로, 플로이드 와샬 문제

플로이드 와샬로도 풀 수 있는데, 현재 풀이에선 다익스트라로만 풀었다.
나중에 플로이드 와샬의 풀이를 추가할 수 있을 때 추가해야겠다.

풀이 과정
    1. 입력을 받고, 다익스트라 함수를 만든다.
    2. 다익스트라 함수를 이용해서 모든 정점에서 다른 정점까지의 최단 거리를 구한다.
    3. 모든 정점에서 다른 정점까지의 최단 거리를 구하고, 최대 아이템을 가지고 있는 정점을 찾는다.
    4. 최대 아이템을 가지고 있는 정점을 출력한다.

in
    5 5 4
    5 7 8 2 3
    1 4 5
    5 2 4
    3 2 3
    1 2 3
out
    23
'''

import sys; input=sys.stdin.readline
import heapq

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start):
    distance = [int(1e9)] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

res = 0

for i in range(1, n + 1):
    temp = dijkstra(i)
    temp_res = 0

    for j in range(1, n + 1):
        if temp[j] <= m:
            temp_res += item[j]

    res = max(res, temp_res)

print(res)
