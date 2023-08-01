# 백준 - 골드4 - 미로만들기 - 2665 - 그래프, bfs 문제
'''
그래프, bfs 문제

'백준 - 골드4 - 알고스팟 (1261)' 문제와 비슷하다.

solved.ac 기준으로 문제의 분류로 데이크스트라가 있었는데 왜 있는지 이해가 잘 안 됐다.
근데, 다른 사람의 풀이를 보는데, popleft 하는 부분을 heap 으로 사요해서 푸는 방식을 보니까 데이크스트라를 활용할 수 있겠구나 라는 생각이 들었다.
 - https://kimmeh1.tistory.com/545 데이크스트라로 푼 다른 사람 풀이 (문제 접근 방식은 비슷)

그래프(이하 g) 에서 상, 하, 좌, 우로 이동할 곳이 g의 범위를 벗어나지 않고, 방문하지 않은 위치일 때
 - 이동할 값이 흰 방(이하 '1') 이면 이전의 값을 그대로 사용하고,
 - 검은 방(이하 '0') 이면 이 전의 값에서 1을 더해서 방을 바꿔야야 된다.
위 과정을 반복한 후 최종 a와 b가 n - 1 의 위치에 도착했을 때 res 의 값을 추가하면 된다.

처음에는 ck를 정답에 출력으로 사용했는데, 위의 글을 읽고 ck는 방문 체크만 하는 역할을 갖게하고, 정답을 출력하기 위해 res 를 사용했다.
'''

import sys; input=sys.stdin.readline
from collections import deque

n = int(input())
g = [list(input()) for _ in range(n)]

# 테스트
# from collections import deque
# n = 8
# g = [
#     list('11100110'), list('11010010'), list('10011010'), list('11101100'),
#     list('01000111'), list('00110001'), list('11011000'), list('11000111')
# ] # 2

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(x, y):
    ck = [[0] * n for _ in range(n)]
    q = deque([(x, y, 0)])
    ck[x][y] = 0

    while q:
        a, b, res = q.popleft()

        if a == n - 1 and b == n - 1:
            print(res)
            exit(0)

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and ck[nx][ny] == 0:
                if g[nx][ny] == '1':
                    q.appendleft([nx, ny, res])
                else:
                    q.append([nx, ny, res + 1])
                ck[nx][ny] = 1

bfs(0, 0)
