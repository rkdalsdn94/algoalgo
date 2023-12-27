# 백준 - 실버2 - 알고리즘 수업 깊이 우선 탐색 2 - 24480 - 그래프, 정렬, dfs 문제
'''
그래프, 정렬, dfs 문제

문제에 있는 다음의 내용을 구현하면 된다.
dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}

위 내용에서 dfs를 실행할 때 시작 정점만 필요해서 V와 E는 생략했다.
'''

import sys; sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, r = map(int, input().split())
g = [[] for _ in range(n + 1)]
ck = [0] * (n + 1)
res = [0] * (n + 1)
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(v):
    global cnt
    ck[v] = 1
    res[v] = cnt
    cnt += 1

    for i in sorted(g[v], reverse=True):
        if not ck[i]:
            dfs(i)
dfs(r)

for i in res[1:]:
    print(i)
