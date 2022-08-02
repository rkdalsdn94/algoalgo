'''
단순 구현 문제

그림의 크디는 100x100 이라고 한다. 해당 board를 만든 후에
x1, y1, x2, y2 를 입력 받고, 해당 크기만큼 board에서 +1을 한다.
마지막 board가 m보다 클 경우만 res에 더한 다음에
res를 출력하면 된다.
'''

n, m = map(int, input().split())
board = [ [0] * 100 for _ in range(100) ]
res = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i-1][j-1] += 1

for i in range(100):
    for j in range(100):
        if board[i-1][j-1] > m:
            res += 1

print(res)
