'''
pypy3로 제줄해야 된다.
python3으로 하면 시간초과.. (dfs로 풀면 괜찮으려나..?)
'''
from collections import deque, defaultdict

def bfs(x):
    global temp
    temp = 1
    ck = [0 for _ in range(n+1)]
    ck[x] = 1
    q = deque([x])

    while q:
        a = q.popleft()

        for i in dic[a]:
            if ck[i] == 0:
                q.append(i)
                ck[i] = 1
                temp += 1

    return temp

def solution():
    global cnt, temp
    answer = []

    for i in range(1, n+1):
        temp = bfs(i)

        if temp >= cnt:
            cnt = temp
            answer.append([i, cnt])

    for i, j in answer:
        if j == cnt:
            print(i, end=' ')

n, m = map(int, input().split())
dic = defaultdict(list)
cnt, temp = 0, 0

for _ in range(m):
    a, b = map(int, input().split())
    dic[b].append(a)

# 테스트
# n, m = 5, 4
# dic = defaultdict(list)
# dic[1].append(3)
# dic[2].append(3)
# dic[3].append(4)
# dic[3].append(5)
# cnt, temp = 0, 0

solution()
