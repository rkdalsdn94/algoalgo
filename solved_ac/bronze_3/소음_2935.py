# 백준 - 브론즈3 - 소음 - 2935 - 단순 구현, 사칙연산 문제
'''
단순 구현, 사칙연산 문제

따로 설명을 안해도 될 정도로 단순한 구현이다.
a, operator(연산자), b 를 입력받고 연사자가 '+' 이면 더하기, '*' 이면 곱하면 되는 단순한 문제이다.
'''

a, operator, b = int(input()), input(), int(input())

# 테스트
# a, operator, b = 1000, '*', 100 # 100000
# a, operator, b = 10000, '+', 10 # 10010
# a, operator, b = 10, '+', 1000 # 1010
# a, operator, b = 1, '*', 1000 # 1000

if operator == '+':
    print(a + b)
elif operator == '*':
    print(a * b)
