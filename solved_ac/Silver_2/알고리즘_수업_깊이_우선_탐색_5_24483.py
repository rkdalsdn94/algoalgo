# 백준 - 실버2 - 알고리즘 수업 깊이 우선 탐색 5 - 24483 - 그래프, 정렬, dfs 문제
'''
그래프, 정렬, dfs 문제

recursionlimit를 설정하지 않으면 RecursionError가 발생하고, PyPy3로 제출하면 메모리 초과가 나온다.
Python3와 input과 recursionlimit 모두 설정해야 함

[문제 해석]
- N개의 정점과 M개의 간선으로 구성된 무방향 그래프에서 DFS를 수행
- 각 노드의 두 가지 특성을 추적해야 함:
  1. 깊이(depth): 시작 노드로부터의 거리
  2. 방문 순서(visit order): DFS가 노드를 방문한 순서
- 모든 노드에 대해 (깊이 × 방문순서)의 합을 계산

[문제 접근]
- DFS를 구현하되 다음 조건들을 고려해야 함:
  1. 시작 노드의 깊이는 0, 방문 불가 노드는 -1
  2. 시작 노드의 방문 순서는 1, 방문 불가 노드는 0
  3. 인접 노드는 반드시 오름차순으로 방문
- 깊이와 방문 순서를 동시에 추적하는 DFS 함수 구현 필요

[해결 방법]
1. 그래프를 인접 리스트로 구현
2. 방문 순서와 깊이를 저장할 배열 초기화
3. DFS 함수에서:
   3.1. 현재 노드의 방문 순서와 깊이 기록
   3.2. 인접 노드를 오름차순 정렬
   3.3. 미방문 인접 노드에 대해 재귀적으로 DFS 수행
4. 모든 노드의 (깊이 × 방문순서) 계산 및 합산
'''

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(r, d):
    global cnt  # 방문 순서를 전역 변수로 관리

    ck[r] = cnt  # 현재 노드의 방문 순서 기록
    depth[r] = d  # 현재 노드의 깊이 기록
    graph[r].sort()  # 인접 노드를 오름차순으로 정렬 (문제 조건)

    # 인접한 모든 노드에 대해 DFS 수행
    for i in graph[r]:
        if ck[i] == 0:  # 미방문 노드인 경우
            cnt += 1    # 방문 순서 증가
            dfs(i, d + 1)  # 깊이를 1 증가시켜 재귀 호출

# 입력 처리 및 초기화
n, m, r = map(int, input().split())  # n:노드 수, m:간선 수, r:시작 노드
ck = [0] * (n + 1)      # 방문 순서 배열 초기화
depth = [-1] * (n + 1)  # 깊이 배열을 -1로 초기화 (방문 불가능한 노드 표시)
graph = [[] for _ in range(n + 1)]  # 인접 리스트로 그래프 구현
cnt = 1  # 방문 순서 카운터 (1부터 시작)

# 무방향 그래프 구성
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)  # 양방향이므로 양쪽에
    graph[v].append(u)  # 모두 간선 추가

dfs(r, 0)  # DFS 시작 (시작 노드의 깊이는 0)

# 결과 계산: 각 노드의 (깊이 × 방문순서)의 합
res = 0
for i in range(1, n+1):
    res += ck[i] * depth[i]

print(res)
