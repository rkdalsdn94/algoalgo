'''
    in                  |  out
    3                   |
    10010111            |  NO
    011000100110001     |  NO
    0110001011001       |  YES
'''

import re
from sys import stdin

input = stdin.readline
t = int(input())

for _ in range(t):
    word = input().strip()
    pattern = re.compile('(100+1+|01)+')
    match = pattern.fullmatch(word)

    if match:
        print('YES')
    else:
        print('NO')
