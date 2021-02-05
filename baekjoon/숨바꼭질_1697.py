from collections import deque

n, k = map(int, input().split())
# n, k = 5, 17 # 4
ck = [0] * 100001
cnt = 0
q = deque()

def bfs(n):
    q.append([n, cnt])

    while q:
        a, b = q.popleft()
        if ck[a] == 0:
            ck[a] = 1
            if a == k:
                return b
            b += 1
            if (a*2) <= 100000:
                q.append([a*2, b])
            if (a+1) <= 100000:
                q.append([a+1, b])
            if (a-1) >= 0:
                q.append([a-1, b])


print(bfs(n))

