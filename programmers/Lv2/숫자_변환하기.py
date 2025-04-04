# 프로그래머스 - Lv2 - 숫자 변환하기 - bfs 문제
"""
bfs 문제

[핵심 아이디어]
    1. 최소 연산 횟수를 구하는 문제이므로 BFS를 활용하여 탐색
    2. x에서 시작하여 세 가지 연산(+n, *2, *3)을 적용하며 y에 도달하는 최단 경로 찾기
    3. 중복 계산을 피하기 위해 방문 체크 배열 활용
    4. y 범위까지만 연산을 수행하여 불필요한 계산 방지

[풀이 과정]
    1. 큐를 사용하여 현재 숫자와 연산 횟수를 저장
    2. 방문 체크 배열을 통해 이미 계산한 숫자는 다시 계산하지 않음
    3. 세 가지 연산을 적용한 결과가 y 이하일 경우에만 큐에 추가
    4. y에 도달하면 해당 시점의 연산 횟수를 반환
    5. 큐가 빌 때까지 y에 도달하지 못하면 변환이 불가능하므로 -1 반환
"""
from collections import deque

def solution(x, y, n):
    if x == y:  # 이미 같은 경우 변환 필요 없음
        return 0

    q = deque([(x, 0)])  # (현재 숫자, 연산 횟수)
    visited = {x}  # 방문한 숫자 추적 (중복 방지)

    while q:
        num, count = q.popleft()

        # 세 가지 연산 적용
        operations = [num + n, num * 2, num * 3]

        for next_num in operations:
            # y를 초과하지 않고 아직 방문하지 않은 숫자인 경우
            if next_num <= y and next_num not in visited:
                if next_num == y:  # y에 도달한 경우
                    return count + 1

                visited.add(next_num)
                q.append((next_num, count + 1))

    return -1  # y에 도달할 수 없는 경우

print(solution(10, 40, 5))  # 2
print(solution(10, 40, 30))  # 1
print(solution(2, 5, 4))    # -1
