from itertools import combinations
n, s = 5, 0
s_list = [-7, -3, -2, 5, 8]
# n, s = map(int, input().split())
# s_list = list(map(int, input().split()))
res = 0
for i in range(1, n+1):
    temp = list(combinations(s_list, i))
    for j in temp:
        if sum(j) == s:
            res += 1
print(res)