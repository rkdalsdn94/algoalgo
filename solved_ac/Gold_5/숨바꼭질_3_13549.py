# 백준 - 골드5 - 숨바꼭질 3 - 13549 - 그래프, bfs, 다익스트라(dijkstra, 데이크스트라) 문제
'''
그래프, bfs, 다익스트라(dijkstra, 데이크스트라) 문제

힌트를 보면 5 - 10, 9 - 18, 17 이렇게 이동한다. 결과적으로 res의 인덱스 범위를 k보다 크게 설정해야 한다.
즉, 최대 범위를 100_001로 설정하고 풀어야지 풀린다... 이거 때문에 좀 헤맸었다.

문제의 분류에선 데이크스트라를 사용하지만 내 풀이에선 생각을 못 했었다.
그래서, 해당 방법은 다른 사람의 풀이를 참고에서 제일 아래 주석으로 붙여놨다.
참고한 링크는 여기이다. - https://velog.io/@hamfan524/백준-13549번-Python-파이썬-Dijkstra

bfs 풀 듯이 풀었다. 뭔가 쉬운거 같으면서 복잡한 문제였다. 인덱스 범위를 잘 신경써야 된다.

6월 28일날 재채점 됐는데 계속 99%에서 틀렸다. 어떻게 해결해야 할지 감이 잘 안와서 아래에 있는 질문 게시판의 반례를 참고했다.
    - https://www.acmicpc.net/board/view/121219
해결하는 방법은 간단하다. if 문의 순서를 기존의 위치에서 a - 1, a + 1 로 바꾸기만 하면 해결할 수 있다.
'''

from collections import deque

n, k = map(int, input().split())

# 테스트
# n, k = 5, 17 # 2
# n, k = 4, 6 # 1

res = [-1] * 100_002 # # -1로 설정하는 이유는 k가 n이랑 같거나, 2배이면 답이 0이된다. (바로 순간이동이 가능함.)
ck = [0] * 100_002
res[n] = 0
ck[n] = 1

q = deque([n])

while q:
    a = q.popleft()

    if a == k:
        break
    if a * 2 <= 100_001 and ck[a * 2] == 0:
        q.appendleft(a * 2)
        ck[a * 2] = 1
        res[a * 2] = res[a]
    if a - 1 >= 0 and ck[a - 1] == 0:
        q.append(a - 1)
        ck[a - 1] = 1
        res[a - 1] = res[a] + 1
    if a + 1 <= 100_001 and ck[a + 1] == 0:
        q.append(a + 1)
        ck[a + 1] = 1
        res[a + 1] = res[a] + 1

print(res[k])

'''
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

n, k = map(int, input().split())
dp = [inf] * (100001)
heap = []

def dijkstra(n, k):
    if k <= n:
        print(n - k)
        return
    
    heappush(heap, [0, n])
    while heap:
        w, n = heappop(heap)
        for nx in [n + 1, n - 1, n * 2]:
            if 0 <= nx <= 100000:
                if nx == n * 2 and dp[nx] == inf:
                    dp[nx] = w
                    heappush(heap, [w, nx])
                elif dp[nx] == inf:
                    dp[nx] = w + 1
                    heappush(heap, [w + 1, nx])
    print(dp[k])

dijkstra(n, k)
'''