# 백준 - 실버2 - 숫자판 점프 - 2210 - 그래프, 완전 탐색, dfs 문제
'''
그래프, 완전 탐색, dfs 문제

단순한 dfs를 돌리면 되는 문제이다. 중복되는 값들을 제거하기 위해 set 자료 구조를 활용했다.
dfs를 돌린 후 set에 추가한 뒤, set의 길이를 출력하면 된다.
'''

board = [ input().split() for _ in range(5) ]

# 테스트
# board = [
#     ['1', '1', '1', '1', '1'],
#     ['1', '1', '1', '1', '1'],
#     ['1', '1', '1', '1', '1'],
#     ['1', '1', '1', '2', '1'],
#     ['1', '1', '1', '1', '1']
# ] # 15

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
res = set()

def dfs(x, y, num_str):
    if len(num_str) == 6:
        res.add(num_str)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num_str + board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(res))
