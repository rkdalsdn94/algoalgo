# 프로그래머스 - Lv3 - 아이템 줍기 - 그래프, bfs 문제
"""
그래프, bfs 문제

참고 : https://jyeonnyang2.tistory.com/247

[핵심 아이디어]
    1. 좌표를 2배로 확대하여 테두리 추출의 정밀도를 높인다
    2. 모든 직사각형 영역을 채운 후, 외부 공간과 인접한 경계만을 테두리로 설정한다
    3. bfs를 사용하여 테두리를 따라 캐릭터에서 아이템까지의 최단거리를 구한다

[풀이 과정]
    1. 좌표계를 2배로 확대하여 102x102 크기의 board 생성
    2. 모든 직사각형의 내부 영역을 1로 채움
    3. (0,0)에서 bfs를 실행하여 외부 공간을 탐색하고 테두리 추출
    4. 외부 공간과 인접한 직사각형 경계를 실제 이동 가능한 테두리로 설정
    5. 캐릭터 위치에서 시작하여 bfs로 아이템까지의 최단거리 계산
    6. 확대된 좌표계에서의 거리를 원래 단위로 변환하여 반환
"""

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표를 2배로 확대
    board = [[0] * 102 for _ in range(102)]

    # 직사각형 내부를 모두 채움
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] = 1

    # 테두리만 남기고 내부는 0으로 변경
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2

        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                board[i][j] = 0

    # bfs로 최단거리 계산
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    queue = deque([(characterX * 2, characterY * 2, 0)])
    ck = [[0] * 102 for _ in range(102)]
    ck[characterX * 2][characterY * 2] = 1

    while queue:
        x, y, dist = queue.popleft()

        if x == itemX * 2 and y == itemY * 2:
            return dist // 2

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[nx][ny] == 1 and not ck[nx][ny]:
                    ck[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1

a, b, c, d, e = [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8
print(solution(a, b, c, d, e)) # 17

a, b, c, d, e = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1
print(solution(a, b, c, d, e)) # 11

a, b, c, d, e = [[1,1,5,7]], 1, 1, 4, 7
print(solution(a, b, c, d, e)) # 9

a, b, c, d, e = [[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10
print(solution(a, b, c, d, e)) # 15

a, b, c, d, e = [[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3
print(solution(a, b, c, d, e)) # 10
