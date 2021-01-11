# from collections import deque

# n, m = map(int, input().split())
# factory = [[] for _ in range(n + 1)]


# def bfs(x):
#     q = deque([start_node])
#     ck = [False] * (n+1)
#     ck[start_node] = True
#     while q:
#         temp = q.popleft()
#         for y, z in factory[temp]:
#             if not ck[y] and z >= x:
#                 ck[y] = True
#                 q.append(y)
#     return ck[end_node]


# start, end = 100000000, 1

# for _ in range(m):
#     x, y, w = map(int, input().split())
#     factory[x].append((y, w))
#     factory[y].append((x, w))
#     start = min(start, w)
#     end = max(end, w)
# start_node, end_node = map(int, input().split())
# res = 0
# while(start <= end):
#     mid = (start + end) // 2
#     if bfs(mid):
#         res = mid
#         start = mid + 1
#     else:
#         end = mid - 1
# print(res)

# 위에 주석한 것도 되는데 시간 좀 더 줄일려고 반복문으로 했는데 그래도 pypy로 제출해야 통과할 수 있음..
from collections import deque

n, m = map(int, input().split())
factory = [[] for _ in range(n + 1)]

start, end = 100000000, 1

for _ in range(m):
    x, y, w = map(int, input().split())
    factory[x].append((y, w))
    factory[y].append((x, w))
    start = min(start, w)
    end = max(end, w)
start_node, end_node = map(int, input().split())
res = 0
while(start <= end):
    mid = (start + end) // 2
    q = deque([start_node])
    ck = [False] * (n+1)
    ck[start_node] = True
    while q:
        temp = q.popleft()
        for y, z in factory[temp]:
            if not ck[y] and z >= mid:
                ck[y] = True
                q.append(y)
    if ck[end_node]:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)
