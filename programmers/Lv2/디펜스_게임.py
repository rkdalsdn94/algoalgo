# 프로그래머스 - Lv2 - 디펜스 게임 - 우선순위 큐(힙), 그리디 문제
"""
우선순위 큐(힙), 그리디 문제

[핵심 아이디어]
   1. 무적권은 적의 수가 많은 라운드에 사용하는 것이 가장 효율적이다
   2. 힙(최대 힙)을 사용하여 지금까지 진행한 라운드 중 가장 적의 수가 많았던 라운드를 추적한다
   3. 병사 수가 부족하면 무적권을 사용하여 가장 많은 적이 있는 라운드를 처리한다

[풀이 과정]
   1. 각 라운드를 순회하면서:
      a. 현재 라운드의 적 수를 최대 힙에 추가하고 총 적의 수에 더한다
      b. 총 적의 수가 보유한 병사 수보다 많아지면:
         - 무적권이 남아있으면, 최대 힙에서 가장 큰 적의 수를 제거하고 총 적의 수에서 뺀다
         - 무적권이 없으면 게임 종료
      c. 라운드 카운트를 증가시킨다
   2. 최종적으로 처리 가능한 라운드 수를 반환한다
"""

from heapq import heappop, heappush

def solution(n, k, enemy):
    rounds_completed = 0  # 완료한 라운드 수
    total_enemies = 0     # 지금까지 등장한 총 적의 수
    max_heap = []

    for e in enemy:
        # 현재 라운드의 적 수를 최대 힙에 추가 (음수로 저장하여 최대 힙 구현)
        heappush(max_heap, -e)
        total_enemies += e

        # 적의 수가 보유한 병사 수보다 많다면
        if total_enemies > n:
            # 무적권이 남아있지 않으면 게임 종료
            if k == 0:
                break

            # 무적권 사용: 가장 많은 적이 있는 라운드를 처리
            # (최대 힙에서 가장 큰 값을 제거하고 총 적의 수에서 뺌)
            total_enemies += heappop(max_heap)  # 음수 값을 더하면 빼는 효과
            k -= 1  # 무적권 사용 횟수 감소

        rounds_completed += 1

    return rounds_completed

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1])) # 5
print(solution(2, 4, [3, 3, 3, 3])) # 4
