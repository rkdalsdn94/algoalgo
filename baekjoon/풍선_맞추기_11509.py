'''
in
    5
    2 1 5 4 3
out
    2
in
    5
    1 2 3 4 5
out
    5
in
    5
    4 5 2 1 4
out
    3
'''

n = int(input())
n_list = list(map(int, input().split()))

ck = [0] * 1000001

res = 0

for i in range(len(n_list)):
    if ck[n_list[i]] == 0:
        res += 1
        ck[n_list[i]-1] += 1
    else:
        ck[n_list[i]] -= 1
        ck[n_list[i]-1] += 1
print(res)