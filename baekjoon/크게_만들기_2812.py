# 크게 만들기 - 2812
n, k = map(int, input().split())
num = list(input())
# n, k = 4, 2
# num = list('1924') # 94
res, temp = [], k
for i in range(n):
    while temp > 0 and res and res[-1] < num[i]:
        del res[-1]
        temp -= 1
    res.append(num[i])
print(''.join(res[:n - k]))
