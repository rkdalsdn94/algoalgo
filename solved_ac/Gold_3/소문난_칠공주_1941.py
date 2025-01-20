# 백준 - 골드3 - 소문난 칠공주 - 1941 - 백 트래킹, 완전 탐색, 그래프, bfs, dfs 문제
'''
백 트래킹, 완전 탐색, 그래프, bfs, dfs 문제

핵심 아이디어
    - 25명 중 7명을 뽑아야 하므로 백 트래킹을 사용한다.
    - 7명을 뽑은 후 인접('S', 'Y'에 대한 체크)한지 체크한다.
    - 인접하다면 + 1을 한다.

풀이 과정
    1. 25명 중 7명을 뽑는다.
        1.1. 백 트래킹을 사용한다.
    2. 인접한지 체크한다.
        2.1. bfs를 통해 인접한지 체크한다.
    3. 결과 출력
'''

from collections import deque

def bfs(i, j):
    q = deque([(i, j)])
    visited = [[0] * 5 for _ in range(5)]
    visited[i][j] = 1
    cnt = 1
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        a, b = q.popleft()

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < 5 and 0 <= ny < 5 and v[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    return cnt == 7

def check():
    for i in range(5):
        for j in range(5):
            if v[i][j]:
                return bfs(i, j)

def dfs(n, cnt, scnt):
    global res

    if cnt > 7: # 7명 초과 이면 7공주를 만들 수 없음
        return

    if n == 25:
        if cnt == 7 and scnt >= 4:  # 7명이 그룹이고, 4명 이상이 다솜파인 경우
            if check():             # 인접 했는지 체크 (인접하다면 + 1)
                res += 1
        return

    v[n // 5][n % 5] = 1  # 포함하는 경우
    dfs(n + 1, cnt + 1, scnt + int(arr[n // 5][n % 5] == 'S'))
    v[n // 5][n % 5] = 0  # 원상 복구
    dfs(n + 1, cnt, scnt) # 포함하지 않는 경우

arr = [input() for _ in range(5)]

# 테스트
# arr = ['YYYYY', 'SYSYS', 'YYYYY', 'YSYYS', 'YYYYY'] # 2

res = 0
v = [[0] * 5 for _ in range(5)]  # 방문 체크
dfs(0, 0, 0)  # 학생 번호(0 ~ 24), 포함 학생 수, 다솜파 학생 수
print(res)
