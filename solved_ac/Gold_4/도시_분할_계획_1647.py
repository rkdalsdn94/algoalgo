# 백준 - 골드4 - 도시 분할 계획 - 1647 - 그래프, 크루스칼 알고리즘, 최소 신장 트리 문제
'''
그래프, 크루스칼 알고리즘, 최소 신장 트리 문제

풀이 과정
 1. find 함수를 정의한다. 만약 부모가 자기 자신이 아니라면 부모를 찾는다.
 2. union 함수를 정의한다. x, y를 find 함수를 통해 찾고, x가 y보다 작으면 y의 부모를 x로 설정하고, 그렇지 않으면 x의 부모를 y로 설정한다.
 3. edges를 가중치를 기준으로 정렬한다.
 4. parent를 초기화하고, res와 max_cost를 0으로 초기화한다.
 5. edges를 돌면서 find(a)와 find(b)가 다른 경우 union을 수행하고, res에 가중치를 더하고, max_cost를 갱신한다.
 6. res에서 max_cost를 뺀 값을 출력한다.
'''

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# n, m = 7, 12
# edges = [
#     [1, 2, 3], [1, 3, 2], [3, 2, 1], [2, 5, 2],
#     [3, 4, 4], [7, 3, 6], [5, 1, 5], [1, 6, 2],
#     [6, 4, 1], [6, 5, 3], [4, 5, 3], [6, 7, 4]
# ] # 8

edges.sort(key=lambda x: x[2])
parent = [i for i in range(n + 1)]
res = 0
max_cost = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(x, y):
    x, y = find(x), find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        res += c
        max_cost = max(max_cost, c)

print(res - max_cost)
