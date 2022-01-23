from collections import deque

n = int(input())
n_list = list(map(int, input().split()))
a, b = map(int, input().split())
a, b = a - 1, b - 1
ck = [-1] * n
# 테스트
# n = 5
# n_list = [1, 2, 2, 1, 2]
# a, b = 1, 5 # 1
# a, b = a - 1, b - 1
# ck = [-1] * n

def bfs(n, a, b, n_list):
    q = deque([a])
    ck[a] = 0

    while q:
        x = q.popleft()

        for i in range(n):
            if (i - x) % n_list[x] == 0 and ck[i] == -1:
                q.append(i)
                ck[i] = ck[x] + 1

                if i == b:
                    return ck[i]
    return -1

print(bfs(n, a, b, n_list))