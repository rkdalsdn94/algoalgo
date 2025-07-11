# 백준 - 실버5 - 슥 빡 빡 슥 - 28470 - 수학, 그리디, 사칙연산 문제
"""
수학, 그리디, 사칙연산 문제

[핵심 아이디어]
    1. 각 동작에서 공격 먼저 하거나 회피 먼저 하는 두 가지 선택이 있다.
    2. 공격 먼저: floor(A_i × K_i) - B_i, 회피 먼저: A_i - floor(B_i × K_i)
    3. 각 동작마다 두 선택 중 더 큰 값을 선택하는 그리디 접근법을 사용한다.
    4. 부동소수점 정밀도 오차를 피하기 위해 K_i를 10배하여 정수로 처리한다.

[풀이 과정]
    1. K_i가 소수점 첫째 자리까지만 주어지므로 10을 곱해서 정수로 변환한다.
    2. 각 동작 i에 대해 두 가지 경우의 아드레날린 변화량을 계산한다:
       - 공격 먼저: (A_i × K_i_int) // 10 - B_i
       - 회피 먼저: A_i - (B_i × K_i_int) // 10
    3. 정수 나눗셈(//)을 사용하여 floor 연산을 수행하고 부동소수점 오차를 완전히 제거한다.
    4. 두 값 중 더 큰 값을 선택하여 총 아드레날린에 누적한다.
    5. 모든 동작을 처리한 후 최종 아드레날린 양을 출력한다.
"""

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
k_list_str = input().split()  # K_i를 문자열로 받아 처리

# 테스트
# n = 3
# a_list = [30, 30, 30]
# b_list = [40, 40, 40]
# k_list = [3.4, 3.4, 3.4] # 186
# n = 5
# a_list = [11, 22, 33, 44, 55]
# b_list = [111, 99, 88, 77, 66]
# k_list = [1.1, 1.2, 1.3, 1.4, 1.5] # -218

res = 0

for i in range(n):
    # K_i를 정수로 변환하여 부동소수점 오차 제거 (예: 3.4 -> 34)
    # K_i가 소수점 첫째 자리까지 주어지므로 10을 곱해서 정수로 만듦
    k_val_int = int(float(k_list_str[i]) * 10)

    # 공격 먼저 하는 경우: floor(A_i * K_i) - B_i
    # (A_i * k_val_int) // 10 은 floor(A_i * K_i)와 동일
    attack_first = (a_list[i] * k_val_int) // 10 - b_list[i]

    # 회피 먼저 하는 경우: A_i - floor(B_i * K_i)
    dodge_first = a_list[i] - (b_list[i] * k_val_int) // 10

    # 더 큰 값을 선택 (그리디)
    res += max(attack_first, dodge_first)

print(res)
