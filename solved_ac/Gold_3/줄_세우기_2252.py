# 백준 - 골드3 - 줄 세우기 - 2252 - 그래프, 위상 정렬 문제
'''
그래프, 위상 정렬 문제

위상 정렬을 구현하면 되는 문제다. 위상 정렬에 잘 모른다면 https://www.youtube.com/watch?v=xeSz3pROPS8 이 영상을 보면 된다.

풀이 과정
- 모든 노드의 대한 진입 차수를 0으로 초기화 한 후 A, B로 이동할 때 진입 차수(indegree)를 1씩 증가한다.

- 위상 정렬 함수 내에서 진입 차수가 0인 노드들을 q에 담고, 아래 과정을 q가 빌 때까지 반복한다.
- 값을 하나씩 꺼내면서 res에 담는다.
- 꺼낸 노드의 진입 차수를 1씩 감소 시킨다.
- 해당 노드의 진입 차수가 0이 되면 그 값을 큐에 담는다.
'''

from collections import deque
import sys; input=sys.stdin.readline

n, m = map(int, input().split())
g = [ [] for _ in range(n + 1) ]

indegree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    indegree[b] += 1

# 테스트
# n, m = 3, 2
# g = [[], [3], [3], []]
# indegree = [0, 0, 0, 2] # 1 2 3
# n, m = 4, 2
# g = [[], [], [], [1], [2]]
# indegree = [0, 1, 1, 0, 0] # 3 4 1 2 --> 이 출력도 정답 가능 (답이 여러 개인 상황)

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

def topology_sort():
    res = []

    while q:
        x = q.popleft()
        res.append(x)

        for i in g[x]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    return res

print(*topology_sort())