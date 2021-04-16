'''
in
    1000 70 170
    3 2 1
out
    11
    -1
'''

a, b, c = map(int, input().split())

if c - b <= 0:
    print(-1)
else:
    print(a // (c - b) + 1)