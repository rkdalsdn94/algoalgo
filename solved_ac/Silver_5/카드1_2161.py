'''
구현, 자료 구조, 큐 문제

큐를 사용해서 문제에 나와있는 방식대로 구하면 된다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다.
 - 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다.
 - 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다.
 - 마지막으로 2를 버리고 나면, 버린 카드들은 순서대로 1 3 2가 되고, 남는 카드는 4가 된다.
'''

from collections import deque

n = int(input())

# 테스트
# n = 7 # 1 3 5 7 4 2 6

q = deque([ i for i in range(1, n + 1) ])
res = []

for _ in range(n - 1):
    res.append(q.popleft())
    q.append(q.popleft())
res.append(q.popleft())

print(*res)
