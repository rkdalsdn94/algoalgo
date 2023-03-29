# 백준 - 브론즈2 - 막대기 - 17608 - 단순 구현 문제
'''
단순 구현 문제

단순 구현 문제이다.
n_list의 값을 역순으로 돌면서 이 전값을 담고 있는 temp보다 클 경우 res를 1씩 더해주고 temp를 바꾸면 된다.
'''

import sys; input = sys.stdin.readline

# 테스트
# n = 6
# n_list = [ 6, 9, 7, 6, 4, 6 ] # 3
# n = 5
# n_list = [ 5, 4, 3, 2, 1 ] # 5

n = int(input())
n_list = [ int(input()) for _ in range(n) ]
res = 1

temp = n_list[-1]
for i in range(n - 2, -1, -1):
    if temp < n_list[i]:
        res += 1
        temp = n_list[i]

print(res)
