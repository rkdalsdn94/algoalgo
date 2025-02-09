# 백준 - 실버2 - Choose your own path - 16021 - 그래프, bfs 문제
'''
그래프, bfs 문제

[핵심 아이디어]
    - 모든 페이지의 접근 가능성 확인 - 불필요한 페이지 인쇄 비용 방지
    - 가장 짧은 스토리 경로 찾기 - 최소 독서 시간 파악

[풀이 과정]
    1. 그래프 구성
        - 각 페이지의 선택지 정보를 바탕으로 방향성 그래프 구축
        - 인접 리스트 방식으로 구현하여 메모리 효율성 확보
    2. 모든 페이지 도달 가능성 확인
        - BFS를 활용하여 시작 페이지(1페이지)에서 접근 가능한 모든 페이지 탐색
        - visited 집합을 사용하여 방문한 페이지 수와 전체 페이지 수 비교
    3. 최단 경로 탐색
        - BFS를 사용하여 시작 페이지부터 첫 번째 끝 페이지까지의 최단 거리 계산
        - 각 탐색 단계에서 경로 길이 정보를 함께 저장하여 추적

in
    3
    2 2 3
    0
    0
out
    Y
    2

in
    3
    2 2 3
    0
    1 1
out
    Y
    2
'''

from collections import deque

def solve_adventure_book(N, graph):
    # 모든 페이지 도달 가능한지 확인
    def check_reachable():
        visited = set()
        queue = deque([1])  # 1페이지부터 시작
        visited.add(1)

        while queue:
            current = queue.popleft()
            for next_page in graph[current]:
                if next_page not in visited:
                    visited.add(next_page)
                    queue.append(next_page)

        return len(visited) == N

    # 가장 짧은 경로 찾기
    def find_shortest_path():
        queue = deque([(1, 1)])  # (페이지, 경로 길이)
        visited = {1}

        while queue:
            current, length = queue.popleft()

            # 현재 페이지가 끝 페이지인 경우
            if len(graph[current]) == 0:
                return length

            for next_page in graph[current]:
                if next_page not in visited:
                    visited.add(next_page)
                    queue.append((next_page, length + 1))

    can_reach_all = check_reachable()
    shortest_path = find_shortest_path()

    return "Y" if can_reach_all else "N", shortest_path

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    nums = list(map(int, input().split()))
    graph[i] = nums[1:] if nums[0] > 0 else []

result_reach, result_path = solve_adventure_book(N, graph)
print(result_reach)
print(result_path)
