# 프로그래머스 - Lv1 - 공원 산책 - 구현, 시뮬레이션
"""
구현, 시뮬레이션

[핵심 아이디어]
    1. 시작 위치('S')를 찾는다
    2. 각 명령(방향과 거리)에 대해 다음 조건을 확인한다:
       - 주어진 방향으로 이동 시 공원 경계를 벗어나는지 확인
       - 이동 경로 중 장애물('X')을 만나는지 확인
    3. 위 조건에 해당하지 않으면 로봇의 위치를 업데이트한다

[풀이 과정]
    1. 공원에서 시작 위치('S')를 찾는다
    2. 각 명령을 파싱하여 방향과 이동할 거리를 얻는다
    3. 로봇이 주어진 방향으로 이동할 때:
       - 경로 중간에 장애물이 있는지 확인
       - 공원 경계를 벗어나는지 확인
    4. 이동이 유효하면 로봇의 현재 위치를 업데이트한다
    5. 모든 명령 수행 후 최종 위치를 반환한다
"""

def solution(park, routes):
    # 방향에 따른 이동 좌표 정의
    move = {
        'E': [0, 1], 'S': [1, 0], 'W': [0, -1], 'N': [-1, 0]
    }
    start_x, start_y = 0, 0

    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start_x, start_y = i, j
                break

    h, w = len(park), len(park[0])  # 공원의 세로, 가로 크기

    # 각 명령 처리
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)

        dx, dy = move[direction]
        nx, ny = start_x, start_y
        valid_move = True

        # 이동 경로 검사
        for _ in range(distance):
            nx += dx
            ny += dy

            # 공원 범위를 벗어나거나 장애물을 만나면 이동 취소
            if nx < 0 or nx >= h or ny < 0 or ny >= w or park[nx][ny] == 'X':
                valid_move = False
                break

        # 유효한 이동인 경우 위치 업데이트
        if valid_move:
            start_x, start_y = nx, ny

    return [start_x, start_y]


print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]) == [2,1])
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]) == [0,1])
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]) == [0,0])
