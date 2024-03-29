# 백준 - 브론즈3 - 최댓값 - 2566 - 단순 구현 문제
'''
단순 구현 문제

board 의 크기가 9 * 9 밖에 되지 않는다.
해당 보드에서 가장 큰 값과 해당 인덱스를 반환하면 된다.
전체 크기가 작아 그리디하게 전체를 반복하면서 큰 값과 위치를 담아놓고 출력하면 된다.

아.. x, y 를 0으로 초기화 해놓고 제출했다가 '틀렸습니다.'를 받고 당황했다.
0, 0이 제일 큰 값일 수 있으므로 x, y는 1, 1로 초기화해야 한다.
'''

board = [ list(map(int, input().split())) for _ in range(9) ]

# 테스트
# board = [
#     [3, 23, 85, 34, 17, 74, 25, 52, 65],
#     [10, 7, 39, 42, 88, 52, 14, 72, 63],
#     [87, 42, 18, 78, 53, 45, 18, 84, 53],
#     [34, 28, 64, 85, 12, 16, 75, 36, 55],
#     [21, 77, 45, 35, 28, 75, 90, 76, 1],
#     [25, 87, 65, 15, 28, 11, 37, 28, 74],
#     [65, 27, 75, 41, 7, 89, 78, 64, 39],
#     [47, 47, 70, 45, 23, 65, 3, 41, 44],
#     [87, 13, 82, 38, 31, 12, 29, 29, 80]
# ]

res, x, y = 0, 1, 1

for i in range(9):
    for j in range(9):
        if res < board[i][j]:
            res = board[i][j]
            x, y = i + 1, j + 1

print(res)
print(x, y)
