# 솔브드 - 브론즈2 - 화성 수학 - 단순 구현, 사칙연산 문제
'''
단순 구현, 사칙연산 문제

입력으로 주어진 값을 첫 번째 값만 빼서 쪼갠 후 계산하면 되는 단순 구현 문제이다.
소수점 두 번째 자리 까지만 잘 기억하면 된다.

in
    3
    3 @ %
    10.4 # % @
    8 #
out
    14.00
    25.20
    1.00
'''

t = int(input())

for _ in range(t):
    a = input().split()
    res = float(a[0])
    
    for i in a[1:]:
        if i == '@':
            res *= 3
        elif i == '%':
            res += 5
        elif i == '#':
            res -= 7
    
    print(f'{res:.2f}')
