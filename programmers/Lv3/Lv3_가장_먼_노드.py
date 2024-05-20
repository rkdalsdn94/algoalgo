# 프로그래머스 - Lv3 - 가장 먼 노드 - 그래프 - bfs 문제
'''
그래프, bfs 문제

풀이 과정
 1. 노드의 개수 n과 간선의 정보 edge가 주어진다.
 2. edge를 이용해서 그래프를 만든다. 양방향으로 만들기 위해 g[i].append(j)와 g[j].append(i)를 해준다.
 3. bfs를 이용해서 1번 노드에서 가장 먼 노드까지의 거리를 구한다.
 4. 가장 먼 노드의 개수를 출력한다.
'''

from collections import deque

def solution(n, edge):
    answer = 0
    g = [[] for _ in range(n + 1)]
    ck = [0] * (n + 1)

    for i, j in edge:
        g[i].append(j)
        g[j].append(i)

    q = deque([1])
    ck[1] = 1
    while q:
        x = q.popleft()

        for i in g[x]:
            if ck[i] == 0:
                ck[i] = ck[x] + 1
                q.append(i)

    answer = ck.count(max(ck))
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3
