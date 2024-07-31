# 백준 - 실버4 - 네모네모 시력검사 - 18242 - 구현, 에드 훅 문제
'''
구현, 에드 훅 문제

풀이 과정
    1. 입력을 받는다.
    2. '#'의 위치를 찾아서, 가장 작은 행과 열, 가장 큰 행과 열을 찾는다.
    3. 가장 작은 행과 열, 가장 큰 행과 열을 이용해서 UP, DOWN, LEFT, RIGHT를 판단한다.
    4. UP, DOWN, LEFT, RIGHT를 출력한다.
'''

n, m = map(int, input().split())
board = [input() for _ in range(n)]

# 테스트
# n, m = 7, 8
# board = [
#     '........', '........', '..#####.',
#     '..#...#.', '..#.....', '..#...#.',
#     '..#####.'
# ] # RIGHT
# n, m = 7, 8
# board = [
#     '#######.', '#.....#.', '#.....#.',
#     '#.....#.', '#.....#.', '#.....#.',
#     '###.###.'
# ] # DOWN
# n, m = 5, 5
# board = [
#     '#####', '#...#', '....#',
#     '#...#', '#####',
# ] # LEFT
# n, m = 8, 10
# board = [
#     '..........', '..........', '...##.##..',
#     '...#...#..', '...#...#..', '...#...#..',
#     '...#####..', '..........'
# ] # UP

min_row, min_col = 200, 200
max_row, max_col = -1, -1

for i in range(n):
    for j in range(m):
        if board[i][j] == '#':
            min_row, min_col = min(min_row, i), min(min_col, j)
            max_row, max_col = max(max_row, i), max(max_col, j)

if board[min_row][(min_col + max_col) // 2] == '.':
    print('UP')
elif board[max_row][(min_col + max_col) // 2] == '.':
    print('DOWN')
elif board[(min_row + max_row) // 2][min_col] == '.':
    print('LEFT')
else:
    print('RIGHT')
