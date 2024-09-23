# 백준 - 실버2 - 영일랜드 - 31871 - 그래프, 완전 탐색, 백 트래킹(dfs) 문제
'''
그래프, 완전 탐색, 백 트래킹(dfs) 문제

풀이 과정
    1. 입력을 받는다.
    2. adj_list를 만들어 각 노드의 간선 정보를 저장한다.
    3. dfs를 만들어서 0부터 시작하여 모든 노드를 방문하면서 최대 거리를 구한다.
    4. ans를 출력한다.

in
    2
    8
    0 1 18
    0 2 20
    0 2 15
    1 0 10
    1 2 15
    2 0 13
    2 2 10
    2 1 5
out
    46
in
    2
    4
    0 1 18
    0 2 20
    1 0 10
    1 2 15
out
    -1
'''

from collections import defaultdict

def dfs(node, dist, count, adj_list, is_visited, N):
    global res

    if node == 0 and count == N + 1:
        res = max(res, dist)
        return

    for next_node, next_dist in adj_list[node]:
        if is_visited[next_node]:
            continue

        is_visited[next_node] = True
        dfs(next_node, dist + next_dist, count + 1, adj_list, is_visited, N)
        is_visited[next_node] = False

n, m = int(input()), int(input())
res = -1

adj_list = defaultdict(list)
edge_map = defaultdict(dict)
for _ in range(m):
    u, v, d = map(int, input().split())

    if u == v:
        continue  # 자신에게로 가는 간선은 제거

    # 중복 간선을 처리 (최대 값 선택)
    if v in edge_map[u]:
        edge_map[u][v] = max(edge_map[u][v], d)
    else:
        edge_map[u][v] = d

# 인접 리스트 구성
for u in range(n + 1):
    for v, d in edge_map[u].items():
        adj_list[u].append((v, d))  # 튜플 사용

ck = [False] * (n + 1)
dfs(0, 0, 0, adj_list, ck, n)

print(res)
