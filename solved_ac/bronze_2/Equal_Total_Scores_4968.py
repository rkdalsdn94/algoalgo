# 백준 - 브론즈2 - Equal Total Scores - 4968 - 수학, 완전 탐색 문제
'''
수학, 완전 탐색 문제

핵심 아이디어
    - 두 사람의 총점이 같아지도록 카드를 교환하는 문제
    - 가능한 모든 교환 케이스를 확인하여 최소 교환 카드 합을 찾는다.

풀이 과정
    1. n, m을 입력받는다.
    2. n만큼 반복하며 taro_cards를 입력받는다.
    3. m만큼 반복하며 hanako_cards를 입력받는다.
    4. find_exchange 함수를 통해 교환 가능한 카드 쌍을 찾는다.
    5. 결과를 출력한다.

in
    2 2
    1
    5
    3
    7
    4 5
    10
    0
    3
    8
    1
    9
    6
    0
    6
    2 3
    1
    1
    2
    2
    2
    0 0
out
    1 3
    -1
    -1
'''

def find_exchange(taro_cards, hanako_cards):
    # 현재 각자의 총점 계산
    taro_sum = sum(taro_cards)
    hanako_sum = sum(hanako_cards)

    # 가능한 모든 교환 케이스를 확인
    min_sum = float('inf')
    res = None

    for _, taro_card in enumerate(taro_cards):
        for _, hanako_card in enumerate(hanako_cards):
            # 카드를 교환했을 때의 새로운 총점 계산
            new_taro_sum = taro_sum - taro_card + hanako_card
            new_hanako_sum = hanako_sum - hanako_card + taro_card

            # 교환 후 총점이 같아지는 경우
            if new_taro_sum == new_hanako_sum:
                # 교환하는 카드들의 합이 최소인 경우를 찾음
                current_sum = taro_card + hanako_card
                if current_sum < min_sum:
                    min_sum = current_sum
                    res = (taro_card, hanako_card)

    return res

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # 카드 점수 입력 받기
    taro_cards = [int(input()) for _ in range(n)]
    hanako_cards = [int(input()) for _ in range(m)]

    # 교환 가능한 카드 쌍 찾기
    res = find_exchange(taro_cards, hanako_cards)

    # 결과 출력
    if res is None:
        print(-1)
    else:
        print(f"{res[0]} {res[1]}")
