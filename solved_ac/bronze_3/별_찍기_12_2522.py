'''
단순 구현 문제

일반적인 별 찍기 문제이다.

in
    3
out
      *
     **
    ***
     **
      *
'''

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)

for i in range(1, n):
    print(' ' * i + '*' * (n - i))
