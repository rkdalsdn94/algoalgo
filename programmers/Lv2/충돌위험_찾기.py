# 프로그래머스 - Lv2 - 충돌위험 찾기 - 구현, 시뮬레이션 문제
"""
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 각 로봇의 시간별 이동 경로를 완전히 시뮬레이션
    2. 포인트 간 이동 시 r 좌표를 먼저 변경한 후 c 좌표 변경 (맨해튼 거리)
    3. 각 시간대별로 좌표에 있는 로봇 수를 카운트하여 2대 이상인 경우 위험 상황으로 판단

[풀이 과정]
    1. 각 로봇의 경로를 순회하며 시간별 위치를 기록
       - 현재 위치에서 목표 포인트까지 r 좌표를 먼저 맞춤 (1초에 1칸)
       - 그 다음 c 좌표를 맞춤
    2. 시간대별 위치 정보를 딕셔너리로 집계 {시간: {좌표: 로봇수}}
    3. 각 시간대에서 로봇 수가 2 이상인 좌표의 개수를 합산
"""

def solution(points, routes):

    # 각 로봇의 시간별 위치를 저장할 리스트
    robot_positions = []

    # 각 로봇의 경로를 시뮬레이션
    for route in routes:
        positions = []  # (시간, 좌표) 형태로 저장
        time = 0

        # 시작 포인트 (routes의 첫 번째 포인트 번호는 1부터 시작하므로 -1)
        current_pos = points[route[0] - 1][:]  # 깊은 복사
        positions.append((time, tuple(current_pos)))

        # 경로의 각 포인트를 순서대로 방문
        for i in range(1, len(route)):
            target_pos = points[route[i] - 1]
            r, c = current_pos
            tr, tc = target_pos

            # r 좌표를 먼저 목표값으로 맞춤
            while r != tr:
                time += 1
                r += 1 if r < tr else -1
                positions.append((time, (r, c)))

            # c 좌표를 목표값으로 맞춤
            while c != tc:
                time += 1
                c += 1 if c < tc else -1
                positions.append((time, (r, c)))

            # 현재 위치 업데이트
            current_pos = [r, c]

        robot_positions.append(positions)

    # 각 시간대별로 좌표에 있는 로봇 수를 카운트
    time_positions = {}
    for positions in robot_positions:
        for time, pos in positions:
            if time not in time_positions:
                time_positions[time] = {}
            if pos not in time_positions[time]:
                time_positions[time][pos] = 0
            time_positions[time][pos] += 1

    # 위험 상황 카운트 (같은 시간에 같은 좌표에 2대 이상)
    danger_count = 0
    for time in time_positions:
        for pos, count in time_positions[time].items():
            if count >= 2:
                danger_count += 1

    return danger_count
