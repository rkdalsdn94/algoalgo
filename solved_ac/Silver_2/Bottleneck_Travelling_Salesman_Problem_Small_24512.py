# 백준 - 실버2 - Bottleneck Travelling Salesman Problem (Small) - 24512 - 완전 탐색, 백 트래킹, 외판원 순회(Traveling Salesman Problem, TSP) 문제
'''
완전 탐색, 백 트래킹, 외판원 순회(Traveling Salesman Problem, TSP) 문제

풀이 과정
    1. n, m을 입력받는다.
    2. cost를 입력받는다.
    3. find_bottleneck_tsp 함수를 생성한다.
    4. min_bottleneck, best_route를 초기화한다.
    5. 0번 정점을 시작점으로 고정하고 나머지 정점들에 대한 모든 순열 생성한다.
    6. 순열에 따라 비용을 계산한다.
    7. 마지막으로 다시 출발점(0)으로 돌아가는 비용을 계산한다.
    8. best_route가 None이면 -1을 출력한다.
    9. best_route가 None이 아니면 최소 비용과 경로를 출력한다.

in
    3 6
    1 2 4
    2 3 4
    3 1 4
    1 3 2
    3 2 3
    2 1 5
out
    4
    1 2 3

in
    2 1
    1 2 3
out
    -1
'''

from itertools import permutations

n, m = map(int, input().split())
inf = float('inf')
cost = [[inf] * n for _ in range(n)]

for i in range(1, m + 1):
    u, v, c = map(int, input().split())
    cost[u - 1][v - 1] = c  # u에서 v로 가는 비용

def find_bottleneck_tsp():
    min_bottleneck = inf
    best_route = None

    # 0번 정점을 시작점으로 고정하고 나머지 정점들에 대한 모든 순열 생성
    nodes = list(range(1, n))
    for perm in permutations(nodes):
        perm = [0] + list(perm)  # 출발점 0을 경로의 맨 앞에 고정
        bottleneck = 0
        valid = True

        # 순열에 따라 비용을 계산
        for i in range(n - 1):
            u, v = perm[i], perm[i + 1]

            if cost[u][v] == inf:
                valid = False  # 경로가 없는 경우
                break

            bottleneck = max(bottleneck, cost[u][v])  # 각 이동 경로의 최대 비용

        # 마지막으로 다시 출발점(0)으로 돌아가는 비용 계산
        if valid and cost[perm[-1]][0] != inf:
            bottleneck = max(bottleneck, cost[perm[-1]][0])

            if bottleneck < min_bottleneck:
                min_bottleneck = bottleneck
                best_route = perm
        else:
            valid = False

    if best_route is None:
        print(-1)
    else:
        print(min_bottleneck)
        print(" ".join(map(str, [x + 1 for x in best_route])))

find_bottleneck_tsp()
