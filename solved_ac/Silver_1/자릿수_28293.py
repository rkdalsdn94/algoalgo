# 백준 - 실버1 - 자릿수 - 28293 - 수학 문제
'''
수학 문제

단순하게 생각했다가 시간 초과가 발생한 문제 (사실 안 될거 알긴 했는데 혹시 하면서 했음)

풀이 과정
    1. 입력값을 받는다.
    2. 입력값을 공백을 기준으로 나눈다.
    3. math 모듈을 사용하여 a의 b승을 구한다.
    4. 결과값을 출력한다.
'''

import math

a, b = map(int, input().split())
res = math.log10(a) * b
res = int(res) + 1

print(res)

'''
시간 초과 코드

a, b = map(int, input().split())
print(len(a ** b))
'''
