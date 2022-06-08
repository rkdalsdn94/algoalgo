'''
힙, 구현 문제

힙을 잘 써서 구현해야 되는 문제로 느껴졌다.
단순하면서도 어려웠다.

jobs를 정렬한 후에 cnt변수로 while 조건을 세운다.
그리고, 주의할 점은 heap에다 push 할 때 b, a 순으로 푸시 한 다음 계산하는게 좀 더 편하다.
'''
from heapq import heappush as hpush, heappop as hpop

def solution(jobs: list):
    answer = 0
    cnt, last, time = 0, -1, 0
    heap = []
    jobs.sort(key=lambda x: (x[1], x[0]))

    while cnt < len(jobs):
        for a, b in jobs:
            if last < a <= time:
                hpush(heap, [b, a])

        if heap:
            a, b = hpop(heap)
            last = time
            time += a
            answer += (time - b)
            cnt += 1
        else:
            time += 1

    return answer // len(jobs)

print(solution([[0,3], [1,9], [2,6]])) # 9
