# 백준 - 실버4 - International meeting - 수학, 구현, 문자열, 사칙연산, 파싱 문제
"""
수학, 구현, 문자열, 사칙연산, 파싱 문제

[핵심 아이디어]
    1. 시간대 변환은 반드시 UTC를 기준점으로 해야 함
    2. YJ의 시간을 먼저 UTC로 변환한 후, 각 동료의 시간대로 변환
    3. 시간대 오프셋은 정수뿐만 아니라 0.5 단위도 포함됨
    4. 하루는 1440분(24시간 × 60분)으로 계산하여 날짜 경계 처리

[풀이 과정]
    1. YJ의 미팅 시간과 시간대 정보를 파싱
    2. YJ의 시간을 UTC로 변환 (YJ 시간 - YJ의 UTC 오프셋)
    3. 각 동료에 대해 다음의 과정을 진행
       - 동료의 UTC 오프셋 파싱
       - UTC 시간에 동료의 오프셋을 더해 해당 시간대 시간 계산
       - 1440분 단위로 정규화하여 0~23:59 범위 유지
    4. HH:MM 형식으로 출력
"""

n = int(input())
time_utc_line = input().split()
n_list = [input() for _ in range(n)]

# 테스트
# n = 4
# time_utc_line = "23:00", "UTC+9"
# n_list = [
#     "UTC+8.5", "UTC-1", "UTC+12", "UTC+10"
# ] # 22:30  \  13:00  \  02:00  \  00:00

time = time_utc_line[0]
yj_utc = time_utc_line[1]

# YJ의 시간 파싱
hh, mm = map(int, time.split(':'))
total_minutes = hh * 60 + mm

# YJ의 UTC 오프셋 파싱
yj_sign = yj_utc[3]
yj_offset = float(yj_utc[4:])
if yj_sign == '-':
    yj_offset = -yj_offset

# YJ의 시간을 UTC로 변환
utc_minutes = total_minutes - int(yj_offset * 60)

# 각 동료의 시간대로 변환
for i in n_list:
    # 동료의 UTC 오프셋 파싱
    sign = i[3]
    offset = float(i[4:])
    if sign == '-':
        offset = -offset

    # UTC에서 동료의 시간대로 변환
    coworker_minutes = utc_minutes + int(offset * 60)

    # 하루 범위로 정규화 (0~1439분)
    coworker_minutes = coworker_minutes % 1440

    # 시간과 분으로 변환
    hh = coworker_minutes // 60
    mm = coworker_minutes % 60

    print(f"{hh:02}:{mm:02}")
