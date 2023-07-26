# 백준 - 실버1 - 배열 돌리기 1 - 16926 - 구현 문제
'''
구현 문제

외부 회전과 내부 회전은 따로 생각해야 된다.
시간 초과를 피하기 위해 외부 배열과, 내부 배열 따로 돌려야 된다. 이 부분을 처음 for 문을 생각하면 된다. (n이랑 m 값 중 더 작은 값의 // 2)
배열을 일차원으로 만든 후 r 만큼 앞 부분을 자르고, 뒤에 잘 붙힌 다음 그 값으로 board 값을 수정하면 된다.

난이도가 상당히 있었다.
https://www.youtube.com/watch?v=RNZAxC6clv8 여기 영상에서 도움을 많이 얻었다.
풀이의 감을 잡았는데 어떻게 구현해야 할 지 난감할 때 참고하면 좋을거 같다.

다른 사람의 풀이를 보면 deque 를 써서 rotate 함수를 적용한거도 봤는데 이 방법도 좋은 방법인거 같다.
'''

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n, m, r = 4, 4, 2
# board = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# '''
# out
#     3 4 8 12
#     2 11 10 16
#     1 7 6 15
#     5 9 13 14
# '''
# n, m, r = 4, 4, 2
# board = [
#     [1, 2, 3, 4],
#     [7, 8, 9, 10],
#     [13, 14, 15, 16],
#     [19, 20, 21, 22],
#     [25, 26, 27, 28]
# ]
# '''
# out
#     28 27 26 25
#     22 9 15 19
#     16 8 21 13
#     10 14 20 7
#     4 3 2 1
# '''

def get_chain(k, n, m, A):
    C = [0] * (n + m - 2) * 2
    i, j, t = k, k, 0

    for _ in range(n - 1):
        C[t] = board[i][j]
        i += 1; t += 1
    for _ in range(m - 1):
        C[t] = board[i][j]
        j += 1; t += 1
    for _ in range(n - 1):
        C[t] = board[i][j]
        i -= 1; t += 1
    for _ in range(m - 1):
        C[t] = board[i][j]
        j -= 1; t += 1

    return C

def put_chain(C, k, n, m, board):
    i, j, t = k, k, 0
    for _ in range(n - 1):
        board[i][j] = C[t]
        i += 1; t += 1
    for _ in range(m - 1):
        board[i][j] = C[t]
        j += 1; t += 1
    for _ in range(n - 1):
        board[i][j] = C[t]
        i -= 1; t += 1
    for _ in range(m - 1):
        board[i][j] = C[t]
        j -= 1; t += 1

def rotate(i, n, m, r, board):
    chain = get_chain(i, n, m, board)
    pos = len(chain) - (r % len(chain))
    rotated = chain[pos:] + chain[:pos]
    put_chain(rotated, i, n, m, board)

for i in range(min(n, m) // 2):
    rotate(i, n - 2 * i, m - 2 * i, r, board)

for i in board:
    print(*i)
