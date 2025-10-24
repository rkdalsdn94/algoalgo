# 백준 - 브론즈1 - 마술사 이민혁 - 3023 - 구현, 문자열 문제
'''
구현, 문자열 문제

[핵심 아이디어]
    1. 왼쪽 위 1/4 부분을 좌우 대칭시켜 위쪽 절반을 만든다
    2. 위쪽 절반을 상하 대칭시켜 전체 카드를 완성한다
    3. 주어진 에러 위치의 문자를 반전시킨다 ('#' → '.', '.' → '#')

[풀이 과정]
    1. 왼쪽 위 1/4 부분(R x C)을 입력받는다
    2. 각 행을 좌우 반전시켜 붙여 위쪽 절반(R x 2C)을 생성한다
       - 예: "#." → "#..#" (원본 + 역순)
    3. 위쪽 절반을 상하 반전시켜 아래 붙여 전체 카드(2R x 2C)를 생성한다
    4. 에러 위치(A, B)의 문자를 반전시킨다
       - 인덱스는 0-based이므로 (A-1, B-1)로 변환
    5. 완성된 카드를 출력한다

in
    2 2
    #.
    .#
    3 3
out
    #..#
    .##.
    .#..
    #..#

in
    3 3
    ###
    ###
    ###
    1 4
out
    ###.##
    ######
    ######
    ######
    ######
    ######

in
    5 4
    #.#.
    #.##
    #.##
    ....
    .#.#
    10 5
out
    #.#..#.#
    #.####.#
    #.####.#
    ........
    .#.##.#.
    .#.##.#.
    ........
    #.####.#
    #.####.#
    #.#.##.#
'''

R, C = map(int, input().split())
quarter = []
for _ in range(R):
    quarter.append(input().strip())

A, B = map(int, input().split())

# 1단계: 좌우 대칭으로 위쪽 절반 만들기
top_half = []
for row in quarter:
    # 원래 행 + 좌우 반전된 행
    full_row = row + row[::-1]
    top_half.append(full_row)

# 2단계: 상하 대칭으로 전체 카드 만들기
full_card = top_half + top_half[::-1]

# 3단계: 에러 적용 (1-indexed를 0-indexed로 변환)
error_row = A - 1
error_col = B - 1

# 해당 위치의 문자를 반전
row_list = list(full_card[error_row])
if row_list[error_col] == '#':
    row_list[error_col] = '.'
else:
    row_list[error_col] = '#'
full_card[error_row] = ''.join(row_list)

for row in full_card:
    print(row)
