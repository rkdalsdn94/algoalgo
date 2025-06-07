# 프로그래머스 - Lv3 - 다단계 칫솔 판매 - 그래프, 시뮬레이션, 해시(딕셔너리) 문제
"""
그래프, 시뮬레이션, 해시(딕셔너리) 문제

[핵심 아이디어]
    1. 다단계 조직을 트리 구조로 보고, 이익을 상위 노드(추천인)로 전파하는 방식
    2. 각 판매원은 자신의 이익에서 10%를 추천인에게 주고 90%를 자신이 가져감
    3. 10% 계산 시 1원 미만은 절사되므로, m//10이 0이 되면 전파 중단
    4. 해시맵을 사용하여 판매원 이름에서 인덱스로의 빠른 접근 구현

[풀이 과정]
    1. 결과 배열과 판매원 이름-인덱스 매핑 딕셔너리 초기화
    2. 각 판매 기록에 대해 이익 분배 시뮬레이션 수행:
       - 총 이익 계산 (판매량 * 100원)
       - while 루프로 추천인 체인을 따라 올라가며 이익 분배
       - 각 단계에서 90%는 현재 판매원이 가져가고, 10%는 상위로 전파
       - 추천인이 없거나(-) 분배할 금액이 0원이 되면 종료
    3. 최종 이익 배열 반환
"""

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    # 판매원 이름을 키로, 배열에서의 인덱스를 값으로 하는 딕셔너리
    name_to_index = {}

    # 판매원 이름과 인덱스 매핑 생성
    for i, name in enumerate(enroll):
        name_to_index[name] = i

    # 각 판매 기록에 대해 이익 분배 처리
    for seller_name, sell_amount in zip(seller, amount):
        # 총 이익 계산 (칫솔 하나당 100원)
        total_money = sell_amount * 100
        current_seller = seller_name

        # 추천인 체인을 따라 올라가며 이익 분배
        # 조건: 추천인이 존재하고(-가 아님) && 분배할 금액이 1원 이상
        while current_seller != "-" and total_money > 0:
            # 현재 판매원의 인덱스 찾기
            seller_idx = name_to_index[current_seller]

            # 현재 판매원이 가져갈 금액: 전체에서 10%를 뺀 나머지 (90%)
            # total_money - total_money//10 = total_money의 90%
            answer[seller_idx] += total_money - total_money // 10

            # 다음 단계로 전파할 금액: 현재 금액의 10% (소수점 버림)
            total_money //= 10

            # 다음 추천인으로 이동
            current_seller = referral[seller_idx]

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller, amount = ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))  # [360, 958, 108, 0, 450, 18, 180, 1080]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller, amount = ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]
print(solution(enroll, referral, seller, amount))  # [0, 110, 378, 180, 270, 450, 0, 0]
