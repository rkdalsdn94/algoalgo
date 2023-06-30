# 백준 - 실버1 - 데스 나이트 - 16948 - 그래프, bfs 문제
'''
그래프, bfs 문제

문제 분류를 먼저 봐서 그런지 쉽게 풀렸다. (다음부턴 분류를 안보고 풀어봐야지 분류를 보면 힌트처럼 적용되는 느낌)
bfs 방식으로 풀었고, start_x, start_y를 시작 위치로 end_x, end_y에 도착할 때 몇 번 q를 돌았는지 확인하면 된다.
나이트의 이동범위는 문제에 나와있다. 해당 값으로 dx, dy를 설정한 후 bfs를 실행하면 된다.

bfs는 start_x, start_y 와 몇 번 방문했는지 확인하기 위해 0으로 초기화한 후 q에 담는다.
q가 빌 때까지 while 반복을 실행한다.
    q의 값들을 꺼낸 후 꺼낸 값이 도착 위치이면 q에 담겨진 마지막 값인 c를 출력하고 exit() 함수를 이용해 종료 시킨다.
    도착 위치가 아니라면 나이트의 이동경로인 q에서 꺼낸 값들 중 a와 b 값에다가 dx, dy를 더한다.
    더해진 nx, ny 값이 g 에 방문하지 않았고, g 내에서 벗어나지 않는다면 q에 담는다.
    이 과정을 q가 빌때까지 반복하면 된다.
bfs 함수를 실행해도 종료되지 않는다면 end_x, end_y 에 도착하지 못하므로 -1을 출력하면 된다.
'''

from collections import deque

n = int(input())
start_x, start_y, end_x, end_y = map(int, input().split())

# 테스트
# from collections import deque
# n = 7
# start_x, start_y, end_x, end_y = 6, 6, 0, 1 # 4
# n = 6
# start_x, start_y, end_x, end_y = 5, 1, 0, 5 # -1
# n = 7
# start_x, start_y, end_x, end_y = 0, 3, 4, 3 # 2

g = [ [0] * n for _ in range(n) ]
dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]
g[start_x][start_y] = 1

def bfs(x, y):
    q = deque([(x, y, 0)])

    while q:
        a, b, c = q.popleft()

        if (a, b) == (end_x, end_y):
            print(c)
            exit(0)

        for i in range(6):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 0:
                q.append([nx, ny, c + 1])
                g[nx][ny] = 1

bfs(start_x, start_y)
print(-1)
