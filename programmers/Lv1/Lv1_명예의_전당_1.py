# 프로그래머스 - Lv1 - 명예의 전당 - 자료 구조(heap) 문제
'''
자료 구조(heap) 문제

[핵심 아이디어]
    최소 힙(min heap)을 사용하여 명예의 전당에 오른 상위 k개의 점수를 관리
    힙의 루트 노드는 항상 힙 내에서 가장 작은 값이므로, 명예의 전당의 최하위 점수를 O(1) 시간에 확인할 수 있음
    새로운 점수가 들어올 때마다 힙을 업데이트하고, 매일 발표되는 최하위 점수(힙의 루트 노드)를 기록

[풀이 과정]
    1. 빈 최소 힙 heap과 결과를 저장할 리스트 answer 초기화
    2. score 배열의 각 점수를 순차적으로 처리:
       - 힙의 크기가 k보다 작으면 현재 점수를 힙에 추가
       - 힙의 크기가 k와 같으면, 현재 점수와 힙의 최솟값을 비교:
         * 현재 점수가 힙의 최솟값보다 크면, 힙의 최솟값을 제거하고 현재 점수를 힙에 추가(heappushpop).
       - 매일 힙의 최솟값(temp[0])을 answer에 추가
    3. 최종적으로 answer 배열을 반환
'''

import heapq

def solution(k, score):
    answer = []
    heap = []

    for i in score:
        if len(heap) < k:
            heapq.heappush(heap, i)
            answer.append(heap[0])
        else:
            heapq.heappushpop(heap, i)
            answer.append(heap[0])

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]) == [10, 10, 10, 20, 20, 100, 100])
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]) == [0, 0, 0, 0, 20, 40, 70, 70, 150, 300])
