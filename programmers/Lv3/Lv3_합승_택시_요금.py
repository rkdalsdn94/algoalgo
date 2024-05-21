# 프로그래머스 - Lv3 - 합승 택시 요금 - 그래프, 다익스트라 문제
'''
그래프, 다익스트라 문제

기본적인 다익스트라 문제이다.
플로이드 워셜로도 풀 수 있다고 하는데, 다익스트라로 풀었다.

풀이 과정
    1. n, s, a, b, fares가 주어진다.
    2. fares를 이용해서 그래프를 만든다. g[i].append((j, c))로 만들어준다.
    3. 다익스트라를 이용해서 s에서 각 노드까지의 거리를 구한다.
    4. s에서 각 노드까지의 거리 + 각 노드에서 a, b까지의 거리를 구해서 최솟값을 구한다.
    5. 최솟값을 출력한다.
'''

import heapq

def dijkstra(start, g):
    q = []
    heapq.heappush(q, (0, start))
    distance = [int(1e9)] * (len(g))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

def solution(n, s, a, b, fares):
    answer = int(1e9)
    g = [[] for _ in range(n + 1)]

    for i, j, c in fares:
        g[i].append((j, c))
        g[j].append((i, c))

    s_distance = dijkstra(s, g)

    for i in range(1, n + 1):
        a_distance = dijkstra(i, g)
        answer = min(answer, s_distance[i] + a_distance[a] + a_distance[b])

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])) # 14
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 9], [1, 6, 14], [3, 6, 9]])) # 18
