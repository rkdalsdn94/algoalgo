# 백준 - 실버2 - 점프 점프 - 14248 - 그래프, bfs 문제
'''
그래프, bfs 문제

기본적인 bfs 문제이다.
스타트 지점을(s) 를 q에 넣어준 뒤 해당 위치에서 앞과 뒤로 점프를 이동하기 위해 해당 인덱스의 -와 +의 값을 nx로 둔 뒤
범위를 벗어나지 않고, 방문하지 않는 돌 다리라면 q에 넣어준 뒤 방문했다는 체크를 한다.

최종적으로 몇 번 방문했는지 ck변수에서 1의 숫자를 출력하면 되는 문제이다.
'''

from collections import deque

n = int(input())
n_list = list(map(int, input().split()))
s = int(input())

# 테스트
# n = 5
# n_list = [1, 4, 2, 2, 1]
# s = 3  # 5

ck = [0] * n
ck[s - 1] = 1
q = deque([(s - 1)])

while q:
    a = q.popleft()

    for i in [-n_list[a], n_list[a]]:
        nx = a + i

        if 0 <= nx < n and ck[nx] == 0:
            q.append(nx)
            ck[nx] = 1

print(ck.count(1))
