n = int(input())
n_list = sorted([int(input()) for _ in range(n)], reverse=True)
# n = 2
# n_list = [10, 15] # 20

res = 0
for i in range(n):
    temp = n_list[i] * (i+1)
    
    if temp > res:
        res = temp
print(res)
