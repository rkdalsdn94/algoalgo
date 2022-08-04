'''
단순 구현 문제

Pypy3 로 제출해야 된다. -> 미리 입력을 받은 후에 res를 구해서 그런거 같다.
i, j, x, y의 범위에서 res변수에 더하면 된다.

in
    2 3
    1 2 4
    8 16 32
    3
    1 1 2 3
    1 2 1 2
    1 3 2 3
out
    63
    2
    36
'''

import sys; input = sys.stdin.readline

n, m = map(int, input().split())
list_1 = [ list(map(int, input().split())) for _ in range(n) ]
list_2 = [ list(map(int, input().split())) for _ in range(int(input())) ]

for i, j, x, y in list_2:
    res = 0
    
    for a in range(i, x + 1):
        for b in range(j, y + 1):
            res += list_1[a - 1][b - 1]
    
    print(res)