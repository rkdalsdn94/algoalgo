'''
    전형적인 다익스트라(dijkstra) 풀이 --> x까지 가는길, x에서 돌아오는 길의 합을 해야됨
in
    4 8 2
    1 2 4
    1 3 2
    1 4 7
    2 1 1
    2 3 5
    3 1 2
    3 4 4
    4 2 3
out
    10
'''
import heapq as hq
INF = int(1e9)

# n, m, x = map(int, input().split())
# g = [[] for _ in range(n + 1)] # 노드의 번호를 인덱스로 바로 사용할 수 있게하기 위해 +1을 했다
# distance = [INF] * (n + 1)     # 정방향 거리 계산
# g_reverse  = [[] for _ in range(n + 1)] # x에서 원래 집으로 돌아가는 거리(역방향) 위에 그래프(g)랑 더하야 됨
# distance_reverse = [INF] * (n + 1)      # 역방향 거리 계산
# res = 0

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     g[a].append((b, c))
#     g_reverse[b].append((a, c))

# 테스트
n, m, x = 4, 8, 2
g = [[], [(2, 4), (3, 2), (4, 7)], [(1, 1), (3, 5)], [(1, 2), (4, 4)], [(2, 3)]]
distance = [INF] * (n + 1)
g_reverse = [[], [(2, 1), (3, 2)], [(1, 4), (4, 3)], [(1, 2), (2, 5)], [(1, 7), (3, 4)]]
distance_reverse = [INF] * (n + 1)
res = 0

def dijkstra(s, g, distance):
    q = []
    distance[s] = 0
    hq.heappush(q, [0, s])

    while q:
        dist, now = hq.heappop(q)

        if distance[now] < dist:
            continue

        for i in g[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(q, (cost, i[0]))

# 각 집에서 x까지의 정뱡향 거리 계산
dijkstra(x, g, distance)
# 각 집에서 x까지의 역뱡향 거리 계산 (원래 집으로 돌아가는 거리)
dijkstra(x, g_reverse, distance_reverse)

for i in range(1, n + 1):
    res = max(res, distance[i] + distance_reverse[i])

print(res)
