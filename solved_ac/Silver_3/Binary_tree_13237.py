# 백준 - 실버3 - Binary tree - 13237 - 그래프, 트리, dfs, bfs 문제
'''
[핵심 아이디어]
    1. 주어진 부모 노드 정보를 바탕으로 트리를 구성합니다.
    2. 루트 노드를 찾고, 해당 노드부터 BFS(너비 우선 탐색)를 통해 각 노드의 높이를 계산합니다.
    3. 각 노드의 높이를 순서대로 출력합니다.

[풀이 과정]
    1. 각 노드의 부모 정보를 입력받습니다.
    2. 부모가 -1인 노드를 루트 노드로 지정합니다.
    3. 부모 정보를 이용해 각 노드의 자식 노드 리스트를 생성합니다.
    4. BFS를 사용하여 루트 노드부터 시작해 각 레벨의 노드들을 순회하며 높이를 기록합니다.
    5. 노드 번호 순서대로 높이를 출력합니다.
'''

from collections import defaultdict, deque

def compute_heights(n, parents):
    # 자식 노드 리스트 생성
    children = defaultdict(list)
    root = -1

    for node, parent in enumerate(parents, 1):
        if parent == -1:
            root = node  # 루트 노드 찾기
        else:
            children[parent].append(node)  # 부모 노드에 자식 노드 추가

    # 각 노드의 높이를 저장할 딕셔너리
    heights = {}

    # BFS로 각 노드의 높이 계산
    queue = deque([(root, 0)])  # (노드, 높이) 형태로 저장

    while queue:
        node, height = queue.popleft()
        heights[node] = height

        # 현재 노드의 자식 노드들을 큐에 추가
        for child in children[node]:
            queue.append((child, height + 1))

    return [heights[i] for i in range(1, n+1)]

n = int(input())
parents = [int(input()) for _ in range(n)]

# 테스트
# n = 7
# parents = [-1, 1, 1, 2, 2, 3, 3] # 0 \ 1 \ 1 \ 2 \ 2 \ 2 \ 2
# n = 5
# parents = [-1, 1, 1, 3, 4] # 0 \ 1 \ 1 \ 2 \ 3
# n = 3
# parents = [2, -1, 2] # 1 \ 0 \ 1

res = compute_heights(n, parents)
for height in res:
    print(height)
