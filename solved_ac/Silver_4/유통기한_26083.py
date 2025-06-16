# 백준 - 실버4 - 유통기한 - 26083 - 구현, 많은 조건 분기 문제
"""
구현, 많은 조건 분기 문제

PyPy3로 제출해야 시간 초과가 나지 않는다.

[핵심 아이디어]
    1. 세 가지 날짜 형식(연도/월/일, 일/월/연도, 월/일/연도)으로 해석하여 유효한 날짜들을 찾는다.
    2. 윤년 계산과 각 월의 일수를 정확히 계산하여 날짜 유효성을 검증한다.
    3. 유효한 모든 해석에서 오늘 날짜보다 이후인지 확인하여 안전성을 판단한다.

[풀이 과정]
    1. 윤년 판단 함수와 날짜 유효성 검증 함수를 작성한다.
    2. A/B/C를 세 가지 방식으로 해석하여 유효한 날짜 리스트를 생성한다.
    3. 유효한 날짜가 없으면 "invalid", 모든 유효한 날짜가 오늘 이후면 "safe", 그렇지 않으면 "unsafe"를 출력한다.
"""

y, m, d = map(int, input().split())
n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# y, m, d = 22, 11, 26
# n = 4
# n_list = [[22, 11, 30], [22, 11, 31], [22, 12, 1], [22, 22, 2]] # safe  \  safe \ unsafe \ invalid

def is_leap_year(year):
    """윤년 판단 함수"""
    return year % 4 == 0

def is_valid_date(year, month, day):
    """날짜 유효성 검증 함수"""
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False

    # 각 월의 일수
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 윤년인 경우 2월은 29일까지
    if is_leap_year(year):
        days_in_month[1] = 29

    return day <= days_in_month[month - 1]

def date_to_days(year, month, day):
    """날짜를 일 단위로 변환하여 비교용으로 사용"""
    return year * 10000 + month * 100 + day

today = date_to_days(2000 + y, m, d)

for a, b, c in n_list:
    valid_dates = []

    # 1. 연도/월/일 형식: A/B/C = (2000+A)년 B월 C일
    if is_valid_date(2000 + a, b, c):
        valid_dates.append(date_to_days(2000 + a, b, c))

    # 2. 일/월/연도 형식: A/B/C = (2000+C)년 B월 A일
    if is_valid_date(2000 + c, b, a):
        valid_dates.append(date_to_days(2000 + c, b, a))

    # 3. 월/일/연도 형식: A/B/C = (2000+C)년 A월 B일
    if is_valid_date(2000 + c, a, b):
        valid_dates.append(date_to_days(2000 + c, a, b))

    # 중복 제거
    valid_dates = list(set(valid_dates))
    if not valid_dates:
        print("invalid")
    elif all(date >= today for date in valid_dates):
        print("safe")
    else:
        print("unsafe")
