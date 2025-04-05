# 프로그래머스 - Lv3 - 야근 지수 - 구현, 자료구조(힙), 그리디 문제
"""
구현, 자료구조(힙), 그리디 문제

[핵심 아이디어]
    1. 야근 피로도는 남은 작업량의 제곱합이므로, 큰 작업량을 먼저 줄이는 것이 유리하다
    2. 매번 가장 큰 작업량을 1씩 줄이는 작업을 n번 반복한다
    3. 최대 힙(Max Heap)을 활용하여 가장 큰 작업량을 효율적으로 찾는다

[풀이 과정]
    1. works 배열의 모든 작업량을 최대 힙에 넣는다
    2. n번 반복하면서 매번 다음 작업을 수행한다:
       a. 힙에서 가장 큰 작업량을 꺼낸다
       b. 작업량이 0보다 크면 1 감소시킨다
       c. 감소된 작업량을 다시 힙에 넣는다
    3. 모든 반복이 끝나면 힙에 남은 작업량들의 제곱합을 계산하여 반환한다
    4. 만약 n이 총 작업량보다 크거나 같다면, 모든 일을 처리할 수 있으므로 0을 반환한다
"""

import heapq

def solution(n, works):
    # 작업량이 없거나 모든 작업을 처리할 수 있는 경우
    if sum(works) <= n:
        return 0

    # 최대 힙을 구현하기 위해 작업량에 -1을 곱해 최소 힙에 넣음
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)

    # n번 반복하며 가장 큰 작업량 감소
    for _ in range(n):
        # 가장 큰 작업량을 꺼내서 1 감소시키고 다시 힙에 넣음
        max_work = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_work + 1)  # 음수이므로 +1이 1 감소와 같음

    # 남은 작업량의 제곱합 계산 (음수를 양수로 변환하여 제곱)
    answer = sum((-work) ** 2 for work in max_heap)

    return answer
