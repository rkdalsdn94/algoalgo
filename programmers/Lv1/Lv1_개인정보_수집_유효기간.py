# 프로그래머스 - Lv1 - 개인정보 수집 유효기간 - 문자열, 날짜, 구현 문제
"""
문자열, 날짜, 구현 문제

[핵심 아이디어]
    1. 모든 날짜를 일수로 변환하여 비교한다.
    2. 약관 종류별 유효기간을 딕셔너리로 관리한다.
    3. 각 개인정보의 수집일자에 유효기간을 더한 후, 오늘 날짜와 비교한다.
    4. 유효기간이 지난 개인정보의 번호를 결과 배열에 추가한다.

[풀이 과정]
    1. 약관 종류별 유효기간을 딕셔너리로 변환한다.
    2. 오늘 날짜를 일수로 변환한다.
    3. 각 개인정보마다:
       a. 수집일자와 약관 종류를 파싱한다.
       b. 수집일자에 해당 약관의 유효기간(월)을 더한다.
       c. 날짜 계산 후 오늘 날짜와 비교하여 유효기간이 지났는지 확인한다.
       d. 유효기간이 지났다면 해당 개인정보 번호를 결과 배열에 추가한다.
    4. 결과 배열을 반환한다.
"""

def solution(today, terms, privacies):
    answer = []
    # 약관 종류별 유효기간 딕셔너리 생성
    term_dict = {t.split()[0]: int(t.split()[1]) for t in terms}

    # 오늘 날짜를 일수로 변환
    today_year, today_month, today_day = map(int, today.split('.'))
    today_days = (today_year * 12 * 28) + (today_month * 28) + today_day

    # 각 개인정보 검사
    for idx, privacy in enumerate(privacies, 1):
        # 수집일자와 약관 종류 파싱
        date, term_type = privacy.split()
        year, month, day = map(int, date.split('.'))

        # 유효기간(월) 추가
        month += term_dict[term_type]

        # 연도 조정
        year += (month - 1) // 12
        month = ((month - 1) % 12) + 1

        # 만료일은 해당 일자의 전날까지이므로 하루 빼기
        day -= 1
        if day == 0:
            month -= 1
            day = 28
            if month == 0:
                year -= 1
                month = 12

        # 날짜를 일수로 변환하여 비교
        privacy_days = (year * 12 * 28) + (month * 28) + day

        # 유효기간이 지났으면 번호 추가
        if today_days > privacy_days:
            answer.append(idx)

    return answer
