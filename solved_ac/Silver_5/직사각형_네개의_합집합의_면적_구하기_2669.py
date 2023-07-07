# 백준 - 실버5 - 직사각형 네개의 합집합의 면적 구하기 - 2669 - 구현 문제
'''
구현 문제

단순 구현 문제이다.
입력으로 들어오는 4 개의 직사각형의 범위만 파악하고 해당 범위만큼 board 를 1로 만든 후
전체 board 의 1의 개수를 출력하면 된다.
'''

n_list = [ list(map(int, input().split())) for _ in range(4) ]

# 테스트
# n_list = [[1,2,4,4], [2,3,5,7], [3,1,6,5], [7,3,8,6]] # 26

board = [ [0] * 101 for _ in range(101) ]
res = 0

for i in n_list:
    a, b, c, d = i

    for j in range(a, c):
        for k in range(b, d):
            board[j][k] = 1

for i in board:
    res += i.count(1)

print(res)
