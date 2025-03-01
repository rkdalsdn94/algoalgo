# 프로그래머스 - Lv1 - 콜라 문제 - 시뮬레이션, 수학 문제
'''
시뮬레이션, 수학 문제

[핵심 아이디어]
    - 교환 프로세스를 반복 수행하여 최종적으로 받을 수 있는 콜라 병 수를 계산
    - 각 단계에서 교환 가능한 병 수와 교환 후 남는 병 수를 추적
    - 병을 교환할 때마다 받는 콜라 병 수(quotient * b)를 누적
    - 더 이상 교환할 수 없을 때까지(몫이 0이 될 때까지) 반복

[풀이 과정]
    1. 초기 빈 병 개수(n)를 교환 비율(a)로 나누어 현재 교환 가능한 병 수(quotient)와 남는 병 수(remainder) 계산
    2. 각 반복 단계에서:
        2.1. 현재 교환 가능한 병 수에 교환 보상률(b)을 곱하여 받을 수 있는 콜라 병 수 계산 및 누적
        2.2. 새로 받은 콜라를 마셔 생긴 빈 병과 이전에 남은 병을 합쳐 다음 교환을 위한 총 빈 병 수 산출
        2.3. 총 빈 병 수를 교환 비율(a)로 나누어 새로운 quotient와 remainder 계산
    3. 교환 가능한 병 수(quotient)가 0이 되면 반복 종료
    4. 총 누적된 콜라 병 수 반환
'''

def solution(a, b, n):
    answer = 0
    quotient, remainder = divmod(n, a)

    while quotient > 0:
        answer += quotient * b
        quotient = quotient * b + remainder
        quotient, remainder = divmod(quotient, a)

    return answer

print(solution(2, 1, 20) == 19)
print(solution(3, 1, 20) == 9)
print(solution(3, 2, 10) == 16)
