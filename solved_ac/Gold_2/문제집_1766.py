'''
위상 정렬 문제이다.
위상 정렬이 뭔지 잘 모른다면 https://blog.naver.com/ndb796/221236874984 여기 나동빈님 블로그를 참고하면 된다. (동빈님 감사합니다)
해당 링크에선 cpp로 되어 있는데, 읽는 거에 있어서 큰 어려움은 없다.
heapq를 사용하지 않고 mind으로 해도 정답은 나오는데, 시간 초과가 나와 heapq를 사용했다.
'''

import heapq as hq

n, priority_problem = map(int, input().split())
priority_problem_list = [ [] for _ in range(n + 1) ]
ck = [0] * (n + 1)

for _ in range(priority_problem):
    a, b = map(int, input().split())
    priority_problem_list[a].append(b)
    ck[b] += 1
# print(priority_problem_list, ck)

# 테스트
# n, priority_problem = 4, 2
# priority_problem_list = [[], [], [], [1], [2]] # 3 1 4 2
# ck = [0, 1, 1, 0, 0]

q, res = [], []

for i in range(1, n + 1):
    if ck[i] == 0:
        hq.heappush(q, i)

while q:
    temp = hq.heappop(q)
    res.append(temp)

    for i in priority_problem_list[temp]:
        ck[i] -= 1

        if ck[i] == 0:
            hq.heappush(q, i)

print(*res)

