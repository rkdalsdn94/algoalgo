# 백준 - 실버2 - 알고리즘 수업 너비 우선 탐색 1 - 24444 - 그래프, 정렬, bfs 문제
'''
그래프, 정렬, bfs 문제

bfs 풀 듯이 문제를 풀어야 되는데 그래프를 정렬한 뒤 풀어야 된다.
문제에 나와있듯이 정렬한 뒤에 제출해야 통과한다. 처음에 정렬을 안하고 '틀렸습니다.' 가 나와서 당황했다.
'''

from collections import deque
import sys; input=sys.stdin.readline # Python3 로 제출하려면 필요 

n, m, r = map(int, input().split())
g = [ [] for _ in range(n + 1) ]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(n + 1):
    g[i].sort()

ck = [0] * (n + 1)
cnt = 1

def bfs(x):
    global cnt
    q = deque([x])
    ck[x] = 1
    cnt += 1

    while q:
        a = q.popleft()

        for i in g[a]:
            if ck[i] == 0:
                ck[i] = cnt
                cnt += 1
                q.append(i)

bfs(r)
for i in ck[1:]:
    print(i)