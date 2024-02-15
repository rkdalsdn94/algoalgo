# 백준 - 실버5 - LCM - 5347 - 수학, 정수론, 유클리드 호제법
'''
수학, 정수론, 유클리드 호제법 문제

최소 공배수를 구하는 문제이다.
내장 함수인 math 안의 lcm을 이용해서 풀었다.
수학적인 풀이를 하고 싶다면 'a * b / 최대공약수' 이렇게 하면 된다.
즉, 최대 공약수만 구할 수 있으면 된다.

in
    3
    15 21
    33 22
    9 10
out
    105
    66
    90
'''

from math import lcm

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))
