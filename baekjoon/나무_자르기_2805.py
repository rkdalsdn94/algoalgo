# pypy3로 제출해야함 안그럼 시간초과 뜸 

# n, m = 4, 7
# n_list = [20, 15, 10, 17]  # 15
n, m = map(int, input().split())
n_list = list(map(int, input().split()))

res = 0
s, res = 1, max(n_list)

while s <= res:
    mid = (s + res) // 2

    temp = 0
    for i in n_list:
        if i >= mid:
            temp += (i - mid)
    
    if temp >= m:
        s = mid + 1
    else:
        res = mid - 1
print(res)