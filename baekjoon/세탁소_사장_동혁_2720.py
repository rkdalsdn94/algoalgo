coin_list = [25, 10, 5, 1]

# t = 3
# t_list = [124,25,194] 
'''
out
4 2 0 4
1 0 0 0
7 1 1 4
'''
# for j in t_list:
#     n = j
#     res = []
#     for i in coin_list:
#        temp = n // i
#        n %= i
#        res.append(temp)
#     print(res)
t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    for i in coin_list:
        temp = n//i
        n %= i
        res.append(temp)
    print(*res)