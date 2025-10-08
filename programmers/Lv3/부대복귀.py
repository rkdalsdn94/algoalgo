# 프로그래머스 - Lv3 - 부대복귀 - 그래프, bfs, 최단 거리 문제
"""
[문제 분류]
그래프 탐색, bfs, 최단 거리 문제

[핵심 아이디어]
    여러 출발지(sources)에서 하나의 목적지(destination)까지의 최단 거리를 구하는 문제
    각 출발지마다 BFS를 수행하면 O(sources 개수 × (V+E))로 비효율적 대신, 양방향 그래프의 특성을 이용해 "역방향 탐색" 수행
        - destination에서 출발하여 모든 노드까지의 거리를 한 번의 bfs로 계산
        - 양방향 그래프이므로 A → B 거리 = B → A 거리
        - 따라서 destination → source 거리 = source → destination 거리는 같음

[풀이 과정]
    1. 양방향 그래프를 인접 리스트로 구성
    2. answer 배열을 -1로 초기화 (미방문 및 도달 불가 표시)
    3. destination을 시작점으로 BFS 수행
       - 방문한 노드의 거리를 answer 배열에 기록
       - answer[i] == -1인 경우에만 방문 (중복 방문 방지)
    4. sources의 각 원소에 대해 answer 배열에서 거리 조회
    5. 도달 불가능한 노드는 -1을 유지
"""

from collections import deque

def solution(n, roads, sources, destination):
    # answer: 각 노드까지의 최단 거리 저장 (-1: 미방문/도달불가)
    answer = [-1] * (n + 1)

    # g: 양방향 그래프를 인접 리스트로 표현
    g = [[] for _ in range(n + 1)]

    # 양방향 간선 추가
    for i, j in roads:
        g[i].append(j)
        g[j].append(i)

    # bfs 시작: destination에서 출발
    q = deque([destination])
    answer[destination] = 0  # 시작점은 거리 0
    while q:
        x = q.popleft()  # 현재 노드
        curr = answer[x]  # 현재 노드까지의 거리

        # 현재 노드와 연결된 모든 인접 노드 탐색
        for i in g[x]:
            # 아직 방문하지 않은 노드만 처리
            if answer[i] == -1:
                answer[i] = curr + 1  # 거리 갱신
                q.append(i)  # 다음 탐색을 위해 큐에 추가

    # sources의 각 위치에서 destination까지의 거리만 추출
    answer = [answer[i] for i in sources]

    return answer

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1) == [1, 2])  # True
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5) == [2, -1, 0])  # True
