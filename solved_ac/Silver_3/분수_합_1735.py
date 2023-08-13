# 백준 - 실버3 - 분수 합 - 1735 - 수학, 정수론, 유클리드 호제법
'''
수학, 정수론, 유클리드 호제법

단순한 수학 문제이다.

두 분수를 더한 뒤 분자와 분모의 최대 공약수를 구한다(유클리드 호제법으로 구했음).
분자와 분모를 기약 분수로 만들기 위해 위에서 구한 최대 공약수의 값으로 분자와 분모 모두 최대 공약수의 값으로 나누어 출력하면 된다..
'''

a, b = map(int, input().split())
c, d = map(int, input().split())

# 테스트
# a, b = 2, 7
# c, d = 3, 5 # 31 35

def gcd(x, y):
    while x % y != 0:
        mod = x % y
        x = y
        y = mod
    return y

numer = a * d + c * b
denom = b * d
gcd = gcd(numer, denom)
print(numer // gcd, denom // gcd)
