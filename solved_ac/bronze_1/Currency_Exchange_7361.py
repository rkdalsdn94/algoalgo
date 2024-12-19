# 백준 - 브론즈1 - Currency Exchange - 7361 - 수학, 사칙 연산 문제
'''
수학, 사칙 연산 문제

풀이 과정
    1. 환율표 입력 받기
        1.1. 5x5 크기의 2차원 리스트를 생성한다
        1.2. 각 행마다 5개의 실수를 입력받아 저장한다

    2. 여행 정보 입력 및 처리
        2.1. 첫 번째 숫자(n)를 입력받는다
        2.2. n이 0이면 프로그램을 종료한다
        2.3. n이 0이 아닌 경우:
            2.3.1. n개의 숫자(방문할 국가 번호)를 입력받는다
            2.3.2. 마지막 숫자(초기 금액)를 입력받는다

    3. 환전 계산 수행
        3.1. 초기 금액을 시작으로 설정한다
        3.2. 현재 국가를 US(1)로 설정한다
        3.3. 여행 경로를 따라 순차적으로 환전:
            3.3.1. 현재 국가에서 다음 국가로의 환율을 찾는다
            3.3.2. 현재 금액에 환율을 곱한다
            3.3.3. 결과를 소수점 둘째 자리에서 반올림한다
            3.3.4. 현재 국가를 다음 국가로 업데이트한다
        3.4. 마지막으로 US 달러로 환전한다
            3.4.1. 현재 국가에서 US로의 환율을 찾는다
            3.4.2. 현재 금액에 환율을 곱한다
            3.4.3. 결과를 소수점 둘째 자리에서 반올림한다

    4. 결과 출력
        4.1. 최종 금액을 소수점 둘째 자리까지 표시하여 출력한다
        4.2. 2번 과정으로 돌아가 다음 여행을 처리한다

in
    1 1.57556 1.10521 0.691426 7.25005
    0.634602 1 0.701196 0.43856 4.59847
    0.904750 1.42647 1 0.625627 6.55957
    1.44616 2.28059 1.59840 1 10.4843
    0.137931 0.217555 0.152449 0.0953772 1
    3 2 4 5 20.00
    1 3 100.00
    6 2 3 4 2 4 3 120.03
    0
out
    19.98
    99.99
    120.01
'''

def round_currency(amount):
    # 소수점 둘째 자리에서 반올림 (0.005는 0.01로 반올림)
    return round(amount * 100) / 100

def process_trip(exchange_rates, route, initial_amount):
    current_amount = initial_amount
    current_country = 1  # 시작은 항상 US (country 1)

    # 경로를 따라 환전 진행
    for next_country in route:
        # 현재 국가에서 다음 국가로의 환율을 적용
        rate = exchange_rates[current_country - 1][next_country - 1]
        current_amount = round_currency(current_amount * rate)
        current_country = next_country

    # 마지막으로 US 달러로 환전
    final_amount = round_currency(current_amount * exchange_rates[current_country - 1][0])
    return final_amount

# 환율 테이블 입력 받기 (5x5 행렬)
exchange_rates = []
for _ in range(5):
    rates = list(map(float, input().split()))
    exchange_rates.append(rates)

# 여행 경로 처리
while True:
    # 여행 정보 입력
    trip_info = list(map(float, input().split()))
    n = int(trip_info[0])

    # 입력 종료 조건
    if n == 0:
        break

    # 경로와 초기 금액 추출
    route = [int(trip_info[i]) for i in range(1, n + 1)]
    initial_amount = trip_info[n + 1]

    # 여행 처리 및 결과 출력
    res = process_trip(exchange_rates, route, initial_amount)
    print(f"{res:.2f}")
