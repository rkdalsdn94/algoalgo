# n = 13
# n_list = ['but', 'i','wont','hesitate','no','more','no'
# 'more','it','cannot','wait','im','yours']
'''
out
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''
n = int(input())
n_list = list(set([input() for _ in range(n)]))
res = sorted([(len(i), i) for i in n_list])
for i, j in res:
    print(j)

