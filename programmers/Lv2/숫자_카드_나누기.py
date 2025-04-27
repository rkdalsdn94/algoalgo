# 프로그래머스 - Lv2 - 숫자 카드 나누기 - 수학, 최대공약수
"""
수학, 최대공약수 문제

[핵심 아이디어]
    1. 각 배열의 최대공약수를 구한다
    2. A의 최대공약수로 B의 모든 원소를 나눠볼 때 하나라도 나누어 떨어지면 조건 불만족
    3. B의 최대공약수로 A의 모든 원소를 나눠볼 때 하나라도 나누어 떨어지면 조건 불만족
    4. 조건을 만족하는 최대공약수들 중 최댓값을 반환

[풀이 과정]
    1. 각 배열 원소들의 최대공약수(GCD)를 구한다
    2. A의 GCD가 B의 모든 원소로 나누어 떨어지지 않는지 확인한다
    3. B의 GCD가 A의 모든 원소로 나누어 떨어지지 않는지 확인한다
    4. 조건을 만족하는 GCD 중 최댓값을 반환한다
    5. 조건을 만족하는 GCD가 없으면 0을 반환한다
"""

from math import gcd
from functools import reduce

def get_gcd_of_array(arr):
    """배열의 모든 원소의 최대공약수를 구하는 함수"""
    return reduce(lambda x, y: gcd(x, y), arr)

def solution(arrayA, arrayB):
    answer = 0

    # 각 배열의 최대공약수 계산
    gcd_A = get_gcd_of_array(arrayA)
    gcd_B = get_gcd_of_array(arrayB)

    # 조건 1: A의 GCD로 B의 모든 원소가 나누어 떨어지지 않는지 확인
    if gcd_A > 1:  # GCD가 1이면 조건을 만족할 수 없음
        can_divide_all_B = all(b % gcd_A != 0 for b in arrayB)
        if can_divide_all_B:
            answer = max(answer, gcd_A)

    # 조건 2: B의 GCD로 A의 모든 원소가 나누어 떨어지지 않는지 확인
    if gcd_B > 1:
        can_divide_all_A = all(a % gcd_B != 0 for a in arrayA)
        if can_divide_all_A:
            answer = max(answer, gcd_B)

    return answer

print(solution([10, 17], [5, 20])) # 0
print(solution([10, 20], [5, 17])) # 10
print(solution([14, 35, 119], [18, 30, 102])) # 7
