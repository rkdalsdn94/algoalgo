'''
in
    9
    0
    12345678
    1
    2
    0
    0
    0
    0
    32
out
    0
    1
    2
    12345678
    0
'''

import heapq
import sys

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    temp = int(sys.stdin.readline())

    if temp != 0:
        heapq.heappush(q, temp)
    else:
        try:
            print(heapq.heappop(q))
        except:
            print(0)

