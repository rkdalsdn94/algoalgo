# 백준 - 실버2 - 로마 카톨릭 미사 - 9518 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

'o'인 부분, '.'인 부분 두 경우를 모두 생각해야 된다. 'o'일 때는 악수를 한 사람이 또 악수하는 경우도 들어가므로 나누기 2를 해야 된다.
'.'인 부분에선 8방향을 탐색했을 때 자리에 앉아 있는 사람이 있는지 검사하고 앉아 있는 사람이 있을 때 temp를 통해 값을 담아놓는다.
해당 temp들 중 제일 큰 값으로 자리에 앉아 있는 사람들이 악수한 경우랑 더해줘야 된다.

막상 풀이를 생각한 후에는 구현이 크게 어렵진 않지만,
풀이 과정인 두 경우로 나눠서 생각해야 된다는걸 눈치채기 전까지는 고민을 좀 했던 문제이다.
  1. 자리에 앉아 있는 사람들끼리 악수하는 경우
  2. 빈 자리에 앉았을 때 근처 앉아 있는 사람들과 악수하는 경우
위 두 경우를 더해준 후 출력해야 된다.
'''

r, s = map(int, input().split())
board = [ input() for _ in range(r) ]

# 테스트
# r, s = 2, 3
# board = [ '..o', 'o..' ] # 2
# r, s = 2, 2
# board = [ 'oo', 'oo' ] # 6

dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1] # 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
res = 0

for i in range(r): # 자리에 앉아 있는 사람들끼리 악수하는 경우
    for j in range(s):
        if board[i][j] == '.':
            continue

        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]

            if 0 <= nx < r and 0 <= ny < s and board[nx][ny] == 'o':
                res += 1
res //= 2
temp_res = 0
for i in range(r): # 빈 자리에 앉았을 때 악수하는 경우
    for j in range(s):
        if board[i][j] == 'o':
            continue

        temp = 0
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]

            if 0 <= nx < r and 0 <= ny < s and board[nx][ny] == 'o':
                temp += 1

        temp_res = max(temp_res, temp)
res += temp_res # 자리에 앉아 있는 사람들끼리 악수한 경우 + 빈 자리에 앉았을 때 추가로 악수하는 경우를 더해야 된다.
print(res)
