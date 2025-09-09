# 프로그래머스 - Lv2 - 혼자서 하는 틱택토 - 구현, 시뮬레이션 문제
"""
구현, 시뮬레이션 문제

[핵심 아이디어]
    틱택토 게임의 규칙적 특성을 이용한 유효성 검증
    - 게임 진행 순서(선공 O, 후공 X)
    - 승리 조건과 게임 종료 규칙
    - 각 상황에서의 말 개수 제약 조건

[풀이 과정]
    1. O와 X의 개수를 세어 기본 조건 확인 (O >= X, O <= X+1)
    2. 가로/세로/대각선으로 승리 조건 확인
    3. 승리 상황에 따른 세부 유효성 검증:
       - 둘 다 승리: 불가능 (동시 승리 불가)
       - O만 승리: O개수 = X개수 + 1 (O 차례에 게임 종료)
       - X만 승리: O개수 = X개수 (X 차례에 게임 종료)
       - 둘 다 승리 안함: O개수 = X개수 또는 O개수 = X개수 + 1
"""

def solution(board):
    # 1단계: O와 X 개수 계산
    board_str = ''.join(board)
    o_count = board_str.count('O')
    x_count = board_str.count('X')

    # 기본 개수 조건 확인
    if o_count < x_count or o_count > x_count + 1:
        return 0

    # 2단계: 승리 조건 확인
    o_win = check_win(board, 'O')
    x_win = check_win(board, 'X')

    # 3단계: 승리 상황별 유효성 검증
    if o_win and x_win:
        return 0
    elif o_win:
        return 1 if o_count == x_count + 1 else 0
    elif x_win:
        return 1 if o_count == x_count else 0
    else:
        return 1

def check_win(board, player):
    # 가로 체크
    for row in board:
        if all(cell == player for cell in row):
            return True

    # 세로 체크
    for col in zip(*board):
        if all(cell == player for cell in col):
            return True

    # 대각선 체크 (좌상 → 우하)
    if all(board[i][i] == player for i in range(3)):
        return True

    # 대각선 체크 (우상 → 좌하)
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

print(solution(["O.X", ".O.", "..X"]))  # 1
print(solution(["OOO", "...", "XXX"]))  # 0
print(solution(["...", ".X.", "..."]))  # 0
print(solution(["...", "...", "..."]))  # 1
