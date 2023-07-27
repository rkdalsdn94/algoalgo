# 백준 - 골드4 - 숨바꼭질 2 - 12851 - 그래프, bfs 문제
'''
그래프, bfs 문제

while 문 부분을 함수로 만들면 다른 bfs 문제들이랑 똑같다. 근데, 다른 조건들이(dx, dy 이런 조건들) 따로 없어 보여서 함수로 안 만들었다.
기존에 백준 문제 중 '숨바꼭질 3(1697)'과 '숨바꼭질 1(13549)'을 섞어서 푸는데, 두 코드를 잘 섞으면 된다.

q 에 n 을 담은 후 값을 꺼내면서 아래의 과정을 문제의 요구사항인 100_001 범위를 벗어나지 않은 한 반복한다.
    1. * 2, + 1, - 1 의 값들이 최대 범위를 벗어나지 않고,
    2. 전의 방문했던 값에서 + 1한 상태이거나 또는 방문하지 않은 곳이라면 q에 담아준다.

위 1. 2. 두 과정을 반복하면서 q에서 꺼낸 값이 k랑 같아지면 res를 더해준다.
ck 의 k 위치와, res 를 출력하면 되는 문제이다.

https://pythontutor.com/visualize.html#mode=edit 여기에서 코드를 돌려보려고 하면
주어진 예제로는 ck 와 while 문 안의 if 문의 범위를 100 으로 줄인 후 돌려보면 이해할 수 있다.
'''

from collections import deque

n, k = map(int, input().split())

# 테스트
# n, k = 5, 17  # 4  \  2

ck, res = [-1] * 100_001, 0
ck[n] = 0
q = deque([n])

while q:
    a = q.popleft()

    if a == k:
        res += 1
        continue

    for nx in (a * 2, a + 1, a - 1):
        if 0 <= nx < 100_001 and (ck[nx] == ck[a] + 1 or ck[nx] == -1):
            ck[nx] = ck[a] + 1
            q.append(nx)

print(ck[k])
print(res)
