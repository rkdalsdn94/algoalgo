# n, m = map(int, input().split())
n, m = 4, 4
'''
in : 4, 4
out :
    1 2 3 4
    1 2 4 3
    1 3 2 4
    1 3 4 2
    1 4 2 3
    1 4 3 2
    2 1 3 4
    2 1 4 3
    2 3 1 4
    2 3 4 1
    2 4 1 3
    2 4 3 1
    3 1 2 4
    3 1 4 2
    3 2 1 4
    3 2 4 1
    3 4 1 2
    3 4 2 1
    4 1 2 3
    4 1 3 2
    4 2 1 3
    4 2 3 1
    4 3 1 2
    4 3 2 1
'''
num_seq = []

def dfs():
    if len(num_seq) == m:
        print(' '.join(map(str, num_seq)))
        return
    
    for i in range(1, n+1):
        if i not in num_seq:
            num_seq.append(i)
            dfs()
            num_seq.pop()

dfs()
