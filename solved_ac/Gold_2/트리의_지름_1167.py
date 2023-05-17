# 백준 - 골드2 - 트리의 지름 - 1167 - 그래프, 트리, dfs 문제
'''
그래프, 트리, dfs 문제

'골드4 - 트리의 지름(1967)' 문제랑 똑같이 풀면 되는데, input에 대해서만 생각하면 된다.
input 값은 문제를 잘 보다보면 방식이 생긴다. -1이 아니면 1, 3, 5 ... 처럼 2단계 씩 이동하면서 -1이 아니면 graph에 추가하면 된다.

나머지 풀이는 상술한 골드4 - 트리의 지금(1967) 파일에 적어놨다.
'''

import sys; sys.setrecursionlimit(10**9)

v = int(input())
graph = [ [] for _ in range(v + 1) ]
distance = [-1] * (v + 1)

for _ in range(v): # input 값 들을 내가 사용하기 편리하게 수정
    v_list = list(map(int, input().split()))
    v_node = v_list[0]

    for i in range(1, len(v_list), 2):
        if v_list[i] == -1:
            break
        graph[v_node].append([v_list[i], v_list[i + 1]])
# print(graph)

# 테스트
# v = 5
# graph = [[], [[3, 2]], [[4, 4]], [[1, 2], [4, 3]], [[2, 4], [3, 3], [5, 6]], [[4, 6]]]
# distance = [-1, -1, -1, -1, -1, -1] # 11

def dfs(x, weight):
    for i in graph[x]:
        a, b = i

        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, distance[a])

distance[1] = 0
dfs(1, 0)

start_node = distance.index(max(distance))
distance = [-1] * (v + 1)
distance[start_node] = 0
dfs(start_node, 0)

print(max(distance))
