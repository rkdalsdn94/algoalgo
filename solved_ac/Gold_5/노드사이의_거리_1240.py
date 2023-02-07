# 백준 - 골드5 - 노드사이의 거리 - 1240 - 그래프, 트리, bfs 문제 (dfs로도 풀 수 있다고 한다.)
'''
그래프, 트리, bfs 문제 (dfs로도 풀 수 있다고 한다.)

전에 다익스트라 문제를 입력받을 때 처럼 트리를 입력을 받은 후 bfs를 실행한 결과를 출력하면 된다.
트리 입력형식과 bfs 두 개념을 알고 있으면 많이 어렵지 않게 풀 수 있다.
입력받은 트리에서 m_list로 주어졌을 때 출발 지점(x)과 도착 지점(y)의 거리를 구하면 된다.
'''

from collections import deque

n, m = map(int, input().split())
g = [ [] for _ in range(n + 1) ]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])
m_list = [ list(map(int, input().split())) for _ in range(m) ]

# 테스트
# n, m = 4, 2
# g = [[], [[2, 2], [4, 3]], [[1, 2]], [[4, 2]], [[3, 2], [1, 3]]]
# m_list =  [[1, 2], [3, 2]] # 2  \  7

def bfs(x, y):
    q = deque([(x, 0)]) # 현재 자기의 위치니까 비용이 0이 된다.
    ck = [0] * (n + 1) # 방문한 곳을 표기하기 위한 check 변수
    ck[x] = 1 # 처음 방문한 곳 체크

    while q:
        a, b = q.popleft()

        if a == y: # 현재 위치가 도착해야 될 곳이라면 비용 반환.
            return b

        for i, j in g[a]:
            if not ck[i]: # 방문한 적이 없다면
                ck[i] = 1 # 방문 표시
                q.append([i, b + j]) # q에 비용을 추가한 후 담기

for i, j in m_list:
    print(bfs(i, j))