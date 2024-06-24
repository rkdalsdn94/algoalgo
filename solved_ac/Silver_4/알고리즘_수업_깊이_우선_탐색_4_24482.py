# 백준 - 실버2 - 깊이 우선 탐색 4 - 24482 - 그래프, 정렬, dfs 문제
'''
그래프, 정렬, dfs 문제

문제에 주어진 조건에 따라 dfs를 구현하면 된다.
처음에 문제를 제대로 읽지 않아, m_list를 만들어야 되는데 n_list로 만들었다가 계속 틀렸다.
범위를 n + 1 크기로 만들면 더 편한데, 그냥 n으로 만들어서 풀었다.

풀이 과정
    1. 입력을 받고, m_list를 만든다.
    2. 그래프 g를 만든다.
    3. dfs 함수를 정의하고, dfs를 실행한다.
        3.1. ck에 depth를 저장한다.
        3.2. g를 순회하면서 dfs를 실행한다.
    4. ck를 출력한다.
'''

import sys; sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n, m, r = map(int, input().split())
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# n, m, r = 5, 5, 1
# m_list = [[1, 4], [1, 2], [2, 3], [2, 4], [3, 4]] # 0  \  3  \  2  \  1  \  -1

g = [[] for _ in range(n)]

for i, j in m_list:
    g[i - 1].append(j - 1)
    g[j - 1].append(i - 1)

ck = [-1] * n

def dfs(depth, g, r):
    ck[r] = depth

    for i in sorted(g[r], reverse=True):
        if ck[i] == -1:
            dfs(depth + 1, g, i)

dfs(0, g, r - 1)

for i in ck:
    print(i)
