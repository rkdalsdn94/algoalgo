# 백준 - 골드3 - 치즈 - 2638 - 그래프, 시뮬레이션, bfs 문제
'''
그래프, 시뮬레이션, bfs 문제

[핵심 아이디어]
    1. 외부 공기와 내부 공기를 구분하기 위해 BFS 활용
    2. 외부 공기는 2로 표시하여 내부 공기(0)와 구분
    3. 치즈(1)가 녹는 조건은 상하좌우 네 방향 중 외부 공기(2)와 2변 이상 접촉하는 경우
    4. 매 시간마다 외부 공기를 새롭게 계산하고, 조건을 만족하는 치즈를 녹임

[풀이 과정]
    1. 치즈가 존재하는 동안 반복:
       - (0,0)에서 시작하여 BFS로 외부 공기를 2로 표시
       - 모든 치즈 좌표를 확인하며 녹는 조건을 만족하는 치즈 위치 저장
       - 저장된 위치의 치즈를 모두 녹임(0으로 변경)
       - 외부 공기 표시(2)를 다시 0으로 초기화
       - 시간(res) 증가
    2. 치즈가 모두 녹으면 걸린 시간 출력
'''

from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m = 8, 9
# board = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0, 1, 1, 0],
#     [0, 0, 1, 1, 1, 1, 1, 1, 0],
#     [0, 0, 1, 1, 1, 1, 1, 0, 0],
#     [0, 0, 1, 1, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ] # 4

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y):
    """외부 공기를 찾아 2로 표시하는 BFS 함수"""
    q = deque([(x, y)])
    ck = [[0] * m for _ in range(n)]  # 방문 체크 배열

    while q:
        a, b = q.popleft()
        ck[a][b] = 1
        board[a][b] = 2  # 외부 공기를 2로 표시

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            # 범위 내이고 미방문이며 치즈가 아닌 곳만 탐색
            if 0 <= nx < n and 0 <= ny < m and ck[nx][ny] == 0 and board[nx][ny] != 1:
                q.append((nx, ny))
                ck[nx][ny] = 1
                board[nx][ny] = 2

def board_check(board):
    """치즈가 남아있는지 확인하는 함수"""
    temp = 0
    for i in range(n):
        temp += sum(board[i])
    return temp >= 1

def check(x, y, board):
    """해당 치즈가 녹는지 확인하는 함수"""
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 외부 공기(2)와 접촉한 변의 개수 계산
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 2:
            cnt += 1
    return cnt >= 2

res = 0
while board_check(board):  # 치즈가 있는 동안 반복
    res += 1
    bfs(0, 0)  # 외부 공기 표시

    # 녹을 치즈 위치 저장
    melt = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and check(i, j, board):
                melt.append((i, j))

    # 저장된 위치의 치즈를 모두 녹임
    for x, y in melt:
        board[x][y] = 0

    # 외부 공기 표시 초기화
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                board[i][j] = 0

print(res)
