# 백준 - 실버1 - 돌다리 - 12761 - 그래프, bfs 문제
'''
그래프, bfs 문제

18% 에서 틀린다면 res나 ck나 범위를 다시 설정해야 한다.
    - 처음 문제를 풀 때 res와 ck 배열을 m + 1 크기로 잡고 했다가 index 에러가 나왔다.
    - 각각 배열을 문제 입력의 최대 범위인 100_001로 잡으면 문제 없이 통과한다.

기본적인 bfs 문제이다.
이동할 수 있는 범위를 dx로 두고, 곱하기로 이동할 수도 있으므로 multiply_dx를 따로 만들어 준다.
bfs 를 시작할 때 -1로 초기화한 res 배열에서 현재 위치를 0으로 바꾼다.
그 후 n이 있는 위치부터 +1, -1, -a, -b, +a, +b, *a, *b 의 bfs를 실행한다.
범위를 벗어나지 않거나, ck에 방문하지 않은 곳이면 q에 담고 계속 검사한다.
q에 nx를 새로 담을 때 q에서 꺼낸 값을 1을 더하고 꺼내고, 마지막 해당 위치를 출력한다.
'''

from collections import deque

a, b, n, m = map(int, input().split())

# 테스트
# a, b, n, m = 2, 3, 1, 20 # 4
# a, b, n, m = 3, 7, 2, 98500 # 10

res = [-1] * 100_001
ck = [0] * 100_001
dx = [1, -1, -a, -b, a, b]
multiply_dx = [a, b]
q = deque([(n)])
ck[n] = 1
res[n] = 0

while q:
    x = q.popleft()

    for i in dx:
        nx = x + i

        if 0 <= nx < 100_001 and ck[nx] == 0:
            res[nx] = res[x] + 1
            q.append(nx)
            ck[nx] = 1

    for i in dx:
        nx = x * i

        if 0 <= nx < 100_001 and ck[nx] == 0:
            res[nx] = res[x] + 1
            q.append(nx)
            ck[nx] = 1

print(res[m])
