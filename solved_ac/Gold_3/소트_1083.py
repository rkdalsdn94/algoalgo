'''
in
    7
    10 20 30 40 50 60 70
    1
out
    20 10 30 40 50 60 70
'''
from sys import stdin
input = stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
s = int(input())

for i in range(n - 1):
    if s == 0:
        break

    temp, idx = n_list[i], i
    for j in range(i + 1, min(n, i + 1 + s)):
        if temp < n_list[j]:
            temp = n_list[j]
            idx = j

    s -= idx - i
    for j in range(idx, i, -1):
        n_list[j] = n_list[j-1]

    n_list[i] = temp

print(*n_list)
