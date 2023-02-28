# 백준 - 실버1 - 컴백홈 - 1189 - 그래프, 완전 탐색, dfs, 백 트래킹 문제
'''
그래프, 완전 탐색, dfs, 백 트래킹 문제

문제 분류엔 백 트래킹이 있는데 사실 기본적인 dfs로 풀 수 있다.
시작을 r - 1과 0으로 시작한 후 방문한 곳을 'T'로 바꾸면서 풀면 된다.
보통 dfs, bfs를 풀 때 ck를 활용 하는데 이 문제에선 'T'로 충분히 확인 가능할 수 있을거 있어서 (오히려 ck를 쓰면 메모리 낭비될거 같아서)
board의 값을 바꿔가면서 조건을 비교했다.
'''

r, c, k = map(int, input().split())
board = [ list(input()) for _ in range(r) ]

# 테스트
# r, c, k = 3, 4, 6
# board = [ list('....'), list('.T..'), list('....') ] # 4

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
board[r - 1][0] = 'T'
res = 0

def dfs(x, y, cnt):
    global res

    if cnt != k:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'T':
                board[nx][ny] = 'T'
                dfs(nx, ny, cnt + 1)
                board[nx][ny] = '.'
    elif cnt == k and x == 0 and y == c - 1:
        res += 1

dfs(r - 1, 0, 1)

print(res)
