'''
input
    2
    5
    50 10 100 20 40
    30 50 70 10 60
    7
    10 30 10 50 100 20 40
    20 40 30 50 60 20 80
out
    260
    290

dp 문제이다.

for i in range(1, n) 부분에서
처음만 대각선으로 값을 더해주고, (if i == 1)
그 다음부턴 max로 값을 비교하면서(대각선 or 전 전 대각선을 더했을 경우에서 큰 값)
더 큰 값을 list에 더해주면서 최종적으로 가장 큰 값을 출력하면 된다.
'''

T = int(input())

for _ in range(T):
    n = int(input())
    sticker_list = [ list(map(int, input().split())) for _ in range(2) ]

    for i in range(1, n):
        if i == 1:
            sticker_list[0][i] += sticker_list[1][i - 1]
            sticker_list[1][i] += sticker_list[0][i - 1]
        else:
            sticker_list[0][i] += max(sticker_list[1][i - 1], sticker_list[1][i - 2])
            sticker_list[1][i] += max(sticker_list[0][i - 1], sticker_list[0][i - 2])

    print(max(sticker_list[0][n - 1], sticker_list[1][n - 1]))
