# 프로그래머스 - Lv1 - 같은 색으로 색칠하기 - 그래프 문제
"""
그래프 문제

bfs를 단 한 번만 적용하면 되는 단순한 문제

[핵심 아이디어]
    1. 현재 위치(h, w)에서 상하좌우로 인접한 네 칸을 확인
    2. 인접한 칸이 보드 범위 내에 있고, 현재 칸과 같은 색인지 확인
    3. 조건을 만족하는 칸의 개수를 세어 반환

[풀이 과정]
    1. 상하좌우 네 방향에 대한 좌표 변화량(nx, ny)을 정의
    2. 현재 위치(h, w)의 색상을 저장
    3. 각 방향에 대해 새로운 좌표가 보드 범위 내에 있는지, 같은 색상인지 확인
    4. 조건을 만족하는 칸의 개수를 카운트하여 반환
"""

def solution(board, h, w):
    answer = 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    color = board[h][w]

    for i in range(4):
        nx, ny = dx[i] + h, dy[i] + w

        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == color:
            answer += 1

    return answer
