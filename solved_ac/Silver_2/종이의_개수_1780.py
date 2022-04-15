'''
재귀 문제

재귀로 풀었다. 시간도 많이 쏟고, 구현해보려고 여러가지 시도 했는데,
문제가 잘 풀리지 않아 다른 사람들이 푼 아이디어를 참고했다.
(예전에 프로그래머스에서도 쿼드압축 후 개수 세기 라는 문제도 풀려다 실패 했는데, 다시 도전 해봐야겠다.)

아이디어는 단순하다.
해당 문제는 3으로만 나눈 값을 생각하면 돼서, 3으로 나눈후 영역을 123, 456, 789 각 영역을 계산하면 된다.
각 영역은 코드 제출한거 같이 n을 3으로 나눈 값으로 * 2 를 하고 안하고 조합으로 생각하면 된다.
'''

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]
# print(n, board)

# 테스트
# n = 9 # 10 \n 12 \n 11
# board = [[0, 0, 0, 1, 1, 1, -1, -1, -1], [0, 0, 0, 1, 1, 1, -1, -1, -1],
#          [0, 0, 0, 1, 1, 1, -1, -1, -1], [1, 1, 1, 0, 0, 0, 0, 0, 0],
#          [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0],
#          [0, 1, -1, 0, 1, -1, 0, 1, -1], [0, -1, 1, 1, 0, -1, 0, 1, -1], [0, 1, -1, 0, 1, -1, 0, 1, -1]]

negative_num, zero_num, positive_num = 0, 0, 0

def dfs(x, y, n):
    global negative_num, zero_num, positive_num
    temp = board[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != temp:
                new_n = n // 3

                # 123
                dfs(x, y, new_n)
                dfs(x, y + new_n, new_n)
                dfs(x, y + new_n * 2, new_n)

                # 456
                dfs(x + new_n, y, new_n)
                dfs(x + new_n, y + new_n, new_n)
                dfs(x + new_n, y + new_n * 2, new_n)

                # 789
                dfs(x + new_n * 2, y, new_n)
                dfs(x + new_n * 2, y + new_n, new_n)
                dfs(x + new_n * 2, y + new_n * 2, new_n)
                return

    if temp == -1: negative_num += 1
    elif temp == 0: zero_num += 1
    elif temp == 1: positive_num += 1

dfs(0, 0, n)

print(negative_num, zero_num, positive_num, sep='\n')
