# 백준 - 실버4 - 나이트 투어 - 1331 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 유효한 나이트 투어의 조건 검사:
       - 모든 칸을 정확히 한 번씩 방문해야 함 (중복 방문 불가)
       - 인접한 두 칸 사이의 이동은 나이트의 이동 규칙을 따라야 함 (L자 형태)
       - 마지막 위치에서 시작 위치로 돌아갈 수 있어야 함
    2. 나이트의 이동 규칙:
       - 가로 2칸, 세로 1칸 이동 또는
       - 가로 1칸, 세로 2칸 이동

[풀이 과정]
    1. 36개의 위치를 입력받음
    2. 중복 위치가 있는지 확인 (집합 자료구조 활용)
    3. 인접한 두 위치 사이의 이동이 나이트의 이동 규칙을 따르는지 확인
    4. 마지막 위치에서 첫 번째 위치로의 이동이 나이트의 이동 규칙을 따르는지 확인
    5. 모든 조건을 만족하면 "Valid", 아니면 "Invalid" 출력
'''

night = [input() for _ in range(36)]

# 테스트
# night = [
#     'A1', 'B3', 'A5', 'C6', 'E5', 'F3', 'D2', 'F1',
#     'E3', 'F5', 'D4', 'B5', 'A3', 'B1', 'C3', 'A2',
#     'C1', 'E2', 'F4', 'E6', 'C5', 'A6', 'B4', 'D5',
#     'F6', 'E4', 'D6', 'C4', 'B6', 'A4', 'B2', 'D1',
#     'F2', 'D3', 'E1', 'C2'
# ] # Valid
# night = [
#     'A1', 'C2', 'E3', 'F5', 'D4', 'B3', 'A1', 'C2',
#     'E3', 'F5', 'D4', 'B3', 'A1', 'C2', 'E3', 'F5',
#     'D4', 'B3', 'A1', 'C2', 'E3', 'F5', 'D4', 'B3',
#     'A1', 'C2', 'E3', 'F5', 'D4', 'B3', 'A1', 'C2',
#     'E3', 'F5', 'D4', 'B3',
# ] # Invalid
# night = [
#     'D4', 'F5', 'D6', 'B5', 'A3', 'B1', 'D2', 'F1',
#     'E3', 'D1', 'F2', 'E4', 'F6', 'D5', 'B6', 'A4',
#     'B2', 'C4', 'A5', 'C6', 'E5', 'F3', 'E1', 'C2',
#     'A1', 'B3', 'C5', 'E6', 'F4', 'E2', 'C3', 'A2',
#     'C1', 'D3', 'B4', 'A6',
# ] # Invalid
# night = [
#     'C5', 'D3', 'F2', 'D1', 'B2', 'A4', 'B6', 'D5', 'C3',
#     'E4', 'F6', 'B3', 'A1', 'C2', 'E1', 'F3', 'E5', 'C6', 'A5',
#     'C4', 'A3', 'B1', 'D2', 'F1', 'E3', 'F5', 'D6', 'B5', 'D4', 'E6',
#     'F4', 'E2', 'C1', 'A2', 'B4', 'A6'
# ] # Invalid

# 중복 방문 검사를 위한 집합
visited = set()

def is_valid_knight_move(prev, curr):
    """
    두 위치 사이의 이동이 나이트의 이동 규칙을 따르는지 확인

    prev: 이전 위치 (예: 'A1')
    curr: 현재 위치 (예: 'B3')
    return: 유효한 나이트 이동이면 True, 아니면 False
    """
    # 열(column) 차이 계산 (A, B, C, ... -> 0, 1, 2, ...)
    col_diff = abs(ord(prev[0]) - ord(curr[0]))

    # 행(row) 차이 계산 (1, 2, 3, ... -> 1, 2, 3, ...)
    row_diff = abs(int(prev[1]) - int(curr[1]))

    # 나이트 이동 규칙 검사: (2, 1) 또는 (1, 2) 패턴
    return (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)

is_valid = True

# 1. 중복 방문 검사
for pos in night:
    if pos in visited:
        is_valid = False
        break
    visited.add(pos)

# 2. 나이트 이동 규칙 검사 (인접한 위치 사이)
if is_valid:
    for i in range(1, 36):
        if not is_valid_knight_move(night[i-1], night[i]):
            is_valid = False
            break

# 3. 마지막 위치에서 첫 번째 위치로의 이동 검사
if is_valid:
    if not is_valid_knight_move(night[35], night[0]):
        is_valid = False

print("Valid" if is_valid else "Invalid")
