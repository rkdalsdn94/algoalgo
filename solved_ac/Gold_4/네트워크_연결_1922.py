# 백준 - 골드4 - 네트워크 연결 - 1922 - 그래프, 최소 신장 트리, 크루스칼 알고리즘 문제
'''
그래프, 최소 신장 트리, 크루스칼 알고리즘 문제

최소 신장 트리, 크루스칼 알고리즘을 알면 쉽게 풀 수 있는 문제이다.

풀이 과정
 1. 입력을 받고, 간선을 edges에 저장한다.
 2. edges를 가중치를 기준으로 정렬한다.
 3. parent를 초기화하고, res를 0으로 초기화한다.
 4. find와 union 함수를 정의한다.
 5. edges를 돌면서 find(a)와 find(b)가 다른 경우 union을 수행하고, res에 가중치를 더한다.
 6. res를 출력한다.
'''

n, m = int(input()), int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])

# 테스트
# n, m = 6, 9
# edges = [[1, 2, 5], [1, 3, 4], [2, 3, 2], [2, 4, 7], [3, 4, 6], [3, 5, 11], [4, 5, 3], [4, 6, 8], [5, 6, 8]] # 23

parent = [i for i in range(n + 1)]
res = 0

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

print(res)
