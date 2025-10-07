# 프로그래머스 - Lv3 - 셔틀버스 - 시뮬레이션, 그리디, 정렬 문제
"""
시뮬레이션, 그리디, 정렬 문제

[핵심 아이디어]
    1. 모든 셔틀 도착 시간을 계산하고, 크루들을 도착 시간 순으로 정렬
    2. 각 셔틀마다 탑승 가능한 크루를 시뮬레이션으로 태움
    3. 마지막 셔틀의 상태에 따라 콘이 도착해야 하는 최적의 시간을 결정
       - 자리가 남으면: 콘은 셔틀 시간에 도착
       - 만석이면: 마지막 탑승자보다 1분 일찍 도착

[풀이 과정]
    1. 시간을 분 단위로 변환 (HH:MM -> 분)
    2. 셔틀 시간표 생성 (09:00부터 n회, t분 간격)
    3. 크루 도착 시간을 오름차순 정렬
    4. 각 셔틀마다 탑승 시뮬레이션 수행
    5. 마지막 셔틀의 상태에 따라 콘의 최적 도착 시간 결정
"""

def solution(n, t, m, timetable):
    # 시간을 분 단위로 변환하는 함수
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(':'))
        return h * 60 + m

    # 분을 HH:MM 형식으로 변환하는 함수
    def minutes_to_time(minutes):
        h = minutes // 60
        m = minutes % 60
        return f"{h:02d}:{m:02d}"

    # 크루 도착 시간을 분 단위로 변환하고 정렬
    crew_times = sorted([time_to_minutes(time) for time in timetable])

    # 셔틀 시간표 생성 (09:00 = 540분부터 시작)
    shuttle_times = []
    start_time = 9 * 60  # 09:00
    for i in range(n):
        shuttle_times.append(start_time + i * t)

    # 각 셔틀에 탑승한 크루를 추적
    crew_index = 0  # 현재 확인 중인 크루의 인덱스

    # 마지막 셔틀을 제외한 모든 셔틀 처리
    for i in range(n - 1):
        shuttle_time = shuttle_times[i]
        boarded = 0  # 현재 셔틀에 탑승한 인원 수

        # 이 셔틀 시간 이하에 도착한 크루를 최대 m명까지 태움
        while crew_index < len(crew_times) and boarded < m and crew_times[crew_index] <= shuttle_time:
            crew_index += 1
            boarded += 1

    # 마지막 셔틀 처리
    last_shuttle_time = shuttle_times[-1]
    boarded = 0
    last_boarded_time = 0

    # 마지막 셔틀에 탈 수 있는 크루 확인
    while crew_index < len(crew_times) and boarded < m and crew_times[crew_index] <= last_shuttle_time:
        last_boarded_time = crew_times[crew_index]
        crew_index += 1
        boarded += 1

    # 콘의 최적 도착 시간 결정
    if boarded < m:
        # 마지막 셔틀에 자리가 남으면 셔틀 시간에 도착
        answer = last_shuttle_time
    else:
        # 마지막 셔틀이 만석이면 마지막 탑승자보다 1분 일찍 도착
        answer = last_boarded_time - 1

    return minutes_to_time(answer)
