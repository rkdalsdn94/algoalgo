# 백준 - 브론즈1 - 최소공배수 - 1934 - 수학, 정수론, 유클리드 호제법 문제
'''
수학, 정수론, 유클리드 호제법 문제

유클리드 호제법으로 최대 공약수를 구한 다음에 a랑 b를 곱한 뒤 최대 공약수로 나누면 최소 공배수가 된다.

in
    3
    1 45000
    6 10
    13 17
out
    45000
    30
    221
'''

def gcd(x, y):
    while x % y != 0:
        mod = x % y
        x = y
        y = mod
    return y

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print((a * b) // gcd(a, b))
