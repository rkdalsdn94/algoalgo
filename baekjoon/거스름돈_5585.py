n = 1000 - 380 # 4
# n = 1000 - int(input())
n_list = [500, 100, 50, 10, 5, 1]
res = 0

for i in n_list:
    res += n // i
    n %= i
    if n == 0:
        break

print(res)
