# 백준 - 실버2 - 결혼식 - 5567 - 그래프, bfs 문제
'''
그래프, bfs 문제


핵심 : ck를 이용해서 2 ~ 3 범위 안에 있는 숫자들은 나의 친구와 나의 친구의 친구라서 결혼식에 참성할 수 있는 범위이다.

풀이 과정
1. board에 input값을 a, b 각각 넣어준다. 그리고 출력할 때 사용할 ck를 n + 1 크기로 초기화 시킨다.
2. bfs를 자기 자신부터 시작한다.
    2.1 q에 자기 자신을 넣고, board의 해당 번째 값을을 꺼내면서 방문했는지 확인해본다. (ck를 확인하기)
    2.2 방문을 안했던 곳이라면 q에 값을 넣고, ck 인덱스의 + 1한 값으로 바꿔준다.
    2.3 q가 빌 때까지 반복한다.
3. ck의 2 ~ 3까지가 내 친구와 내 친구의 친구 이므로 두 숫자의 count를 더해서 출력하면 된다.

in
    6
    5
    1 2
    1 3
    3 4
    2 3
    4 5
out
    3

in
    6
    5
    2 3
    3 4
    4 5
    5 6
    2 5
out
    0
'''

from collections import deque

n, m = int(input()), int(input())
board = [ [] for _ in range(n + 1) ]
ck = [ 0 for _ in range(n + 1) ]

for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

def bfs(x):
    q = deque([x])
    cnt = 0
    ck[x] = 1

    while q:
        a = q.popleft()
        cnt += 1

        for i in board[a]:
            if not ck[i]:
                ck[i] = ck[a] + 1
                q.append(i)
    
    return ck.count(2) + ck.count(3)

print(bfs(1))
