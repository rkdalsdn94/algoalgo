# 백준 - 골드4 - 이분 그래프 - 1707 - 그래프, bfs, dfs 문제
'''
그래프, bfs, dfs 문제

문제를 해석하는 데 시간이 걸린다.
해석하고 난 뒤는 bfs 또는 dfs로 문제를 풀 수 있다.
다음의 풀이 영상을 참고 후 문제를 풀었다. (JAVA 풀이)
    - https://www.youtube.com/watch?v=mDSQfb5Rqc4

풀이 과정
 - 그래프를 입력받고, 방문 여부를 체크하기 위한 ck변수와 그래프 초기화한다.
 - 모든 노드를 탐색해야 하므로 for문을 실행하면서 dfs를 실행한다. (방문하지 않은 노드만)
    - dfs 안에서도 이분 그래프가 가능한지 여부를 확인한다.
 - res가 True라면 YES를 출력하고 아니면 NO를 출력한다.
'''

import sys; sys.setrecursionlimit(10 ** 7)

def dfs(start, group):
    ck[start] = group # group을 1 또는 -1로 지정

    for i in g[start]:
        if not ck[i]:
            temp = dfs(i, -group)

            if not temp:
                return False
        elif ck[i] == ck[start]: # 이 전의 값과 같은 그룹이라면
            return False
    return True

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    g = [[] for _ in range(v + 1)]
    ck = [0] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    for i in range(1, v + 1):
        if not ck[i]:
            res = dfs(i, 1)

            if not res:
                break

    print('YES' if res else 'NO')
