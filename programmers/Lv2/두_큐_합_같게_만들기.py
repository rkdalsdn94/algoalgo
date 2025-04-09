# 프로그래머스 - Lv2 - 두 큐 합 같게 만들기 - 구현, 자료구조(큐), 그리디 문제
"""
구현, 자료구조(큐), 그리디 문제

[핵심 아이디어]
- 두 큐의 원소 합을 같게 만들기 위해 각 큐가 전체 합의 절반이 되도록 함
- 항상 합이 더 큰 큐에서 작은 큐로 원소를 이동시키는 그리디 방식 적용
- 최악의 경우를 대비해 최대 작업 횟수 제한 설정 (두 큐 길이 합의 2배)

[풀이 과정]
1. 두 큐와 각 큐의 합을 초기화
2. 전체 합이 홀수인 경우 두 큐의 합을 같게 만들 수 없으므로 -1 반환
3. 목표 합계를 전체 합의 절반으로 설정
4. 최대 작업 횟수를 두 큐 길이 합의 2배로 제한 (모든 원소가 한 번씩 이동하고 다시 원위치로 돌아오는 경우)
5. 다음 규칙으로 원소 이동을 반복:
  - 첫 번째 큐의 합이 목표보다 크면: 첫 번째 큐에서 두 번째 큐로 원소 이동
  - 첫 번째 큐의 합이 목표보다 작으면: 두 번째 큐에서 첫 번째 큐로 원소 이동
6. 두 큐의 합이 같아지면 작업 횟수 반환, 최대 작업 횟수 초과 시 -1 반환
"""

from collections import deque

def solution(queue1, queue2):
    # 큐 초기화
    q1 = deque(queue1)
    q2 = deque(queue2)

    # 각 큐의 합계 계산
    sum1 = sum(q1)
    sum2 = sum(q2)

    # 전체 합계 계산
    total_sum = sum1 + sum2

    # 합계가 홀수이면 같게 만들 수 없음
    if total_sum % 2 != 0:
        return -1

    target = total_sum // 2

    # 최대 작업 횟수 계산 (두 큐 길이의 합의 2배)
    max_count = (len(queue1) + len(queue2)) * 2
    count = 0

    # 두 큐의 합이 같아질 때까지 반복
    while sum1 != target and count < max_count:
        if sum1 > target:
            # q1의 합이 더 크면 q1에서 q2로 원소 이동
            val = q1.popleft()
            q2.append(val)
            sum1 -= val
            sum2 += val
        else:
            # q2의 합이 더 크면 q2에서 q1로 원소 이동
            val = q2.popleft()
            q1.append(val)
            sum2 -= val
            sum1 += val
        count += 1

    # 두 큐의 합이 같아졌는지 확인
    if sum1 == target:
        return count
    else:
        return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5])) # -1
