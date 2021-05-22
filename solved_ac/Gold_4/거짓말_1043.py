'''
in
    4 3
    0
    2 1 2
    1 3
    3 2 3 4
out
    3
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
true = list(map(int, input().split()))[1:]
ck = [0] * n

for i in true:
    ck[i-1] = 1

parties = []
for _ in range(m):
    parties.append(list(map(int, input().split()))[1:])

res = [0] * m
while true:
    true_guest = true.pop()

    candidate = set()

    for i in range(len(parties)):
        party = set(parties[i])
        if true_guest in party:
            candidate = candidate.union(party)
            res[i] = 1

    for i in candidate:
        if not ck[i-1]:
            true.append(i)
            ck[i - 1] = 1
    
print(res.count(0))