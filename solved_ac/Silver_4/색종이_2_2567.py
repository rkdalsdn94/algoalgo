# 백준 - 실버4 - 색종이 2 - 2567 - 구현 문제
'''
색종이 2

기존 색종이 문제(백준 2563번)에서 상하좌우를 검사하는 방식만 추가하면 된다.
검정 블록의 둘레를 처리해야 된다.
    단, 모서리 부분은 + 2를 해야 한다. (가로줄, 세로줄 모두 포함하기 때문)
    주변의 1이 3개라면 둘레의 포함되므로 + 1을 하면 된다.
'''

n = int(input())
n_list = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# n = 4
# n_list = [ [3, 7], [5, 2], [15, 7], [13, 14] ] # 96

board = [ [0] * 101 for _ in range(101) ]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
res = 0

for i in n_list:
    a, b = i

    for j in range(a, a + 10):
        for k in range(b, b + 10):
            board[j][k] = 1

for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            temp = 0

            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if 0 <= nx < 102 and 0 <= ny < 102 and board[nx][ny] == 1:
                    temp += 1
            if temp == 2: # 모서리 체크
                res += 2
            elif temp == 3: # 길이 체크
                res += 1

print(res)
