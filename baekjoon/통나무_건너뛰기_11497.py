# 백준 통나무 건너뛰기 - 11497
'''
input
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6
out
1
4
0
'''
t = int(input())
for _ in range(t):
    n = int(input())
    log = sorted(list(map(int, input().split())))

    res = 0
    for i in range(2, n):
        res = max(res, log[i] - log[i - 2])

    print(res)