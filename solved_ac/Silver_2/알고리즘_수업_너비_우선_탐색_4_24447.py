# 백준 - 실버2 - 알고리즘 수업 너비 우선 탐색 4 - 24447 - 그래프, 정렬, bfs 문제
'''
그래프, 정렬, bfs 문제

PyPy3로 제출하거나 input을 sys.stdin.readline으로 바꿔야 통과할 수 있다. (아니면 시간 초과)

문제 분류에는 정렬이 포함되어 있지만, 정렬을 하지 않고 제출해도 통과된다. (심지어 더 빠름)
그 후 bfs 방식을 사용하여 문제를 풀면 되는데, depth를 구할 수 있는 d 배열과 정점의 방문 순서를 저장할 수 있는 t 배열을 만들어서 풀면 된다.

풀이 과정
    1. n, m, r을 입력받는다.
    2. g를 만들어 n + 1만큼의 빈 리스트를 추가한다.
    3. m만큼 반복하면서 a, b를 입력받고 g[a]에 b를 추가하고, g[b]에 a를 추가한다.
    4. t, d를 만들어 n + 1만큼 0으로 초기화한다.
    5. res, cnt를 0으로 초기화한다.
    6. bfs를 만들어 start를 받는다.
        6.1. cnt를 1로 초기화한다.
        6.2. t[start]를 cnt로 초기화한다.
        6.3. d[start]를 0으로 초기화한다.
        6.4. q를 만들어 start를 넣는다.
        6.5. q가 빌 때까지 다음을 반복한다.
            6.5.1. a를 q.popleft()로 받는다.
            6.5.2. g[a]를 돌면서 다음을 반복한다.
        6.6. i가 정렬된 g[a]를 돌면서 다음을 반복한다.
        6.7. i가 0이면 t[i]를 cnt + 1로 초기화하고 cnt를 1 증가시키고 d[i]를 d[a] + 1로 초기화한다.
        6.8. q에 i를 넣는다.
    7. bfs(r)를 실행한다.
    8. n만큼 반복하면서 res에 t[i] * d[i]를 더한다.
    9. res를 출력한다.
'''

import sys; input=sys.stdin.readline
from collections import deque

n, m, r = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

t = [0] * (n + 1)
d = [-1] * (n + 1)
res, cnt = 0, 1

def bfs(start):
    global cnt

    t[start] = cnt
    d[start] = 0
    q = deque([start])

    while q:
        a = q.popleft()

        for i in sorted(g[a]):
            if t[i] == 0:
                t[i] = cnt + 1
                cnt += 1
                d[i] = d[a] + 1
                q.append(i)

bfs(r)
for i in range(1, n + 1):
    res += t[i] * d[i]

print(res)
