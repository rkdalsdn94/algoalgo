# 백준 - 실버5 - 지뢰 찾기 - 1996 - 구현 문제
'''
구현 문제

다음의 조건만 신경쓰면 되는 문제이다.
 - 지뢰가 있는 칸은 '*'로 표시
 - 지뢰가 없는 칸은 인접한 지뢰의 개수로 표시
 - 지뢰가 없는 칸은 인접한 지뢰의 개수가 10개 이상이면 'M'으로 표시

풀이 과정
    1. 8방향 탐색을 통해 지뢰가 있는지 확인
    2. 지뢰가 있는 경우 '*'로 표시
    3. 지뢰가 없는 경우 인접한 지뢰의 개수를 더해줌
    4. 인접한 지뢰의 개수가 10개 이상인 경우 'M'으로 표시
    5. 결과 출력
'''

n = int(input())
board = [list(input()) for _ in range(n)]

# 테스트
# n = 5
# board = [
#     list('1....'),
#     list('..3..'),
#     list('.....'),
#     list('.4...'),
#     list('...9.')
# ]
# '''
# out
#     *4330
#     14*30
#     47730
#     4*M99
#     44M*9
# '''

dx, dy = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, -1, 1, 1] # 상하좌우 대각선
res = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] != '.':
            res[i][j] = '*'
            continue

        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny].isdigit():
                res[i][j] += int(board[nx][ny])

                if res[i][j] >= 10:
                    res[i][j] = 'M'
                    break

for i in range(n):
    print(*res[i], sep='')
