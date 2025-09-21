# 프로그래머스 - Lv2 - 혼자 놀기의 달인 - 그래프, dfs 문제
"""
그래프, dfs 문제

[핵심 아이디어]
    - 각 상자를 노드로, 카드 번호를 다음 노드의 인덱스로 보는 그래프 문제
    - DFS를 통해 사이클(그룹)들을 찾고, 가장 큰 두 그룹의 크기를 곱함

[풀이 과정]
    1. 방문하지 않은 노드부터 DFS 시작
    2. 사이클이 형성될 때까지 탐색하여 그룹 크기 계산
    3. 모든 그룹 크기를 저장 후 내림차순 정렬
    4. 상위 2개 그룹 크기를 곱하여 최대 점수 계산
"""

def solution(cards):
    visited = [False] * len(cards)
    group_sizes = []

    # 모든 노드에 대해 사이클 탐지
    for i in range(len(cards)):
        if not visited[i]:
            group_size = dfs(cards, visited, i)
            group_sizes.append(group_size)

    # 그룹이 1개뿐이면 게임 종료 (점수 0)
    if len(group_sizes) < 2:
        return 0

    # 내림차순 정렬하여 가장 큰 두 그룹 선택
    group_sizes.sort(reverse=True)

    return group_sizes[0] * group_sizes[1]

def dfs(cards, visited, start):
    """DFS를 통해 하나의 사이클(그룹) 크기 계산"""
    current = start
    size = 0

    # 이미 방문한 노드를 만날 때까지 탐색
    while not visited[current]:
        visited[current] = True
        current = cards[current] - 1  # 1-based → 0-based 인덱스 변환
        size += 1

    return size

print(solution([8,6,3,7,2,5,1,4]) == 12)
