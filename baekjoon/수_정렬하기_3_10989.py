'''
in
    10
    5
    2
    3
    1
    4
    2
    3
    5
    1
    7
out
    1
    1
    2
    2
    3
    3
    4
    5
    5
    7
'''
import sys
input = sys.stdin.readline
n = int(input())
n_list = [0] * 10001

for _ in range(n):
    n_list[int(input())] += 1

for i in range(len(n_list)):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)
