# 백준 - 실버1 - 촌수 계산 - 2644 - 그래프, bfs, dfs 문제
'''
그래프, bfs, dfs 문제

dfs로도 풀 수 있는데, bfs가 더 편해서 bfs 방식으로 풀었다.
처음에 딕셔너리를 써서 사용해야 되나 고민을 좀 하다가 양방향 연결이 필요할거 같아 이중리스트로 빈 배열을 초기화해서 풀었다.
풀이 과정은 간단하다. m_list에다 양방향으로 연결시켜준 뒤 m_list의 a번째 리스트의 값들을 꺼내서 b와 만난다면 그 횟수를 출력하면 된다.
단, 처음 ck를 방문할 때 1부터 시작하므로 b와 같아졌을 때(bfs함수 안에서는 y) return 할 때 -1을 해야된다.

나중에 dfs로도 다시 풀어보려고 한다.

in
    9
    7 3
    7
    1 2
    1 3
    2 7
    2 8
    2 9
    4 5
    4 6
out
    3

in
    9
    8 6
    7
    1 2
    1 3
    2 7
    2 8
    2 9
    4 5
    4 6
out
    -1
'''

from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
m_list = [ [] for _ in range(n + 1) ] # 3
ck = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    m_list[x].append(y)
    m_list[y].append(x)

def bfs(x, y):
    q = deque()
    q.append(x)
    ck[x] = 1

    while q:
        temp = q.popleft()

        if temp == y:
            return ck[y] - 1

        for i in m_list[temp]:
            if not ck[i]:
                q.append(i)
                ck[i] += ck[temp] + 1

    return -1

print(bfs(a, b))