# 백준 주식 - 11501
'''
input
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2

out
0
10
5
'''

t = int(input())

for _ in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    temp = n_list[-1]
    res = 0
    for i in range(len(n_list)-2, -1, -1):
        if temp > n_list[i]:
            res += temp - n_list[i]
        else:
            temp = n_list[i]
    
    print(res)
