# 백준 - 실버5 - 최소공배수 - 13241 - 수학, 정수론, 유클리드 호제법
'''
수학, 정수론, 유클리드 호제법

입력으로 들어오는 a, b를 곱한 뒤 a와 b의 최대 공약수로 나눠주면 된다.
최대 공약수는 유클리드 호제법으로 구했다.

아예 처음부터 python math 함수 내에서 lcm 을 이용하는 방법도 있다.
단, python 3.9 버전부터 가능하다. 23.08.16 기준으로 백준의 python 채점 버전은 3.11.0 이다.

lcm 이용 코드
from math import lcm
a, b = map(int, input().split())
print(lcm(a, b))
'''

a, b = map(int, input().split())

# 테스트
# a, b = 1, 1 # 1
# a, b = 3, 5 # 15
# a, b = 1, 123 # 123
# a, b = 121, 199 # 24079

def gcd(x, y):
    while x % y != 0:
        mod = x % y
        x = y
        y = mod
    return y

print((a * b) // gcd(a, b))
