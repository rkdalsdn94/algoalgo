# 백준 - 실버2 - 미로 만들기 - 1347 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

정답으로 출력할 배열을 미리 만들어 놓고, 이동하는 방향에 따라 '.' 으로 바꿔 나가는 방식으로 문제를 풀었다.
범위도 크지 않고, 최대 입력의 값도 크지 않아 충분히 통과할 수 있다.

풀이 과정
    1. 입력 받기
    2. 정답으로 출력할 res 배열을 101 * 101 크기로 '#'으로 초기화한다.
    3. 현재 위치를 (50, 50)으로 초기화하고, 이동 방향을 설정한다.
    4. 이동 방향에 따라 이동하면서 '.'으로 바꿔 나간다.
        4.1. 이때 시작과 끝 위치를 찾아야 한다.
    5. 시작 위치와 끝 위치를 찾아 출력한다.
'''

n = int(input())
command = input()

# 테스트
# n = 5
# command = 'RRRFRF'
# '''
#     ..
#     .#
# '''
# n = 6
# command = 'LFFRFF'
# '''
#     ...
#     ##.
#     ##.
# '''
# n = 14
# command = 'LFLFRRFLFRRFLF'
# '''
#     #.#
#     ...
#     #.#
# '''
# n = 19
# command = 'FLFRFFRFFFRFFRFLFLLF'
# '''
#     #..#
#     ....
#     .##.
#     ....
# '''
# n = 31
# command = 'FRFFFFFFLLFRFFFFFLLFRFFFFLFFLFF'
# '''
#     ######.
#     .......
#     #.#####
#     #.#...#
#     #.###.#
#     #.....#
#     #.#####
# '''

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, direction = 50, 50, 1
start_x, start_y, end_x, end_y = 50, 50, 50, 50

res = [['#'] * 101 for _ in range(101)]
res[x][y] = '.'

for i in command:
    if i == 'L':
        direction = (direction + 3) % 4
    elif i == 'R':
        direction = (direction + 1) % 4
    elif i == 'F':
        x = x + dx[direction]
        y = y + dy[direction]
        res[x][y] = '.'
        start_x, start_y, end_x, end_y = min(start_x, x), min(start_y, y), max(end_x, x), max(end_y, y)

for i in range(start_x, end_x + 1):
    print(''.join(res[i][start_y : end_y + 1]))
