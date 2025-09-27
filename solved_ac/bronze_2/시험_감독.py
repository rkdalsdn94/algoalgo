# 백준 - 브론즈2 - 시험 감독 - 13458 - 수학, 구현 문제
"""
수학, 구현 문제

[핵심 아이디어]
    각 시험장마다 총감독관 1명 배치 후, 남은 학생 수에 대해 부감독관 수를 계산
    부감독관은 한 명이 c명의 학생을 감독할 수 있으므로, 남은 학생 수를 c로 나눈 후 올림 처리하여 필요한 부감독관 수를 구함

[풀이 과정]
    1. 각 시험장마다 총감독관 1명 배치
    2. 남은 학생 수에 대해 부감독관 수 계산 (올림 처리)
    3. 모든 시험장의 감독관 수를 합산하여 출력
"""

import math

n = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

# 테스트
# n = 1
# students = [1]
# b, c = 1, 1  # 1
# n = 3
# students = [3, 4, 5]
# b, c = 2, 2  # 7
# n = 5
# students = [1000000, 1000000, 1000000, 1000000, 1000000]
# b, c = 5, 7 # 714290
# n = 5
# students = [10, 9, 10, 9, 10]
# b, c = 7, 20  # 10
# n = 5
# students = [10, 9, 10, 9, 10]
# b, c = 7, 2  # 13

total_supervisors = 0

for student_count in students:
    # 각 시험장마다 총감독관 1명 배치
    total_supervisors += 1
    remaining_students = student_count - b
    if remaining_students > 0:
        # 남은 학생 수에 대해 부감독관 수 계산 (올림 처리)
        total_supervisors += math.ceil(remaining_students / c)

print(total_supervisors)
