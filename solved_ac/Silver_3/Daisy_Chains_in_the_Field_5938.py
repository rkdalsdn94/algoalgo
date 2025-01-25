# 백준 - 실버3 - Daisy Chains in the Field - 5938 - 그래프, bfs, dfs 문제
'''
그래프, bfs, dfs 문제

핵심 아이디어
   - 1번 소를 시작점으로 BFS를 통해 연결된 모든 소들을 탐색
   - visited 배열을 통해 1번 소와 연결된 소들을 체크
   - visited가 False인 소들이 1번 소와 연결되지 않은 "misbehaving cows"
   - flag 변수를 통해 모든 소가 연결된 경우(0 출력)와 연결되지 않은 소가 있는 경우를 구분

풀이 과정
   1. 소의 수(N)와 연결된 쌍의 수(M)를 입력받음
   2. 인접 리스트 형태로 그래프 구현
   3. M개의 연결 관계를 입력받아 그래프에 저장
   4. BFS 함수를 통해 1번 소부터 시작하여 연결된 모든 소들을 탐색
   5. visited 배열로 방문한 소들을 체크
   6. flag 변수를 통해 연결되지 않은 소 존재 여부 확인
   7. 연결되지 않은 소들을 오름차순으로 출력하거나, 모두 연결된 경우 0을 출력

in
    6 4
    1 3
    2 3
    1 2
    4 5
out
    4
    5
    6
'''

from collections import deque

# N: 소의 수, M: 연결된 쌍의 수
n, m = map(int, input().split())
# 각 소와 연결된 다른 소들을 저장하는 인접 리스트
graph = [[] for _ in range(n + 1)]

# 소들 간의 연결 관계를 그래프에 저장
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문한 소들을 체크하는 배열
visited = [False] * (n + 1)

def bfs(start):
    # 시작 소를 방문 처리
    visited[start] = True
    q = deque([start])

    while q:
        # 현재 확인할 소를 큐에서 꺼냄
        now = q.popleft()

        # 현재 소와 연결된 모든 소들을 확인
        for i in graph[now]:
            # 아직 방문하지 않은 소라면
            if not visited[i]:
                # 방문 처리하고 큐에 추가
                visited[i] = True
                q.append(i)

# 1번 소부터 시작하여 연결된 모든 소들을 탐색
bfs(1)
# 연결되지 않은 소가 있는지 체크하는 플래그
flag = True
# 모든 소들을 순회하며 연결되지 않은 소들을 출력
for i in range(1, n + 1):
    if not visited[i]:
        print(i)
        flag = False

# 모든 소가 연결되어 있다면 0 출력
if flag:
    print(0)
