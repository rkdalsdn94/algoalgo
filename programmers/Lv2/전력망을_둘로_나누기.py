# 프로그래머스 - Lv2 - 전력망을 둘로 나누기 - 그래프, bfs, 완전 탐색 문제
"""
그래프, bfs, 완전 탐색 문제

[핵심 아이디어]
    1. 트리에서 하나의 간선을 끊으면 두 개의 서브트리로 분리됨
    2. 각 간선을 하나씩 제거해보면서 두 서브트리의 노드 개수 차이를 계산
    3. BFS를 사용하여 서브트리의 노드 개수를 세고, 차이의 최솟값 찾기

[풀이 과정]
    1. 인접 리스트 형태로 그래프 구성
    2. 모든 간선에 대해 하나씩 제거해보기:
       - 간선 (a, b)를 제거
       - BFS로 a에서 시작하여 연결된 노드 개수 count_a 계산
       - 전체 노드 개수 n에서 count_a를 빼서 count_b 계산
       - |count_a - count_b| 계산하여 최솟값 갱신
    3. 최종적으로 구한 최솟값 반환
"""

from collections import deque

def solution(n, wires):
    answer = n  # 최대 차이로 초기화

    # 모든 간선에 대해 하나씩 끊어보기
    for i in range(len(wires)):
        # i번째 간선을 제외한 그래프 구성
        graph = [[] for _ in range(n+1)]
        for j in range(len(wires)):
            if i == j:  # 제외할 간선
                continue
            v1, v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)

        # BFS로 한쪽 서브트리의 노드 개수 세기
        visited = [False] * (n+1)
        q = deque([1])  # 1번 노드부터 시작
        visited[1] = True
        count = 1  # 연결된 노드 수

        while q:
            node = q.popleft()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
                    count += 1

        # 두 서브트리의 노드 개수 차이 계산
        diff = abs(count - (n - count))
        answer = min(answer, diff)

    return answer
