# 카드 정렬하기 - 1715
import heapq
n = 3
n_list = [10,20,40]
heapq.heapify(n_list)
# n = int(input())
# n_list = ([ int(input()) for _ in range(n) ])
# heapq.heapify(n_list)
res = 0
while len(n_list) != 1:
    a = heapq.heappop(n_list)
    b = heapq.heappop(n_list)
    res += (a+b)
    heapq.heappush(n_list, a+b)

print(res)