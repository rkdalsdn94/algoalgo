'''
in
    3 2
    1 65
    5 23
    2 99
    10
    2
out
    164
'''
import heapq
from sys import stdin

input = stdin.readline
n, k = map(int, input().split())
jewelry_info = [] # 보석 정보
bag = []          # 가방
temp = []
res = 0

for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewelry_info, [m, v])

for _ in range(k):
    c = int(input())
    heapq.heappush(bag, c)

for _ in range(k):
    c = heapq.heappop(bag)

    while jewelry_info and c >= jewelry_info[0][0]:
        (m, v) = heapq.heappop(jewelry_info)
        heapq.heappush(temp, -v)
    
    if temp:
        res -= heapq.heappop(temp)
    elif not jewelry_info:
        break

print(res)