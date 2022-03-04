'''
완전탐색 문제이다.
문제 조건중  "8x8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다."
저 부분을 잘 생각해야 된다. n, m의 범위가 8 <= n, m <= 50 이므로 최소 8이상의 board가 만들어지므로
i, j를 사용하는 for문은 8로 자를려고 -7을 했고, 그 다음 a, b 를 사용하는 for문은 + 8을 통해 board의 크기를 수정한 값으로 반복한다.
그 아래 조건문은 B가 나오면 W, W가 나오면 B가 나오는지 검사한 후 맞게 나오는 경우에만 한 쪽 값이 커지게 된다 (홀수로 들어왔을 때 반대로 처리해줌)
다 한 후에 min값을 반환
8 * 8 board로 어떻게 자를지만 해결하면 문제는 금방 풀린다.

아래 예제중 n과 m이 10, 10 들어온 경우를 생각해보면
i, j가 1, 1 일때 8 * 8 크기로 생각해보면 borad[1][1]부터 borad[8][8]을 보면 BWBW~~ 순으로 올바르게 되어 있다
해당 상황에서 cnt1값만 커지게 되므로 0을 반환한다. 해당 예제를 잘 구현하면 어려움 없이 풀 수 있을거 같다.
'''
# n, m = map(int, input().split())
# board = [ input() for _ in range(n) ]
# print(n, m, board)

''' 테스트
n, m, board = 8, 8, ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBBBWBW',
                    'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW'] # 1
n, m = 10, 13
board = ['BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW',
        'BBBBBBBBBWBWB', 'BBBBBBBBWBWBW', 'BBBBBBBBBWBWB', 'WWWWWWWWWWBWB', 'WWWWWWWWWWBWB'] # 12
n, m, board = 8, 8, ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB',
                    'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB'] # 0
n, m = 9, 23
board = ['BBBBBBBBBBBBBBBBBBBBBBB', 'BBBBBBBBBBBBBBBBBBBBBBB', 'BBBBBBBBBBBBBBBBBBBBBBB',
        'BBBBBBBBBBBBBBBBBBBBBBB', 'BBBBBBBBBBBBBBBBBBBBBBB', 'BBBBBBBBBBBBBBBBBBBBBBB',
        'BBBBBBBBBBBBBBBBBBBBBBB', 'BBBBBBBBBBBBBBBBBBBBBBB', 'BBBBBBBBBBBBBBBBBBBBBBW'] # 31
n, m = 10, 10
board = ['BBBBBBBBBB', 'BBWBWBWBWB', 'BWBWBWBWBB', 'BBWBWBWBWB', 'BWBWBWBWBB',
        'BBWBWBWBWB', 'BWBWBWBWBB', 'BBWBWBWBWB', 'BWBWBWBWBB', 'BBBBBBBBBB'] # 0
n, m, board = 8, 8, ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBBBWBW',
                    'WBWBWBWB', 'BWBWBWBW', 'WBWBWWWB', 'BWBWBWBW'] # 2
n, m = 11, 12
board = ['BWWBWWBWWBWW', 'BWWBWBBWWBWW', 'WBWWBWBBWWBW', 'BWWBWBBWWBWW', 'WBWWBWBBWWBW',
        'BWWBWBBWWBWW', 'WBWWBWBBWWBW', 'BWWBWBWWWBWW', 'WBWWBWBBWWBW', 'BWWBWBBWWBWW', 'WBWWBWBBWWBW'] # 15
'''
n, m = 10, 10
board = ['BBBBBBBBBB', 'BBWBWBWBWB', 'BWBWBWBWBB', 'BBWBWBWBWB', 'BWBWBWBWBB',
        'BBWBWBWBWB', 'BWBWBWBWBB', 'BBWBWBWBWB', 'BWBWBWBWBB', 'BBBBBBBBBB'] # 0

res = []

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        cnt1 += 1
                    elif board[a][b] != 'B':
                        cnt2 += 1
                else:
                    if board[a][b] != 'W':
                        cnt2 += 1
                    elif board[a][b] != 'B':
                        cnt1 += 1

        res.append(min(cnt1, cnt2))

print(min(res))
