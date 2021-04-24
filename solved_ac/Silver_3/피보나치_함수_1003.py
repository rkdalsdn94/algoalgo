'''
in
    3
    0
    1
    3
out
    1 0
    0 1
    1 2
'''

t = int(input())

zero, one = [1, 0, 1], [0, 1, 1]

for _ in range(t):
    n = int(input())
    if len(zero) <= n:
        for i in range(len(zero), n+1):
            zero.append( zero[i-1] + zero[i-2] )
            one.append( one[i-1] + one[i-2] )
    print(zero[n], one[n])