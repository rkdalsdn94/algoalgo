# 백준 - 트리의 부모 찾기 - 11725 - 실버2 - 트리, dfs, bfs, 그래프 문제
'''
트리, dfs, bfs, 그래프 문제

dfs, bfs 둘 다 푸는 방식은 똑같다.
입력 받을 때 a, b 서로 연결 시킨 다음, 방문한 노드를 체크하는 느낌으로 res 변수를 초기화 한다.
res 변수의 노드들 중 방문하지 않은 노드를 방문할 때 부모 노드를 저장하는 방식으로 풀면 된다.

dfs 방식에선 input = sys.stdin.readline 이 없으면 시간 초과가 나오고,
bfs 방식에선 사용하지 않을 경우 4초 정도 차이가 난다. 자주 사용하진 않지만 필요한 순간에는 사용하면 좋을거 같다.
'''

# dfs 방식
import sys; sys.setrecursionlimit(10 ** 9); input = sys.stdin.readline

n = int(input())
tree = [ [] for _ in range(n + 1) ]
res = [ 0 for _ in range(n + 1) ]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 테스트
# n = 7
# tree = [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]] # 4  6  1  3  1  4
# res = [0] * (n + 1)

def dfs(a):
    for i in tree[a]:
        if res[i] == 0:
            res[i] = a
            dfs(i)

dfs(1)

print(*res[2:], sep='\n')


'''
bfs 방식
'''
import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
tree = [ [] for _ in range(n + 1) ]
res = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# n = 7
# tree = [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]] # 4  6  1  3  1  4
# res = [0] * (n + 1)
q = deque([1])

while q:
    a = q.popleft()

    for i in tree[a]:
        if res[i] == 0:
            res[i] = a
            q.append(i)

print(*res[2:], sep='\n')
