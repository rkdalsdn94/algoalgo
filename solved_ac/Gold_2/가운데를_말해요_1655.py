# 백준 - 골드2 - 가운데를 말해요 - 1655 - 자료 구조, 우선순위 큐 문제
'''
자료 구조, 우선순위 큐 문제

left_heap은 최댓값으로, right_heap은 최솟값으로 구현하면 되는 문제이다.
단, python에서 heap은 최솟값만 지원되기 때문에 최댓값을 구하려면 약간의 꼼수(?)가 필요하다.
방법은 사용할 숫자를 음수로 만들어서 최솟값처럼 사용하면 된다.

heap을 활용할 수 있다면 난이도의 비해 크게 어렵지 않은 문제이다.
'''

import sys; input = sys.stdin.readline
import heapq as hq

n = int(input())
n_list = [ int(input()) for _ in range(n) ]

# 테스트
# n = 7
# n_list = [1,5,2,10,-99,7,5] # 1  \  1  \  2  \  2  \  2  \  2  \  5

left_heap, right_heap = [], []
res = []

for x in n_list:
    if len(left_heap) == len(right_heap):
        hq.heappush(left_heap, (-x, x))
    else:
        hq.heappush(right_heap, x)

    if right_heap and right_heap[0] <= left_heap[0][1]:
        a = hq.heappop(right_heap)
        b = hq.heappop(left_heap)[1]
        hq.heappush(left_heap, (-a, a))
        hq.heappush(right_heap, b)

    res.append(left_heap[0][1])

for i in res:
    print(i)
