'''
자료 구조, 우선순위 큐 문제

input을 sys.stdin.readline 이걸로 바꾸지 않으면 시간 초과가 난다.
heap 자료 구조를 사용하는 문제다.
입력받은 값이 0이 아니면 heap에다 넣고, 아닐 경우 빼야 되는데
힙에 값을 넣을 때 절댓값이랑 원본값 둘 다 넣은 상태(비교를 위해)에서 원본값을 출력하면 된다.
ㄴ> 절댓값이 같을 경우 가장 작은 수를 출력하기 위해 절댓값, 원본값 둘 다 넣는다
'''

import heapq as hq
# import sys
# input = sys.stdin.readline

# n = int(input())
q = []

# 테스트 
test = [18, 1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0] # -1, 1, 0, -1, -1, 1, 1, -2, 2, 0
for x in test:
# for _ in range(n):
    # x = int(input())

    if x:
        hq.heappush(q, (abs(x), x))
        continue
    if q:
        print(hq.heappop(q)[1])
    else:
        print(0)
