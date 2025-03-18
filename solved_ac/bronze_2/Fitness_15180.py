# 백준 - 브론즈2 - Fitness - 15180 - 시뮬레이션, 구현
"""
시뮬레이션, 구현 문제

[핵심 아이디어]
    1. 8개의 피트니스 역이 원형으로 배치되어 있어 시계/반시계 방향으로 이동할 수 있다
    2. 계획이 최소 5개의 서로 다른 역을 방문해야 하며 중복 방문이 없어야 한다
    3. 시작 역부터 시작하여 각 단계(A/C + 숫자)에 따라 다음 역을 계산
    4. 방문한 역들을 저장하고 조건에 맞는지 확인

[풀이 과정]
    1. 시작 역을 방문 역 리스트에 추가
    2. 각 단계를 처리:
       - 'A'(반시계) 또는 'C'(시계) 방향으로 주어진 숫자만큼 이동하여 다음 역 계산
       - 계산된 역을 방문 역 리스트에 추가
    3. 모든 단계 처리 후:
       - 방문한 역들을 공백으로 구분하여 출력
       - 방문한 서로 다른 역이 5개 미만이거나 중복 방문이 있으면 "reject" 추가
"""

def calculate_next_station(current, direction, distance):
    if direction == 'A':  # 반시계 방향
        next_station = (current - distance) % 8
    else:  # 시계 방향 (C)
        next_station = (current + distance) % 8

    # 0번 역은 없으므로 8번으로 변경
    return 8 if next_station == 0 else next_station

start_station = int(input())  # 시작 역
visited = [start_station]     # 방문한 역들을 저장하는 리스트
current = start_station       # 현재 역
visited_set = {start_station} # 방문한 역들의 집합 (중복 확인용)
has_duplicates = False        # 중복 방문 여부

while True:
    step = input()
    if step[0] == '#':  # 종료 조건
        break

    direction = step[0]       # 'A' 또는 'C'
    distance = int(step[1])   # 이동할 역 수

    # 다음 역 계산
    current = calculate_next_station(current, direction, distance)

    # 중복 방문 확인
    if current in visited_set:
        has_duplicates = True

    # 방문한 역 추가
    visited.append(current)
    visited_set.add(current)

print(*visited, end='')
if len(visited_set) < 5 or has_duplicates:
    print(" reject")
else:
    print()
