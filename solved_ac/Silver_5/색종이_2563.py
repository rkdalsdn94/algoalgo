# 백준 - 실버5 - 색종이 - 2563 - 구현 문제
'''
구현 문제

문제만 잘 이해하면 쉽게 구현할 수 있다.

문제의 내용은 아래와 같다.
'가로, 세로의 크기가 각각 100' 인 정사각형 모양의 흰색 도화지가 있다.
  ㄴ> [101][101] 크기의 board
이 도화지 위에 '가로, 세로의 크기가 각각 10인 정사각형 모양'
  ㄴ> n_list에 입력받은 x, y 의 10을 더한 크기만큼 1로 바꾼다.
색종이가 붙은 검은 영역의 넓이
  ㄴ> board에서 1인 부분의 전체 합
'''

n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 3
# n_list = [[3,7], [15, 7], [5, 2]] # 260

board = [ [0 for _ in range(101)] for _ in range(101) ]
res = 0

for x, y in n_list:
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

for i in board:
    res += sum(i)

print(res)
