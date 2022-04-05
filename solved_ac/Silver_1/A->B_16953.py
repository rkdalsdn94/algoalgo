'''
bfs 문제

입력을 q에 넣어둔 후,
2를 곱했을 때, 1을 추가 했을 때, 각 경우를 q에다 넣은 후에
b의 값이랑 같아 졌을 때 res를 바꾸고 반환한다.

x가 b를 넘을 때 까지 x가 b와 같지 않으면, 해당 값은 안되는 경우라서 -1를 반환하려고,
res의 기본 값은 -1로 설정했다.
'''

from collections import deque

a, b = map(int, input().split())

# # 테스트
# a, b = 2, 162 # 5
# a, b = 4, 42 # -1
# a, b = 100, 40021 # 5

res = -1
q = deque([(a, 1)])

while q:
    x, y = q.popleft()

    if x == b:
        res = y
        break

    if x * 2 <= b:
        q.append((x * 2, y + 1))
    
    if int(str(x) + '1') <= b:
        q.append((int(str(x) + '1'), y + 1))

print(res)
