# 프로그래머스 - Lv2 - 프렌즈4블록 - 구현, 시뮬레이션 문제
"""
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 2×2 형태의 같은 블록을 찾아 표시한 후 한꺼번에 제거
    2. 블록이 제거된 후 중력에 의해 블록들이 아래로 떨어짐
    3. 더 이상 제거할 블록이 없을 때까지 위 과정을 반복

[풀이 과정]
    1. 문자열로 된 board를 2차원 리스트로 변환
    2. 반복 작업 수행:
       a. 2×2 형태로 같은 블록이 모인 위치를 찾아 표시(to_remove 배열 사용)
       b. 표시된 블록들을 제거(빈 문자열로 변경)하고 제거된 블록 수 카운트
       c. 제거된 블록 위의 블록들을 아래로 떨어뜨림
       d. 더 이상 제거할 블록이 없으면 반복 종료
    3. 총 제거된 블록 수 반환
"""
def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    while True:
        removed_count = process_blocks(board, m, n)
        if removed_count == 0:
            break
        answer += removed_count

    return answer

def process_blocks(board, m, n):
    removed_count = 0
    # 삭제할 블록 찾기
    to_remove = [[0] * n for _ in range(m)]

    for i in range(m - 1):
        for j in range(n - 1):
            block = board[i][j]
            if block != '' and board[i + 1][j] == block and board[i][j + 1] == block and board[i + 1][j + 1] == block:
                to_remove[i][j] = 1
                to_remove[i + 1][j] = 1
                to_remove[i][j + 1] = 1
                to_remove[i + 1][j + 1] = 1

    # 표시된 블록 제거 및 카운트
    for i in range(m):
        for j in range(n):
            if to_remove[i][j] == 1:
                board[i][j] = ''
                removed_count += 1

    # 밑으로 떨어뜨리기
    for col in range(n):
        empty_spaces = 0
        for row in range(m - 1, -1, -1):
            if board[row][col] == '':
                empty_spaces += 1
            elif empty_spaces > 0:
                board[row + empty_spaces][col] = board[row][col]
                board[row][col] = ''

    return removed_count

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15
