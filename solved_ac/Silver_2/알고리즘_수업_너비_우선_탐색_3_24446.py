# 백준 - 실버2 - 알고리즘 수업 너비 우선 탐색 3 - 24446 - 그래프, bfs 문제
'''
그래프, bfs 문제

기본적인 bfs 문제이다. 문제에 나와 있는 슈도코드를 그대로 구현하면 된다.
단, 제출할 때 input 을 stdin.readline 으로 받거나, PyPy3로 제출해야 된다.

풀이 과정
 1. 입력을 받고, 그래프를 만든다.
 2. bfs로 탐색하고, 결과를 출력한다.
'''

from collections import deque

n, m, r = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# 테스트
# n, m, r = 5, 5, 1
# g = [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []] # 0  \  1  \  2  \  1  \  -1

ck = [-1] * (n + 1)

def bfs(start):
    q = deque([start])
    ck[start] = 0

    while q:
        x = q.popleft()

        for i in g[x]:
            if ck[i] == -1:
                q.append(i)
                ck[i] = ck[x] + 1

bfs(r)

for i in ck[1:]:
    print(i)
