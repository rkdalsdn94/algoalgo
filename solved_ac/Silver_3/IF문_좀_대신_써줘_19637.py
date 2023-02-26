# 백준 - 실버3 - IF문 좀 대신 써줘 - 19637 - 이분 탐색 문제
'''
이분 탐색 문제

이분 탐색으로 문제를 풀면 된다.
sys.stdin.readline 이 없으면 시간 초과가 난다.
다른 사람 코드를 보니 bisect를 사용하면 엄청 간단하게 풀린다. (bisect 공부해야겠다...)
제일 아래 주석으로 해당 코드를 붙여놓고 bisect를 공부좀 해야겠다.

in
    3 8
    WEAK 10000
    NORMAL 100000
    STRONG 1000000
    0
    9999
    10000
    10001
    50000
    100000
    500000
    1000000
out
    WEAK
    WEAK
    WEAK
    NORMAL
    NORMAL
    NORMAL
    STRONG
    STRONG

in
    3 5
    B 100
    A 100
    C 1000
    99
    100
    101
    500
    1000
out
    B
    B
    C
    C
    C
'''

import sys; input = sys.stdin.readline

n, m = map(int, input().split())
n_list = [ list(input().split()) for _ in range(n) ]

for _ in range(m):
    x = int(input())
    start, end = 0, len(n_list) - 1
    idx = 0

    while start <= end:
        mid = (start + end) // 2

        if int(n_list[mid][1]) >= x:
            end = mid - 1
            idx = mid
        else:
            start = mid + 1
    
    print(n_list[idx][0])

'''
bisect 사용
위 코드보다 동작도 빠르다.

from bisect import bisect_left
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
name = []
array = []
for i in range(n):
    x, y = input().split()
    name.append(x)
    array.append(int(y))
        
for i in range(m):
    print(name[bisect_left(array,int(input()))])
'''