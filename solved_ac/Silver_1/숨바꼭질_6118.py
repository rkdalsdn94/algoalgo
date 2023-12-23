# 백준 - 실버1 - 숨바꼭질 - 6118 - 그래프, bfs 문제
'''
그래프, bfs 문제

기본적인 bfs로 풀면 되는 문제다.

처음에 문제 이해를 제대로 하지 못해 인덱스 에러를 맞았다. (96% 에서 에러가 나오면 바로 아랫줄을 확인해보자)
 - 그래프의 범위(g)와 방문 여부 체크(ck)의 범위를 m + 1의 크기로 초기화 했다가 96%에서 인덱스 에러가 나왔다.

범위를 제대로 잡고 입력으로 주어진 그래프에 대해 1번 노드부터 bfs를 돌린 뒤, ck의 최댓값으로 다음과 같이 출력하면 된다.
    - q에 꺼낸 값으로 g의 노드들의 방문 여부를 체크하고 이 전에 방문하지 않은 노드이면 ck의 해당 번째 인덱스는 이 전 값에서 1을 더 더해야 한다.
출력할 때 순서는 다음과 같다.
    - 헛간 번호 : 최댓값(res)이 처음 나오는 index와 (n + 1의 범위이므로 + 1을 안해도 된다.)
    - 헛간 까지의 거리 : ck의 첫 번째 방문을 1부터 시작했으므로 거리에 1을 빼야 된다. (res - 1)
    - 최댓값이 같은 헛간 : count 함수를 통해 구하면 된다. (같은 거리는 ck의 동일한 값을 갖는다.)

in
    6 7
    3 6
    4 3
    3 2
    1 3
    1 2
    2 4
    5 2
out
    4 2 3
'''

from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
ck = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(n):
    ck[n] = 1
    q = deque([n])

    while q:
        a = q.popleft()

        for i in g[a]:
            if not ck[i]:
                ck[i] = ck[a] + 1
                q.append(i)

bfs(1)
res = max(ck)
print(ck.index(res), res - 1, ck.count(res))
