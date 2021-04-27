'''
in
    13
    input_list = 0, 1, 2, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0
out
    res = 0,2,1,3,2,1,0,0
'''
import heapq
import sys

# 파이썬 기본 heapq에는 minHeap만 지원한다 약간 응용을 해야됨
n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    temp = int(sys.stdin.readline())

    if temp != 0:
        heapq.heappush(heap, (-temp, temp)) # 여기서 응용 (우선순위, 값) 이런 느낌
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)

