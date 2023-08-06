# 프로그래머스 - Lv2 - 무인도 여행 - bfs, dfs 문제
'''
bfs 문제

단순한 bfs 방식으로 풀었다.
maps의 길이만큼 반복하면서 'X'가 아닐경우에 bfs를 실행한다.
bfs에서 while 문을 반복하는 조건은 다음과 같다.
방문하지 않은 곳이고, maps의 범위를 벗어나지 않고, 이동할 maps의 위치가 'X'가 아닐 경우 temp에 수를 더해준다.

bfs 함수로 만들어서 문제를 풀려고 했는데, 스코프 문제로 에러가 발생했다. 그래서 그냥 bfs 함수를 쭉 나열했다.
요즘 계속 백문 문제를 풀다 보니, 입력 파라미터들의 스코프를 global로 생각해서 그런 거 같은데,
문제를 다 풀고 다른 사람 풀이를 보니 solution 함수 안에서 bfs든 dfs든 정의한다. 다음에 프로그래머스 문제를 풀 때 신경 써야겠다.
'''

from collections import deque

def solution(maps):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    answer = []
    ck = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and ck[i][j] == 0:
                q = deque([(i, j)])
                temp = 0
                ck[i][j] = 1

                while q:
                    a, b = q.popleft()
                    temp += int(maps[a][b])

                    for k in range(4):
                        nx, ny = a + dx[k], b + dy[k]

                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and ck[nx][ny] == 0:
                            q.append((nx, ny))
                            ck[nx][ny] = 1
                answer.append(temp)

    return sorted(answer) if answer else [-1]

print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))  # [1, 1, 27]
print(solution(["XXX", "XXX", "XXX"])) # [-1]
