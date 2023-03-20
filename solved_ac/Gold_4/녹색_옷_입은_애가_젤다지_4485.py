# 백준 - 골드4 - 녹색 옷 입은 애가 젤다지? - 4485 - 그래프, 데이크스트라(dijkstra) 문제
'''
그래프, 데이크스트라(dijkstra) 문제

(0, 0) 위치부터 시작해서 (n - 1, n - 1)의 위치까지 이동하는데 비용이 얼마나 생기는지 구하는 문제이다.
푸는 방식은 bfs 풀 듯이 풀면 된다.
거리를 계산하는 distance 리스트를 n의 크기와 INF 값을 초기화 한 다음에, 비용(cost)이 더 싼 값이면 해당 값을 바꿔주는 방식으로 풀면 된다.
코드를 읽는게 어렵지 않아서 천천히 따라가면서 읽으면 이해할 수 있다.
'''

import heapq as hq

INF = int(1e9)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cnt = 0

def dijkstra(graph, distance):
    q = []
    distance[0][0] = 0
    hq.heappush(q, [graph[0][0], 0, 0])

    while q:
        dist, x, y = hq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {distance[x][y]}')
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    hq.heappush(q, [cost, nx, ny])

while 1:
    cnt += 1
    n = int(input())
    if n == 0: break

    graph = [ list(map(int, input().split())) for _ in range(n) ]
    distance = [ [INF] * n for _ in range(n) ]
    dijkstra(graph, distance)
