# 백준 - 실버1 - 음식물 피하기 - 1743 - 그래프(bfs) 문제
'''
그래프 문제이다. bfs로 문제를 해결했다.

풀이 과정
1. board를 만든다.
  - board를 만들 때 임력되는 음식물의 값을 그대로 사용하고 싶어 1씩 크게 만들었다.
2. 음식물을 입력받고, board에서 음식물의 위치를 3으로 바꾼다.
3. board를 0,0 부터 n + 1, r + 1 까지 반복한다.
  - 반복하는 중간에 음식물을 만나면 bfs를 실행하게 되고, bfs에서 상하좌우로 음식물이 있으면 해당 크기를 재는 cnt를 리턴한다.
4. return되는 값을 max함수로 비교하면서 최종 결과인 res를 출력하면 된다.
'''

from collections import deque

n, r, k = map(int, input().split())
k_list = [ list(map(int, input().split())) for _ in range(k) ]

# 테스트
# n, r, k = 3, 4, 5
# k_list = [[3,2],[2,2],[3,1],[2,3],[1,1]] # 4

ck = [ [0] * (r + 1) for _ in range(n + 1) ]
board = [ [0] * (r + 1) for _ in range(n + 1) ]
res = 0

def bfs(i, j):
    q = deque([(i, j)])
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    cnt = 0

    while q:
        a, b = q.popleft()
        ck[a][b] = 1
        cnt += 1

        for i, j in zip(dx, dy):
            nx, ny = a + i, b + j

            if 0 <= nx < n + 1 and 0 <= ny < r + 1 and ck[nx][ny] == 0 and board[nx][ny] == 3:
                q.append([nx, ny])
                ck[nx][ny] = 1
    
    return cnt

for i, j in k_list:
    board[i][j] = 3

for i in range(n + 1):
    for j in range(r + 1):
        if board[i][j] == 3:
            res = max(bfs(i, j), res)
        else:
            ck[i][j] = 1

print(res)