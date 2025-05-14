# 프로그래머스 - Lv2 - 이모티콘 할인행사 - 완전 탐색, 시뮬레이션 문제
"""
완전 탐색, 시뮬레이션 문제

[핵심 아이디어]
    1. 각 이모티콘에 적용할 수 있는 할인율이 정해져 있으므로(10%, 20%, 30%, 40%) 가능한 모든 할인율 조합을 완전탐색한다.
    2. 각 할인율 조합에 대해 모든 사용자의 구매 행동을 시뮬레이션한다.
    3. 우선순위에 따라 이모티콘 플러스 가입자 수를 최대화하고, 그 다음으로 매출액을 최대화한다.

[풀이 과정]
    1. itertools의 product를 활용하여 각 이모티콘에 적용할 수 있는 모든 할인율 조합을 생성한다.
    2. 각 할인율 조합에 대해 다음 과정을 수행한다:
       a. 모든 사용자에 대해 할인된 이모티콘 구매 여부를 결정하고 총 구매 비용을 계산한다.
       b. 사용자의 총 구매 비용이 기준 가격 이상이면 플러스 서비스에 가입하고, 그렇지 않으면 이모티콘을 구매한다.
    3. 각 조합의 결과(플러스 가입자 수, 총 매출액)를 비교하여 최적의 결과를 찾는다:
       a. 플러스 가입자 수가 더 많은 경우 결과를 업데이트한다.
       b. 플러스 가입자 수가 같은 경우 매출액이 더 높으면 결과를 업데이트한다.
"""

from itertools import product

def solution(users, emoticons):
    answer = [0, 0]  # [플러스 서비스 가입자 수, 이모티콘 총 매출액]
    discount_rate = [10, 20, 30, 40]  # 가능한 할인율 목록

    # 가능한 모든 할인율 조합에 대해 완전탐색
    for discount in product(discount_rate, repeat=len(emoticons)):
        total_pay, plus_num = 0, 0  # 현재 조합의 총 매출액과 플러스 가입자 수

        # 각 사용자별로 구매 행동 시뮬레이션
        for rate, price in users:
            pay = 0  # 현재 사용자의 이모티콘 구매 비용
            # 각 이모티콘에 대해 할인율 조건을 만족하면 구매
            for i, emoticon in enumerate(emoticons):
                if discount[i] >= rate:  # 사용자의 기준 할인율 이상인 경우 구매
                    pay += emoticon * (100 - discount[i]) // 100  # 할인된 가격으로 구매

            # 구매 비용이 기준 가격 이상이면 플러스 서비스 가입
            if pay >= price:
                plus_num += 1
            else:
                total_pay += pay  # 그렇지 않으면 이모티콘 구매 비용 추가

        # 결과 업데이트 (우선순위: 1. 플러스 가입자 수, 2. 총 매출액)
        if plus_num > answer[0]:
            answer[0], answer[1] = plus_num, total_pay
        elif plus_num == answer[0] and total_pay > answer[1]:
            answer[1] = total_pay

    return answer

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users, emoticons) == [1, 5400])

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons) == [4, 13860])
