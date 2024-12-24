# 백준 - 실버1 - n단 논법 - 15723 - 그래프, bfs, dfs, 플로이드 와샬, 최단 경로 문제
'''
그래프, bfs, dfs, 플로이드 와샬, 최단 경로 문제

풀이 과정
1. 논법의 표현
   - n단 논법은 n x n 행렬로 표현 가능
   - i -> j로 가는 경로가 있으면 i -> j로 표시
    - i -> j로 가는 경로가 없으면 i -> j로 표시
2. 플로이드 와샬 알고리즘
    - 모든 정점에서 모든 정점으로의 최단 경로를 구하는 알고리즘
    - 3중 for문을 통해 모든 정점을 거쳐가는 경우를 고려
3. 결과 출력
    - i -> j로 가는 경로가 있으면 T, 없으면 F 출력

in
    3
    a is b
    b is c
    a is c
    3
    a is b
    b is c
    c is a
out
    T
    T
    F
'''

n = int(input())
graph = [[0] * 26 for _ in range(26)]

for _ in range(n):
    a, _, b = input().split()
    a, b = ord(a) - 97, ord(b) - 97
    graph[a][b] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

m = int(input())
for _ in range(m):
    a, _, b = input().split()
    a, b = ord(a) - 97, ord(b) - 97
    print('T' if graph[a][b] else 'F')
