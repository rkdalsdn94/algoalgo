# 프로그래머스 - Lv1 - 가장 많이 받은 선물 - 구현, 시뮬레이션 문제
"""
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 선물 교환 기록을 2차원 테이블로 관리
    2. 선물 지수(준 선물 - 받은 선물) 계산
    3. 규칙에 따라 다음 달 선물 수 계산

[풀이 과정]
    1. 친구 이름을 인덱스로 매핑
    2. 선물 기록 처리 및 선물 지수 계산
    3. 규칙에 따라 다음 달 선물 계산:
       - 이전에 더 많이 준 사람이 선물 받음
       - 교환 기록이 같으면 선물 지수가 높은 사람이 받음
    4. 최대 선물 수 반환
"""

def solution(friends, gifts):
    n = len(friends)

    # 친구 이름을 인덱스로 매핑
    name_to_idx = {}
    for i in range(n):
        name_to_idx[friends[i]] = i

    # 선물 지수와 교환 기록 초기화
    gift_index = [0] * n
    gift_table = [[0] * n for _ in range(n)]

    # 선물 기록 처리
    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx, receiver_idx = name_to_idx[giver], name_to_idx[receiver]
        gift_index[giver_idx] += 1
        gift_index[receiver_idx] -= 1
        gift_table[giver_idx][receiver_idx] += 1

    # 다음 달 선물 계산
    next_gifts = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # 더 많이 준 경우
            if gift_table[i][j] > gift_table[j][i]:
                next_gifts[i] += 1
            # 주고받은 수가 같은 경우
            elif gift_table[i][j] == gift_table[j][i]:
                if gift_index[i] > gift_index[j]:
                    next_gifts[i] += 1

    return max(next_gifts)

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(friends, gifts)) # 2

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
print(solution(friends, gifts))

friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends, gifts)) # 0
