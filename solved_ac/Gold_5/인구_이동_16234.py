# 백준 - 골드5 - 인구 이동 - 16234 - 그래프, 시뮬레이션, bfs 문제
'''
그래프, 시뮬레이션, bfs 문제

https://www.youtube.com/watch?v=8OMCUH50CHA 이 영상을 통해 구조를 잡는데 도움을 얻었다.
구현은 크게 어렵지 않지만, 제일 바깥의 루프를 어떻게 잡아야 할 지 고민이 됐는데, 위의 영상을 통해 힌트를 얻을 수 있었다. (근데 결국 문제를 잘 안 읽어서 그런듯..)
    - 문제의 조건중 '최대 2000 번의 인구 이동'이 나온다는걸 영상을 통해 확인할 수 있었다.

구현 방식은 bfs를 통해 구현하는 것이다. 지금까지 bfs 푸는 방식과 동일하게
    - 그래프(g)의 범위를 벗어나는지,
    - ck를 통해 방문 여부를 검사하는거,
    - 이 문제의 핵심인 인구 이동을 할 수 있는지 (l <= abs(g[a][b] - g[nx][ny]) <= r)
위의 조건들을 다 통과할 수 있으면 방문 표시와 q에 담고 인구 이동 했을 때 평균 인구로 바꿔주기 위해 average_population 라는 변수를 만들어서 활용했다.
연합 국가들을 union_country 라는 이름으로 리스트로 만든 후 전체 인구의 합에서 연합 국가의 길이만큼 나눈 몫으로 그래프를 수정했다.

연합 국가가 없으면 0을 return 하고, 있으면 1을 return 해서 while 문을 도중에 빠져나올수 있도록 만들었다.

여기 코드들이 이해가 잘 안갈경우 https://pythontutor.com/render.html#mode=display 여기 링크에서 한 스텝씩 넘겨보거나, 제일 위의 영상을 보면 이해하는데 도움이 된다.
'''

from collections import deque
import sys; input=sys.stdin.readline

n, l, r = map(int, input().split())
g = [ list(map(int, input().split())) for _ in range(n) ]

# 테스트
# from collections import deque
# n, l, r = 2, 20, 50
# g = [ [50, 30], [20, 40] ] # 1
# n, l, r = 2, 40, 50
# g = [ [50, 30], [20, 40] ] # 0
# n, l, r = 2, 20, 50
# g = [ [50, 30], [30, 40] ] # 1
# n, l, r = 3, 5, 10
# g = [ [10, 15, 20], [20, 30, 25], [40, 22, 10] ] # 2
# n, l, r = 4, 10, 50
# g = [ [10, 100, 20, 90], [80, 100, 60, 70], [70, 20, 30, 40], [50, 20, 100, 10] ] # 3

res = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(a, b):
    q = deque([(a, b)])
    ck[a][b] = 1
    union_country = [(a, b)]
    average_population = g[a][b]

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]

            if 0 <= nx < n and 0 <= ny < n and ck[nx][ny] == 0 and l <= abs(g[a][b] - g[nx][ny]) <= r:
                q.append([nx, ny])
                ck[nx][ny] = 1
                union_country.append([nx, ny])
                average_population += g[nx][ny]

    for i, j in union_country:
        g[i][j] = average_population // len(union_country)

    if len(union_country) > 1:
        return 1
    return 0

while res <= 2000:
    ck = [ [0] * n for _ in range(n) ]
    flag = 0

    for i in range(n):
        for j in range(n):
            if ck[i][j] == 0:
                flag = max(flag, bfs(i, j))
    if flag == 0:
        break
    res += 1

print(res)
