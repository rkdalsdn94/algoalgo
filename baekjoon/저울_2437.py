# 저울 - 2437

n = 7
n_list = sorted([3, 1, 6, 2, 7, 30, 1])
# n = int(input())
# n_list = sorted(list(map(int, input().split())))
res = 1
for i in n_list:
    if res < i:
        break
    res += i

print(res)