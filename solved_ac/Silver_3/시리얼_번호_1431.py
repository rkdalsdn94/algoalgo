'''
in
    5
    ABCD
    145C
    A
    A910
    Z321
out
    A
    ABCD
    Z321
    145C
    A910
문제에 주어진 순서대로 차분하게 풀면 쉽게 풀 수 있다.
'''

from sys import stdin
input = stdin.readline

n = int(input())
n_list = []

for _ in range(n):
    num = 0
    serial_number = input().strip()
    for i in serial_number:
        if i.isdigit():
            num += int(i)
    n_list.append((serial_number, num))

# 1. A, B 중에 짧은 것, 2. 길이가 같다면 숫자인 것들만 비교 후 작은 합, 3. 사전순 정렬
res = [ i for i, j in sorted( n_list, key=lambda x: (len(x[0]), x[1], x[0]) ) ]
print(*res)
