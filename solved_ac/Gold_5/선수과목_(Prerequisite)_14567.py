# 백준 - 골드5 - 선수과목 (Prerequisite) - 14567 - dp, 그래프, 위상 정렬 문제
'''
dp, 그래프, 위상 정렬 문제

최근에 푼 '백준 - 줄 세우기(2252)' 문제와 비슷하면서 조금 더 응용하면 되는 문제이다.
개인적으로 줄 세우기 문제보다 이 문제가 더 어렵게 느껴졌다.(난이도는 이 문제가 더 낮다...)

위상 정렬을 이용해서 풀면 되는 문제인 데, q에 append 할 때와 정답을 출력할 때 조금만 생각하면 풀 수 있다.
학기 시작 후 바로 들을 수 있는 과목과 바로 시작할 수 있다는 표시인 1로 append 한다.
그 다음 q에서 값을 하나 씩 꺼낸 다음 해당 과목들은 선수과목의 조건을 만족시켜야 되므로 cnt를 1씩 더해가며 append 한다.
이때 res에도 같이 cnt를 추가해가며 값을 수정한다.

위에서 얘기한 줄 세우기 문제랑 다른 부분이 res를 초기화할 때도 조심해야 한다.
줄 세우는 문제에선 append 만 쭉 해도 괜찮은 데, 해당 문제에선 그렇게하면 값이 빈다. 그래서 직접 res의 인덱스 값을 수정하는 방식으로 바꿨다.
'''

from collections import deque
import sys; input=sys.stdin.readline

n, m = map(int, input().split())
g = [ [] for _ in range(n + 1) ]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    indegree[b] += 1
# print(g, indegree)

# 테스트
# n, m = 3, 2
# g = [[], [2], [3], []]
# indegree = [0, 0, 1, 1] # 1 2 3
# n, m = 6, 4
# g = [[], [2, 3], [5], [], [5], [], []]
# indegree = [0, 0, 1, 1, 0, 2, 0] # 1 2 2 1 3 1

def topology_sort():
    q = deque()
    res = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append([i, 1])
            res[i] = 1

    while q:
        a, cnt = q.popleft()

        for i in g[a]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append([i, cnt + 1])
                res[i] = cnt + 1

    print(*res[1:])

topology_sort()
