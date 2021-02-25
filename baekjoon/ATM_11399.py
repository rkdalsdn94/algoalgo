n = 5
n_list = [3, 1, 4, 3, 2] # 32
# n = int(input())
# n_list = list(map(int, input().split()))
n_list.sort()
for i in range(1, len(n_list)):
    n_list[i] = n_list[i] + n_list[i-1]
print(sum(n_list))

