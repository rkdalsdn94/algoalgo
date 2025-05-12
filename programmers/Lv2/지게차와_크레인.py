# 프로그래머스 - Lv2 - 지게차와 크레인 - 그래프, bfs, 시뮬레이션 문제
"""
그래프, bfs, 시뮬레이션 문제

[핵심 아이디어]
    1. 창고의 바깥 영역을 별도로 표시하여 외부 공간 확인
    2. BFS를 사용하여 외부 공간과 접하는 컨테이너를 찾음
    3. 요청 타입에 따라 다르게 처리:
       - 길이 1 요청(지게차): 접근 가능한 해당 타입 컨테이너만 제거
       - 길이 2 요청(크레인): 모든 해당 타입 컨테이너 제거
    4. 제거 후 외부 공간을 다시 계산하여 접근성 업데이트
    5. 남은 컨테이너 수 계산

[풀이 과정]
    1. storage를 2차원 배열로 변환하고 외부에 가상의 테두리 추가
    2. 각 요청에 대해:
       - BFS로 외부 공간 표시
       - 외부 공간과 접하는 컨테이너 찾기
       - 요청 타입(지게차/크레인)에 따라 컨테이너 제거
    3. 모든 요청 처리 후 남은 컨테이너 수 반환
"""

from collections import deque

def solution(storage, requests):
    # 2차원 배열로 변환
    board = []
    for row in storage:
        board.append(list(row))

    n, m = len(board), len(board[0])

    # 요청 처리
    for request in requests:
        container_type = request[0]  # 컨테이너 종류

        if len(request) == 1:  # 지게차 요청
            # 외부와 접하는 컨테이너 찾기
            accessible = find_accessible_containers(board, n, m)

            # 접근 가능한 해당 종류 컨테이너 제거
            for i in range(n):
                for j in range(m):
                    if board[i][j] == container_type and accessible[i][j]:
                        board[i][j] = '0'  # 제거된 컨테이너는 '0'으로 표시

        else:  # 크레인 요청
            # 모든 해당 종류 컨테이너 제거
            for i in range(n):
                for j in range(m):
                    if board[i][j] == container_type:
                        board[i][j] = '0'

    # 남은 컨테이너 수 계산
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != '0':
                answer += 1

    return answer

def find_accessible_containers(board, n, m):
    # 상하좌우 이동 방향
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 외부 공간을 표시할 배열, 1: 외부 공간, 0: 컨테이너 또는 미방문 영역
    outside = [[0] * m for _ in range(n)]
    # 접근 가능 컨테이너 표시 배열
    accessible = [[0] * m for _ in range(n)]
    # 바깥 테두리에서 BFS 시작 (가장자리가 전부 외부 공간이라고 가정)
    q = deque()

    # 가상의 외부 공간 시작점 (가장자리)
    # 위쪽과 아래쪽 가장자리
    for j in range(m):
        if board[0][j] == '0':  # 빈 공간이면 외부 공간으로 표시
            q.append((0, j))
            outside[0][j] = 1
        else:  # 컨테이너면 접근 가능
            accessible[0][j] = 1

        if board[n-1][j] == '0':
            q.append((n-1, j))
            outside[n-1][j] = 1
        else:
            accessible[n-1][j] = 1

    # 왼쪽과 오른쪽 가장자리
    for i in range(1, n-1):
        if board[i][0] == '0':
            q.append((i, 0))
            outside[i][0] = 1
        else:
            accessible[i][0] = 1

        if board[i][m-1] == '0':
            q.append((i, m-1))
            outside[i][m-1] = 1
        else:
            accessible[i][m-1] = 1

    # BFS로 외부 공간 탐색
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 내이고 아직 방문하지 않은 빈 공간('0')
            if 0 <= nx < n and 0 <= ny < m and not outside[nx][ny] and board[nx][ny] == '0':
                q.append((nx, ny))
                outside[nx][ny] = 1

    # 외부 공간과 접하는 컨테이너 찾기
    for x in range(n):
        for y in range(m):
            if board[x][y] != '0':  # 컨테이너인 경우
                # 상하좌우 확인해서 외부 공간과 접하는지 확인
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and outside[nx][ny]:
                        accessible[x][y] = 1
                        break

    return accessible

storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
requests = ["A", "BB", "A"]
print(solution(storage, requests)) # 11

storage = ["HAH", "HBH", "HHH", "HAH", "HBH"]
requests = ["C", "B", "B", "B", "B", "H"]
print(solution(storage, requests)) # 4
