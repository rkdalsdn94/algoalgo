# 백준 - 골드4 - 트리의 지름 - 1967 - 그래프, 트리, dfs 문제
'''
그래프, 트리, dfs 문제

setrecursionlimit이 없으면 '런타임 에러 (RecursionError)'가 발생한다.
distance에서 처음 위치를 방문했다는 표시를 잘 해야된다. (2 번째 dfs에서 까먹었고 안했다가 '틀렸습니다'가 나옴.)

문제 풀이의 핵심 아이디어는 '임의의 노드에서 가장 긴 경로로 연결된 노드는 트리의 지음에 해당하는 두 노드 중 하나'이다. -> 여기 코드에선 부모 노드부터 시작
이와 관련된 영상으로 C++로 푼 https://www.youtube.com/watch?v=gIROKVJV6w8 유튜브 영상이 있다. 풀이만 참고했다.(저 영상에선 bfs로 품.)

두 번의 dfs로 문제를 풀었다.
처음 dfs에선 start 노드를 찾기 위해 -> distance의 max 값이 start_node
두 번째 dfs에선 start_node에서 가장 거리가 긴 노드를 찾기 위한 dfs -> distance의 max 값이 트리의 지름
'''

import sys; sys.setrecursionlimit(10**9)

n = int(input())
g = [ [] for _ in range(n + 1) ]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])
# print(g)

# 테스트
# n = 12
# g = [[],
#     [[2, 3], [3, 2]], [[1, 3], [4, 5]], [[1, 2], [5, 11], [6, 9]],
#     [[2, 5], [7, 1], [8, 7]], [[3, 11], [9, 15], [10, 4]],
#     [[3, 9], [11, 6], [12, 10]],[[4, 1]], [[4, 7]],
#     [[5, 15]], [[5, 4]], [[6, 6]], [[6, 10]]
# ] # 45
# n = 1
# g = [[], []] # 0

distance = [-1] * (n + 1)

def dfs(start, weight):

    for i in g[start]:
        a, b = i

        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, distance[a])

distance[1] = 0 # dfs 를 시작하기 전에 시작하는 노드를 0으로 초기화
dfs(1, 0) # 부모(어떤 노드라도 괜찮) 노드에서 가중치(거리)가 제일 긴 노드를 찾으면 그 곳이 start 노드

start_node = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start_node] = 0 # 86% / 90% / 100% 에서 틀렸습니다 발생할 때.. -> 까먹고 안해놨다가 틀렸다. 질문 게시판 참고
dfs(start_node, 0)

print(max(distance))
