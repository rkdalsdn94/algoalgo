# 백준 - 브론즈5 - 영수증 - 25304 - 단순 구현, 사칙연산 문제
'''
단순 구현, 사칙연산 문제

단순하게 구현하면 되는 문제이다. n만큼 입력으로 들어온 값들을 res에 담은 후, res와 x가 같으면 'Yes' 다르면 'No'를 출력하면 된다.
'''

x = int(input())
n = int(input())
res = 0

for _ in range(n):
    a, b = map(int, input().split())
    res += a * b

if x == res:
    print('Yes')
else:
    print('No')
