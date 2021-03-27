# n = 3
# k = 7 # 6
n = int(input())
k = int(input())

s, e = 0, k
res = 0

while s <= e:
    mid = (s + e) // 2
    temp = 0

    for i in range(1, n+1):
        temp += min(mid//i, n)
    
    if temp < k:
        s = mid + 1
    else:
        res = mid
        e = mid - 1

print(res)
