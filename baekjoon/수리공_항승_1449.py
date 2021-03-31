# n, l = 4, 2
# n_list = sorted([1, 2, 100, 101]) # 2
n, l = map(int, input().split())
n_list = sorted(list(map(int, input().split())))

res = 1
temp = n_list[0] + (l - 1)

for i in range(1, n):
    if n_list[i] <= temp:
        continue
    res += 1
    temp = n_list[i] + (l - 1)
print(res)

