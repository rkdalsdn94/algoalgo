'''
자료 구조, 우선순위 큐 문제

pypy3로 제출해야 통과할 수 있다. (그래도 5000ms 나온다... 최적화를 좀 더 해야될거 같다...)
문제는 최대힙, 최소힙 이 두개를 잘 다루면 된다.
파이썬에서는 최소힙을 응용해서 최대힙으로 만들어 줄 수 있다. (음수로 push하면 최대힙으로 활용 가능)

그리고 각 min_q, max_q(heapq)에 해당 인덱스로 같이 push를 한 후
둘 중 하나의 값이 pop되면 다른 힙에 있는 값도 pop해야 돼서 인덱스를 같이 push한다.

마지막 while문으로 힙들의 초기화를 한 후에 값 검사 후 출력한다.

처음엔 heapq를 이용해서 바로 풀 수 있을줄 알았는데, 시간이 좀 걸렸다.
구현력 관련된 문제를 좀 더 풀어야 될거 같다.
'''

import heapq as hq

T = int(input())

for _ in range(T):
    k = int(input())
    ck = [0] * k
    max_q, min_q = [], []

    for i in range(k):
        a, b = input().split()
        b = int(b)

        if a == 'I':
            hq.heappush(min_q, (b, i))
            hq.heappush(max_q, (-b, i))
            ck[i] = 1
        elif a == 'D' and b == -1:
            while min_q and not ck[min_q[0][1]]:
                hq.heappop(min_q)
            if min_q:
                ck[min_q[0][1]] = 0
                hq.heappop(min_q)
        elif a == 'D' and b == 1:
            while max_q and not ck[max_q[0][1]]:
                hq.heappop(max_q)
            if max_q:
                ck[max_q[0][1]] = 0
                hq.heappop(max_q)
    
    while max_q and not ck[max_q[0][1]]:
        hq.heappop(max_q)

    while min_q and not ck[min_q[0][1]]:
        hq.heappop(min_q)

    if max_q and min_q: print(-max_q[0][0], min_q[0][0])
    else: print('EMPTY')
