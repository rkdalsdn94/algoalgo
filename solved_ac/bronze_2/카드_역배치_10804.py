# 백준 - 브론즈2 - 카드 역배치 - 10804 - 구현, 시뮬레이션 문제
'''
구현, 시뮬레이션 문제

list 슬라이싱을 이용해 배열을 구간으로 나눈 후 잘 합치면 되는 문제이다.
특정 알고리즘을 적용하고 푸는 문제가 아니라 구현 문제이다.

아래 링크에서 1 ~ 20 의 배열을 갖고 시도하다보면 감이 온다. 
https://pythontutor.com/visualize.html#mode=edit
'''

command = [ list(map(int, input().split())) for _ in range(10) ]

# 테스트
# command = [
#     [5, 10], [9, 13], [1, 2], [3, 4], [5, 6],
#     [1, 2], [3, 4], [5, 6], [1, 20], [1, 20]
# ] # 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

board = [ i for i in range(1, 21) ]

for i in command:
    a, b = i
    board = board[:a - 1] + board[a - 1:b][::-1] + board[b:]

print(*board)
