# 프로그래머스 - 교점에 별 만들기 - 87377 - 구현, 수학 문제
"""
구현, 수학 문제

[핵심 아이디어]
    1. 모든 직선 쌍에 대해 교점을 계산합니다.
    2. 교점이 정수 좌표인 경우에만 리스트에 추가합니다.
    3. 모든 교점의 최소 및 최대 x, y 좌표를 찾아 격자판의 크기를 결정합니다.
    4. 격자판을 초기화하고, 교점 위치에 '*'를 표시합니다.
    5. 격자판을 문자열 리스트로 변환하여 반환합니다.

[풀이 과정]
    1. 이중 루프를 사용하여 모든 직선 쌍을 선택합니다.
    2. 각 직선 쌍에 대해 교점 좌표를 계산합니다.
        - 교점 공식: x = (B*F - E*D) / (A*D - B*C), y = (E*C - A*F) / (A*D - B*C)
        - 분모가 0이면 평행하거나 일치하는 직선이므로 무시합니다.
        - 분자가 분모로 나누어 떨어지는지 확인하여 정수 좌표인지 판단합니다.
    3. 모든 교점 좌표를 리스트에 저장합니다.
    4. 교점 좌표의 최소 및 최대 x, y 값을 찾아 격자판의 크기를 계산합니다.
    5. 격자판을 '.'로 초기화하고, 교점 좌표에 해당하는 위치에 '*'를 표시합니다.
    6. 격자판을 문자열 리스트로 변환하여 반환합니다.
"""

def solution(line):
    # 모든 정수 교점 찾기
    points = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]

            denominator = A * D - B * C
            if denominator == 0:
                continue

            x_num, y_num = B * F - E * D, E * C - A * F

            if x_num % denominator == 0 and y_num % denominator == 0:
                points.append((x_num // denominator, y_num // denominator))

    # 경계 찾기
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    # 격자판 생성
    height, width = max_y - min_y + 1, max_x - min_x + 1
    grid = [['.' for _ in range(width)] for _ in range(height)]

    # 별 표시
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'

    return [''.join(row) for row in grid]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]) == ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"])
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]) == ["*.*"])
print(solution([[1, -1, 0], [2, -1, 0]]) == ["*"])
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]) == ["*"])
