# 백준 - 골드3 - DFS 스페셜 저지 - 16964 - 그래프, 정렬, dfs 문제
'''
그래프, 정렬, dfs 문제

PyPy3로 제출해야 된다. (이렇게 해도 6000ms가 나옴)
    q 부분을 deque으로 바꾸고, edge_list를 안 쓰면 조금 더 빠를거 같긴 하지만, 애초에 느린 코드다.

풀이 과정
    1. 입력을 받고, edge_list와 ck_dfs를 만든다.
    2. 그래프 g를 만든다.
    3. dfs 함수를 정의하고, dfs를 실행한다.
        3.1. x를 pop하고, q가 없다면 1을 출력하고 종료한다.
        3.2. ck[x]를 1로 바꾼다.
        3.3. g[x]를 정렬하고, q[0]이 g[x]에 있다면 dfs를 실행한다.
    4. ck_dfs[0]이 1이 아니라면 0을 출력하고 종료한다.
    5. dfs를 실행한다.
    6. dfs가 False라면 0을 출력하고 종료한다.
'''

import sys; input=sys.stdin.readline

n = int(input())
edge_list = [list(map(int, input().split())) for _ in range(n - 1)]
ck_dfs = list(map(int, input().split()))

# 테스트
# n = 4
# edge_list = [[1, 2], [1, 3], [2, 4]]
# ck_dfs = [1, 2, 3, 4] # 0
# n = 4
# edge_list = [[1, 2], [1, 3], [2, 4]]
# ck_dfs = [1, 2, 4, 3] # 1
# n = 4
# edge_list = [[1, 2], [1, 3], [2, 4]]
# ck_dfs = [1, 3, 2, 4] # 1

g = [[] for _ in range(n + 1)]
for i, j in edge_list:
    g[i].append(j)
    g[j].append(i)

ck = [0] * (n + 1)

def dfs(q):
    x = q.pop(0)

    if not q:
        print(1)
        exit(0)

    ck[x] = 1
    for _ in sorted(g[x]):
        if q[0] in g[x] and ck[q[0]] == 0:
            dfs(q)

    return False

if ck_dfs[0] != 1:
    print(0)
    exit(0)
if not dfs(ck_dfs):
    print(0)
