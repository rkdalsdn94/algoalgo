# 백준 - 골드2 - 중앙값 구하기 - 2696 - 자료 구조, 우선순위 큐 문제
'''
자료 구조, 우선순위 큐 문제

어제 푼 '가운데를 말해요' 문제랑 똑같이 풀면 되는 문제이다.
해당 코드 파일에 설명을 적어놔서 차이점만 여기서 적으려고 한다.

전 문제랑 차이점은 10개씩 끊어서 들어오는 것과, 2의 배수인거만 고려하면 된다.
그거만 생각한 다음 '가운데를 말해요' 문제랑 똑같이 풀었다.

--- 코드가 더러워서 나중에 리팩토링 하고 싶다... ---
'''

import sys; input = sys.stdin.readline
import heapq as hq

t = int(input())
for _ in range(t):
    m = int(input())
    m_list = list(map(int, input().split()))

    if m >= 10:
        num_range = m // 10

        for _ in range(num_range):
            m_list += list(map(int, input().split()))

    cnt = 0
    res = []
    left_heap, right_heap = [], []

    for x in range(m):
        if x % 2 == 0:
            cnt += 1

            if len(left_heap) == len(right_heap):
                hq.heappush(left_heap, (-m_list[x], m_list[x]))
            else:
                hq.heappush(right_heap, m_list[x])
            
            if right_heap and left_heap[0][1] > right_heap[0]:
                a = hq.heappop(left_heap)[1]
                b = hq.heappop(right_heap)
                hq.heappush(left_heap, (-b, b))
                hq.heappush(right_heap, a)

            res.append(left_heap[0][1])
        else:
            if len(left_heap) == len(right_heap):
                hq.heappush(left_heap, (-m_list[x], m_list[x]))
            else:
                hq.heappush(right_heap, m_list[x])

            if right_heap and left_heap[0][1] > right_heap[0]:
                a = hq.heappop(left_heap)[1]
                b = hq.heappop(right_heap)
                hq.heappush(left_heap, (-b, b))
                hq.heappush(right_heap, a)
    
    print(cnt)
    for i in range(0, cnt, 10):
        print(*res[i : i + 10])
