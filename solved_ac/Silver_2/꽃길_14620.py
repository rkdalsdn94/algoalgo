# 백준 - 실버2 - 꽃길 - 14620 - 완전 탐색 문제
'''
완전 탐색 문제

풀이 과정
 1. 입력을 받고, dx, dy를 설정한다.
    1.1. dx, dy는 문제에 주어진 대로 상 하 좌 우 그리고 현재 위치를 나타낸다.
 2. check 함수를 만들어서 꽃을 심을 수 있는지 확인한다.
    2.1. 꽃을 심을 수 있는지 확인하는 방법은 상 하 좌 우 현재 위치에 꽃이 심어져 있는지와, 범위가 벗어나는지 확인한다.
 3. 꽃을 심는다.
    3.1. 꽃을 심는 방법은 상 하 좌 우 현재 위치에 꽃(ck 리스트 변수를 1로 변경)을 심는다.
 4. 꽃을 심을 수 있으면 꽃을 심고, dfs로 탐색한다.
 6. 꽃을 심을 수 없으면 꽃을 심지 않고, dfs로 탐색한다.
 7. 꽃을 심은 개수가 3개가 되면 total을 통해 값을 구한 걸 min 함수를 통해 최솟값을 갱신한다.
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 6
# n_list = [
#     [1, 0, 2, 3, 3, 4], [1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1],
#     [3, 9, 9, 0, 1, 99], [9, 11, 3, 1, 0, 3], [12, 3, 0, 0, 0, 1]
# ] # 12

dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]
res = int(1e9)
ck = [[0] * n for _ in range(n)]

def check(x, y, ck):
    for k in range(5):
        nx, ny = x + dx[k], y + dy[k]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return False
        if ck[nx][ny]:
            return False

    return True

def dfs(x, ck, cnt, total):
    global res

    if cnt == 3:
        res = min(res, total)
        return

    for i in range(x, n - 1):
        for j in range(1, n - 1):
            if check(i, j, ck):
                for k in range(5):
                    nx, ny = i + dx[k], j + dy[k]
                    ck[nx][ny] = 1
                    total += n_list[nx][ny]

                dfs(i, ck, cnt + 1, total)

                for k in range(5):
                    nx, ny = i + dx[k], j + dy[k]
                    ck[nx][ny] = 0
                    total -= n_list[nx][ny]

dfs(1, ck, 0, 0)

print(res)
