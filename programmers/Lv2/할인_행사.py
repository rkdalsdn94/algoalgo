# 프로그래머스 - Lv2 - 할인 행사 - 구현, 슬라이딩 윈도우
"""
구현, 슬라이딩 윈도우, 해시(딕셔너리)

[핵심 아이디어]
    1. 10일 연속으로 할인 품목이 원하는 제품과 수량을 모두 충족하는지 확인
    2. 슬라이딩 윈도우 기법을 사용하여 10일 단위로 확인
    3. 딕셔너리를 활용하여 원하는 제품의 수량과 현재 윈도우의 제품 수량을 비교

[풀이 과정]
    1. 원하는 제품과 수량을 딕셔너리로 변환하여 관리
    2. discount 배열을 순회하며 10일 단위 윈도우를 확인:
       - 각 윈도우에서 할인하는 제품을 딕셔너리로 집계
       - 원하는 제품의 딕셔너리와 현재 윈도우의 딕셔너리를 비교
       - 모든 제품의 수량이 충족되면 정답 카운트 증가
    3. 총 가능한 날짜 수 반환
"""

def solution(want, number, discount):
    answer = 0

    # 원하는 제품과 수량을 딕셔너리로 변환
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    # 10일 단위로 윈도우를 이동하며 확인
    for i in range(len(discount) - 9):
        # 현재 10일 윈도우의 제품 집계
        current_dict = {}
        for j in range(i, i + 10):
            if discount[j] in current_dict:
                current_dict[discount[j]] += 1
            else:
                current_dict[discount[j]] = 1

        # 원하는 제품과 수량이 모두 충족되는지 확인
        is_possible = True
        for product, count in want_dict.items():
            if product not in current_dict or current_dict[product] < count:
                is_possible = False
                break

        # 가능하면 카운트 증가
        if is_possible:
            answer += 1

    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))  # 3

want = ["apple"]
number = [10]
discount = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
print(solution(want, number, discount))  # 0
