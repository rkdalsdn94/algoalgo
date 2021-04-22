'''
in
    5
    OOXXOXXOOO
    OOXXOOXXOO
    OXOXOXOXOXOXOX
    OOOOOOOOOO
    OOOOXOOOOXOOOOX
out
    10
    9
    7
    55
    30
'''

t = int(input())

for i in range(t):
    word = list(input())
    res = 0
    temp = 0
    for j in word:
        if j == 'O':
            temp += 1
            res += temp
        else:
            temp = 0
    print(res)
