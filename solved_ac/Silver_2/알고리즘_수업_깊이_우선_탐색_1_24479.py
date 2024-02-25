# 백준 - 실버2 - 알고리즘 수업 깊이 우선 탐색 1 - 24479 - 그래프, 정렬, dfs 문제
'''
그래프. 정렬, dfs 문제

처음 틀린 풀이에서 왜 안되는지 고민하다 반례를 찾았다. (제일 아래 주석으로 적음)
처음 코드에선 num을 인자로 받아서 처리했다. 근데, 이렇게 하니까 num 값이 증가해야 될 부분에서 증가하지 않는 문제가 발생함
따라서, num을 외부로 빼고 전역 변수로 활용했다.
풀이는 기존의 그래프 문제를 풀 듯이 풀면 된다.
    - bfs 처럼 stack을 활용해서 풀 수도 있다. (문제가 깊이 우선 탐색이라 dfs로 풀음)

풀이 과정
 - n, m, r 과 그래프를 양방향으로 입력받고, 0으로 초기화 한 방문한 곳인지 체크를 위한 ck와 정답으로 출력할 res를 n + 1의 크기로 초기화한다.
 - 위 과정을 다 진행한 후 dfs 를 r부터 시작한다.
 - 이후 정답으로 출력하기 위해 몇 번째 방문 여부를 체크하기 위해 cnt를 global로 만든 뒤, g의 r번째 (함수 내에선 node)를 정렬해서 반복한다.
    - 정렬된 g[node]가 방문하지 않았으면 res의 해당 부분을 cnt로 만들고, cnt의 값도 증가시킨 뒤, 해당 노드를 dfs로 다시 실행시킨다.
 - 위 과정을 반복한 뒤 res의 1번째 인덱스부터 한 줄씩 출력하면 된다.

in
    5 5 1
    1 4
    1 2
    2 3
    2 4
    3 4
out
    1
    2
    3
    4
    0
'''

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, r = map(int, input().split())
g = [[] for _ in range(n + 1)]
ck = [0] * (n + 1)
res = [0] * (n + 1)
cnt = 2

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(node):
    global cnt

    for i in sorted(g[node]):
        if not ck[i]:
            res[i] = cnt
            cnt += 1
            ck[i] = 1
            dfs(i)

res[r] = 1
ck[r] = 1
dfs(r)

for i in res[1:]:
    print(i)

'''
처음 틀린 코드
아래 코드에 대한 반례
in
    5 4 3
    1 2
    2 3
    3 4
    4 5
out
    3
    2
    1
    4
    5
아래 코드 out
    3
    2
    1
    2
    3

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m, r = map(int, input().split())
g = [[] for _ in range(n + 1)]

ck = [0] * (n + 1)
res = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(num, node):
    for i in sorted(g[node]):
        if not ck[i]:
            res[i] = num + 1
            ck[i] = 1
            dfs(num + 1, i)

res[r] = 1
ck[r] = 1
dfs(1, r)

for i in res[1:]:
    print(i)
'''
