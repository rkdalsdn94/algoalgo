# 백준 - 골드4 - 최소 스패닝 트리 - 1197 - 그래프, 최소 스패닝 트리, 크루스칼 문제
'''
그래프, 최소 스패닝 트리, 크루스칼 문제

2024.09.06 재채점 결과 런타임 에러(RecursionError)가 발생
  - 재귀 깊이(sys.setrecursionlimit) 설정해서 해결

최소 신장 트리 문제이다. 최소 신장 트리에 관한 사전 지식이 있으면 쉽게 풀 수 있다.
최소 신장 트리를 구하는 알고리즘으로 대표적인 2가지가 있는데, 그 중 하나인 크루스칼 알고리즘을 이용해서 풀었다.
ㄴ> (다른 알고리즘은 '프림 알고리즘'이다. 당연히 프림 알고리즘으로 해도 문제를 풀 수 있다.)
ㄴ> 크루스칼 알고리즘에 대해선 https://chanhuiseok.github.io/posts/algo-33/ 참고

최소 신장 트리의 특징으로 모든 노드가 연결되어 있으면서, 사이클이 존재하지 않아야된다.
사이클을 방지하기 위해 Union-Find 알고리즘도 같이 사용했다.
ㄴ> Union-Find 알고리즘 https://gmlwjd9405.github.io/2018/08/31/algorithm-union-find.html 참고

Union-Find 알고리즘을 좀 더 효율적으로 사용하기 위해
'union-by-rank' 기법, 'path compression' 기법을 사용했다.
ㄴ> 두 기법에 대해선 https://www.secmem.org/blog/2021/03/21/Disjoint-Set-Union-find/ 참고
'''

import sys; input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v, e = map(int, input().split())
vertices = [ i for i in range(v + 1) ]
graph = [ list(map(int, input().split())) for _ in range(e) ]
parent = dict()
rank = dict()

def find(node):
    if parent[node] != node: # 'path compression' 기법
        parent[node] = find(parent[node])
    
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]: # 'union-by-rank' 기법
        parent[root2] = root1
    else:
        parent[root1] = root2

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph, vertices):
    res = 0

    for node in vertices[1:]: # 그래프 초기화 이 문제에선 없어도 된다.
        make_set(node)
    
    edges = sorted(graph, key=lambda x: x[2]) # 간선 초기화

    for edge in edges: # 사이클 방지를 위한 union-find 알고리즘
        node_v, node_u, weight = edge

        if find(node_v) != find(node_u):
            union(node_v, node_u)
            res += weight
    
    return res

print(kruskal(graph, vertices))
