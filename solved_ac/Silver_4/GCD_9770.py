# 백준 - 실버4 - GCD - 9770 - 수학, 정수론, 완전 탐색, 유클리드 호제법 문제
'''
수학, 정수론, 완전 탐색, 유클리드 호제법 문제

최대 공약수(GCD)를 구하는 문제이다.
단순히 모든 숫자 쌍에 대해 GCD를 계산하여 최대값을 찾으면 된다.
입력이 언제 끝날지 모르기 때문에 try, except를 사용하여 입력을 받는다.

풀이 과정
    1. 모든 숫자 쌍에 대해 GCD를 계산하여 최대값을 찾는다.
    2. 최대값을 출력한다.
'''

from math import gcd
from itertools import combinations

def max_gcd(nums):
    max_gcd_value = 0

    # 모든 숫자 쌍에 대해 GCD를 계산하여 최대값 찾기
    for a, b in combinations(nums, 2):
        gcd_value = gcd(a, b)

        if gcd_value > max_gcd_value:
            max_gcd_value = gcd_value

    return max_gcd_value

nums = []
while 1:
    try:
        nums += list(map(int, input().split()))
    except:
        break

print(max_gcd(nums))
