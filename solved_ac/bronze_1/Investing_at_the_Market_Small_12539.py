# 백준 - 브론즈1 - Investing at the Market (Small) - 12539 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

입력받은 M과 prices를 가지고 최대 이익을 구하는 문제이다.

풀이 과정
    1. 최대 이익을 저장할 변수 best_profit를 -1로 초기화한다.
    2. 최적의 구매 월을 저장할 변수 best_buy_month를 -1로 초기화한다.
    3. 최적의 판매 월을 저장할 변수 best_sell_month를 -1로 초기화한다.
    4. 같은 이익 시 더 낮은 구매가를 선택하기 위한 변수 lowest_buy_price를 무한대로 초기화한다.
    5. 0부터 10까지 순회하면서(1월~11월)
        5.1. buy_month를 구매 월로 설정한다.
        5.2. buy_price를 prices[buy_month]로 설정한다.
        5.3. buy_price가 M보다 큰 경우 구매 불가능한 경우이므로 건너뛴다.
        5.4. units를 M // buy_price로 설정한다.
        5.5. buy_month + 1부터 12까지 순회하면서(구매 월 다음 달부터 12월까지)
            5.5.1. sell_month를 판매 월로 설정한다.
            5.5.2. sell_price를 prices[sell_month]로 설정한다.
            5.5.3. profit를 units * (sell_price - buy_price)로 설정한다.
            5.5.4. 최적 결과 갱신(이익이 더 크거나, 이익이 같으면 구매가가 더 낮은 경우)
    6. best_profit가 0보다 작거나 같은 경우 "IMPOSSIBLE"을 반환한다.
    7. 그렇지 않으면 f"{best_buy_month} {best_sell_month} {best_profit}"를 반환한다.

in
    3
    100
    1 2 3 4 5 6 7 8 9 10 11 12
    100
    52 50 25 100 61 63 70 51 71 55 10 5
    100
    200 150 250 132 125 110 210 220 180 176 108 113
out
    Case #1: 1 12 1100
    Case #2: 3 4 300
    Case #3: IMPOSSIBLE
'''

def solve_case(M, prices):
    best_profit = -1          # 최고 이익을 저장할 변수
    best_buy_month = -1       # 최적의 구매 월
    best_sell_month = -1      # 최적의 판매 월
    lowest_buy_price = float('inf')  # 같은 이익 시 더 낮은 구매가를 선택하기 위한 변수

    for buy_month in range(11):  # 0부터 10까지 순회 (1월~11월)
        buy_price = prices[buy_month]

        if buy_price > M:  # 구매 불가능한 경우 건너뛰기
            continue

        units = M // buy_price  # 구매 가능한 최대 수량 계산

        for sell_month in range(buy_month + 1, 12):
            sell_price = prices[sell_month]
            profit = units * (sell_price - buy_price)  # 총 이익 계산

            # 최적 결과 갱신 (이익이 더 크거나, 이익이 같으면 구매가가 더 낮은 경우)
            if profit > best_profit or (profit == best_profit and buy_price < lowest_buy_price):
                best_profit = profit
                best_buy_month = buy_month + 1
                best_sell_month = sell_month + 1
                lowest_buy_price = buy_price

    if best_profit <= 0:
        return "IMPOSSIBLE"
    return f"{best_buy_month} {best_sell_month} {best_profit}"

N = int(input())

for case in range(1, N + 1):
    M = int(input())
    prices = list(map(int, input().split()))

    result = solve_case(M, prices)
    print(f"Case #{case}: {result}")
