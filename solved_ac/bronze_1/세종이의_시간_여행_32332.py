# 백준 - 브론즈1 - 세종이의 시간 여행 - 32332 - 수학, 구현, 사칙연산 문제
"""
수학, 구현, 사칙연산 문제

[핵심 아이디어]
    1. 타임머신의 버그로 인해 입력값과 반대 방향으로 이동하는 특성을 이용
    2. 현재 위치에서 목표 위치까지의 차이를 구하고, 그 차이만큼 반대 방향으로 입력값 설정
    3. 시간은 일 단위로 통일하여 계산 (1년 = 12개월 = 360일, 1개월 = 30일)
    4. 위도와 경도는 단순한 좌표 차이 계산

[풀이 과정]
    1. 현재 시각과 목표 시각을 일 단위로 변환하여 차이 계산
    2. 시간 차이의 반대 방향이 되도록 입력 시각 계산
    3. 위도, 경도의 차이를 구하고 반대 방향으로 입력 좌표 계산
    4. 일 단위를 다시 년/월/일 형태로 변환하여 출력
"""

def date_to_days(year, month, day):
    """년/월/일을 총 일수로 변환 (기준점에서부터의 절대 일수)"""
    return year * 12 * 30 + (month - 1) * 30 + (day - 1)

def days_to_date(days):
    """총 일수를 년/월/일로 변환"""
    year = days // (12 * 30)
    remaining = days % (12 * 30)
    month = remaining // 30 + 1
    day = remaining % 30 + 1
    return year, month, day

Y0, M0, D0, T0, P0 = input().split()
Y1, M1, D1, T1, P1 = input().split()

# 테스트
# Y0, M0, D0, T0, P0 = '2024 9 20 37.556 127.047'.split()
# Y1, M1, D1, T1, P1 = '2624 9 20 37.532 127.117'.split() # 1424 9 20 37.580 126.977
# Y0, M0, D0, T0, P0 = '2624 9 20 37.551 127.074'.split()
# Y1, M1, D1, T1, P1 = '2024 9 20 37.503 127.095'.split() # 3224 9 20 37.599 127.053
# Y0, M0, D0, T0, P0 = '2024 1 1 37.000 127.000'.split()
# Y1, M1, D1, T1, P1 = '2024 1 2 37.500 130.000'.split() # 2023 12 30 36.500 124.000

Y0, M0, D0 = int(Y0), int(M0), int(D0)
Y1, M1, D1 = int(Y1), int(M1), int(D1)
T0, P0 = float(T0), float(P0)
T1, P1 = float(T1), float(P1)

# 현재 시간과 목표 시간을 일로 변환
current_days = date_to_days(Y0, M0, D0)
target_days = date_to_days(Y1, M1, D1)

# 시간 차이 계산
diff_days = target_days - current_days

# 타임머신에 입력해야 할 시간 (반대 방향)
# 목표가 미래면 과거를 입력, 목표가 과거면 미래를 입력
input_days = current_days - diff_days

# 일을 년/월/일로 변환
input_year, input_month, input_day = days_to_date(input_days)

# 위도, 경도 차이 계산
diff_lat = T1 - T0  # 목표 위도 - 현재 위도
diff_lon = P1 - P0  # 목표 경도 - 현재 경도

# 타임머신에 입력해야 할 위도, 경도 (반대 방향)
# 목표가 북쪽이면 남쪽을 입력, 목표가 남쪽이면 북쪽을 입력
input_lat = T0 - diff_lat
input_lon = P0 - diff_lon

print(f"{input_year} {input_month} {input_day} {input_lat:.3f} {input_lon:.3f}")
