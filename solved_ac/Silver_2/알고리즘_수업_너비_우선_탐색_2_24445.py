# 백준 - 실버2 - 알고리즘 수업 너비 우선 탐색 2 - 24445 - 그래프, bfs 문제
'''
그래프, bfs 문제

문제에 주어진 요구사항을 구현하면 된다.

기본적인 bfs 문제라서 따로 설명을 안 적는다. 이해가
pseudo-code 도 나와 있어서 그대로 구현하면 된다. (내림차순으로 정렬하는걸 잘 기억해야 된다.)
'''

from collections import deque

n, m, r = map(int,input().split())
g = [[] for _ in range(n + 1)]
ck = [0] * (n + 1)
ck[r] = 1
cnt = 1
q = deque([r])

for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1,n+1):
    g[i].sort(reverse = True)

while q:
    v = q.popleft()

    for i in g[v]:
        if not ck[i]:
            cnt += 1
            ck[i] = cnt
            q.append(i)

print(*ck[1:], sep='\n')
