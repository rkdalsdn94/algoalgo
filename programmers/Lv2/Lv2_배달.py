'''
다익스트라(dijkstra) 알고리즘
어제 푼 백준의 '파티-1238'도 역방향을 안하고 풀 수도 있을거 같다.
이따 시간날때 한번 풀어봐야겠다
'''
import heapq
INF = int(1e9)

def dijkstra(s, g, distance):
    q = []
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(N, road, K):
    answer = 0
    g = [[] for _ in range(N+1)]
    distance = [INF] * (N + 1)

    for a, b, c in road:
        g[a].append((b, c))
        g[b].append((a, c))
    
    dijkstra(1, g, distance)

    for i in distance:
        if i <= K:
            answer += 1

    return answer


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4

