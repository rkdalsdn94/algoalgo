# 백준 - 실버2 - 알고리즘 수업 깊이 우선 탐색 3 - 24481 - 그래프, 정렬, dfs 문제
'''
그래프, 정렬, dfs 문제

기존에 풀던 그래프와 dfs를 이용해서 풀면 된다.

풀이 과정
    1. 입력을 받고, m_list를 만든다.
    2. m_list를 이용해서 그래프를 만든다.
    3. dfs 함수를 만들어서 깊이 우선 탐색을 한다.
    4. ck를 출력한다.
'''

import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, r = map(int, input().split())
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# n, m, r = 5, 5, 1
# m_list = [[1, 4], [1, 2], [2, 3], [2, 4], [3, 4]] # 0  \  1  \  2  \  3  \  -1

g = [[] for _ in range(n + 1)]
ck = [-1] * (n + 1)

for i, j in m_list:
    g[i].append(j)
    g[j].append(i)

def dfs(node):
    for i in sorted(g[node]):
        if ck[i] == -1:
            ck[i] = ck[node] + 1
            dfs(i)

ck[r] = 0
dfs(r)

for i in ck[1:]:
    print(i)
