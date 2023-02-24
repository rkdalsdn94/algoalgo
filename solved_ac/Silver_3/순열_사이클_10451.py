# 백준 - 실버3 - 순열 사이클 - 10451 - 순열 사이클 분할, 그래프 문제
'''
순열 사이클 분할, 그래프 문제

solved.ac 에서 '순열 사이클 분할'이라는 분류로 들어가는데 그냥 그래프 문제로 봐도 무방할거 같다. dfs나 dfs로 구현할 수 있다.
구현 방식은 ck변수를 통해 '해당 인덱스가 방문한 곳'이면 사이클이 이루어진 것으로 1을 더해준다.
'해당 인덱스가 방문한 곳'을 생각하면 쉽게 구현할 수 있다.

in
    2
    8
    3 2 7 8 1 4 5 6
    10
    2 1 3 4 5 6 7 9 10 8
out
    3
    7
'''

from collections import deque

t = int(input())

def cycle_detection_bfs(v): # deque을 활용한 bfs로 푼 방식
    q = deque([v])
    ck[v] = 1

    while q:
        x = q.popleft()
        temp = n_list[x]

        if ck[temp] == 0:
            ck[temp] = 1
            q.append(temp)
    return 1

def cycle_detection_dfs(v): # dfs 재귀로 푼 방식
    if ck[v] == 1:
        return
    ck[v] = 1
    cycle_detection_dfs(n_list[v])
    return 1

for _ in range(t):
    n = int(input())
    n_list = [0] + list(map(int, input().split()))
    ck = [0] * (n + 1)
    res = 0

    # 사이클 체크
    for i in range(1, n + 1):
        if ck[i] == 0:
            res += cycle_detection_bfs(i)
            # res += cycle_detection_dfs(i)

    print(res)
