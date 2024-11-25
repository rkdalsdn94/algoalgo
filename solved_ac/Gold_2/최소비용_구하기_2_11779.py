# 백준 - 골드3 - 최소비용 구하기 2 - 11779 - 그래프, 최단 경로, 다익스트라(dijkstra) 문제
'''
그래프, 최단 경로, 다익스트라(dijkstra) 문제

다익스트라 알고리즘을 사용하는데, 이전 노드를 저장하여 경로를 출력해야 된다.
그래서 이전 노드를 저장하는 nearest 리스트를 만들어서 해결했다.

풀이 과정
    1. 다익스트라(dijkstra) 알고리즘을 사용하여 최단 경로를 구한다.
    2. 최단 경로를 구하는 과정에서 이전 노드를 저장한다.
    3. 최단 경로를 출력한다.

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
    3
    1 3 5
'''

import heapq

n, m = int(input()), int(input())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])

start, end = map(int, input().split())
nearest = [0] * (n + 1)
distance = [1e9] * (n + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                nearest[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance[end]) # start -> end 최단 거리

path = [end]
while nearest[end] != start:
    path.append(nearest[end])
    end = nearest[end]
path.append(start)
print(len(path)) # 경로 길이

print(*path[::-1]) # 경로 출력
