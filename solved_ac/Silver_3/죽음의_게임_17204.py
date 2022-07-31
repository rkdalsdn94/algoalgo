'''
구현, 그래프, 시뮬레이션 문제

n_list를 받은 후에 0번 인덱스에서 시작하는 bfs로 구현했다.
n만큼 돌면서 0번째 인덱스에서 시작해서 해당 인덱스가 k이면 break후 출력하고,
반복문을 n번 다 돌아도 k를 못만나면 -1을 출력하면 된다.
'''

from collections import deque

n, k = map(int, input().split())
n_list = [ int(input()) for _ in range(n) ]

# 테스트
# n, k = 5, 3
# n_list = [ 1, 3, 2, 1, 4 ] # 2
# n, k = 6, 2
# n_list = [ 1, 3, 5, 4, 0, 2 ] # -1

res = 0
q = deque([0])
ck = False

for _ in range(n):
    temp = q.popleft()
    res += 1

    if n_list[temp] == k:
        ck = True
        break
    q.append(n_list[temp])

if ck:
    print(res)
else:
    print(-1)
