# 백준 - 실버2 - 그대, 그머가 되어 - 14496 - 그래프, bfs 문제
'''
그래프, bfs 문제

문제를 이해하고 코드를 짜는 시간보다 문제를 이해하는 데 시간이 더 걸린 문제였다.
근데, (n, m)으로 들어오는 값들은 서로 치환할 수 있다는 사실을 알고 그래프 문제라는걸 깨달았다.
즉, 그래프(g)에는 x, y를 서로 연결시켜 놓고, 방문 여부를 체크를 위한 ck변수를 0으로 초기화해둔다. (그래프의 길이 만큼, 입력 그대로 숫자를 사용하기 위해 n + 1)
출발값(a)의 가중치를 0으로 q에 미리 넣어두고 bfs를 실행한다.
bfs는 다른 그래프 문제 풀듯이 풀면 된다.
단, 치환하는 경우가 여러 방법이 있을 수 있으므로 그 중 제일 작은 값을 구해야 하므로(최소 치환 횟수) res와 가중치(dist) 두 값 중 min 함수를 실행해야 한다.

in
    1 2
    4 4
    1 3
    1 4
    3 2
    4 2
out
    2
in
    2 3
    3 3
    1 2
    1 3
    3 2
out
    1
'''

from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

res = int(1e9)
ck = [0] * (n + 1)
ck[a] = 1
q = deque([(a, 0)])

while q:
    curr, dist = q.popleft()

    if curr == b:
        res = min(res, dist)

    for i in g[curr]:
        if ck[i] == 0:
            ck[i] = 1
            q.append((i, dist + 1))

print(res if res != int(1e9) else -1)
