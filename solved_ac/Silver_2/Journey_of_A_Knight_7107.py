# 백준 - 실버2 - Journey of A Knight - 7107 - 그래프, bfs 문제
'''
그래프, bfs 문제

[문제 해석]
- 나이트가 이동할 수 있는 8가지 방향으로 이동하여 목표 지점에 도달하는 최소 이동 횟수를 구하는 문제

[문제 접근]
- 나이트가 이동할 수 있는 8가지 방향을 정의한다.
- 시작 위치에서 목표 지점까지 BFS를 수행한다.
- 목표 지점에 도달하면 이동 횟수를 반환한다.

[해결 방법]
1. 나이트가 이동할 수 있는 8가지 방향을 정의한다.
2. 시작 위치는 (1,1)이다.
3. 방문 여부를 저장할 2차원 배열을 생성한다.
4. BFS를 위한 큐를 생성한다.
5. 큐에 시작 위치와 이동 횟수를 저장한다.
6. 큐가 빌 때까지 반복한다.
    6.1. 큐에서 위치 i, 위치 j, 이동 횟수를 꺼낸다.
    6.2. 목표 지점에 도달하면 이동 횟수를 반환한다.
    6.3. 가능한 모든 이동을 시도한다.
    6.4. 방문하지 않은 위치라면 큐에 추가한다.
7. 목표 지점에 도달할 수 없는 경우 "NEVAR"를 반환한다.
8. 결과를 출력한다.
'''

from collections import deque

def knight_moves(n, m, target_i, target_j):
    # 나이트가 이동할 수 있는 8가지 방향
    moves = [
        (-2, -1), (-2, 1),  # 위로 2칸, 좌/우로 1칸
        (2, -1), (2, 1),    # 아래로 2칸, 좌/우로 1칸
        (-1, -2), (1, -2),  # 좌로 2칸, 위/아래로 1칸
        (-1, 2), (1, 2)     # 우로 2칸, 위/아래로 1칸
    ]

    # 시작 위치는 (1,1)
    start_i, start_j = 1, 1

    # 방문 여부를 저장할 2차원 배열
    visited = [[False] * (m + 1) for _ in range(n + 1)]

    # BFS를 위한 큐: (위치 i, 위치 j, 이동 횟수)
    queue = deque([(start_i, start_j, 0)])
    visited[start_i][start_j] = True

    while queue:
        current_i, current_j, moves_count = queue.popleft()

        # 목표 지점에 도달했다면 이동 횟수 반환
        if current_i == target_i and current_j == target_j:
            return moves_count

        # 가능한 모든 이동 시도
        for move_i, move_j in moves:
            next_i = current_i + move_i
            next_j = current_j + move_j

            # 보드 범위 내에 있고 아직 방문하지 않은 위치라면
            if (1 <= next_i <= n and
                    1 <= next_j <= m and
                    not visited[next_i][next_j]):

                visited[next_i][next_j] = True
                queue.append((next_i, next_j, moves_count + 1))

    # 목표 지점에 도달할 수 없는 경우
    return "NEVAR"

n, m, i, j = map(int, input().split())

# 테스트
# n, m, i, j = 5, 3, 1, 2 # 3
# n, m, i, j = 100, 2, 2, 2 # NEVAR

result = knight_moves(n, m, i, j)
print(result)
