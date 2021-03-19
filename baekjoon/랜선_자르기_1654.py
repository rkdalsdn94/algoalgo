'''
input
    4 11
    802
    743
    457
    539
out
    200
'''
k, n = map(int, input().split())
n_list = [int(input()) for _ in range(k)]
s, res = 1, max(n_list)

while s <= res:
    m = (s + res) // 2
    temp = 0

    for i in n_list:
        temp += i // m
    
    if temp >= n:
        s = m + 1
    else:
        res = m - 1
print(res)