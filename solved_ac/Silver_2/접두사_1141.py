'''
in
    6
    hello
    hi
    h
    run
    rerun
    running
out
    4
'''
from sys import stdin
input = stdin.readline

n = int(input())
n_list = sorted([ input().strip() for _ in range(n) ], key=len)
res = 0

for i in range(n):
    temp = n_list[i]
    ck = True

    for j in range(i+1, n):
        try:
            if n_list[j].index(temp) == 0:
                ck = False
                break
        except:
            continue
    
    if ck:
        res += 1
    
print(res)