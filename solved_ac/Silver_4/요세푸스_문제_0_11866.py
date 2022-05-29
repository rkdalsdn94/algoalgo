'''
구현, 큐 문제

문제를 구현해야 될 부분을 쪼개면 이렇게 할 수 있다
1. 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, q = deque([i for i in range(1, n + 1)])
   양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. while문 안에 K - 1에서 q다시 append하는 과정
2. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. q가 없어질 때까지 반복하는 과정

위에 과정을 다 진행한 후에 마지막 출력을 위해서(<x, x1, x2, ..., xn> 이런식으로 되어 있는거) answer를 사용했다.
'''

from collections import deque

n, k = map(int, input().split())

# 테스트
n, k = 7, 3 # <3, 6, 2, 7, 5, 1, 4>

q = deque([i for i in range(1, n + 1)])
res = []
answer = '<'

while q:
    for i in range(k - 1):
        q.append(q.popleft())
    
    res.append(q.popleft())

for i in res:
    answer += str(i) + ', '

print(answer[:-2] + '>')
