# 백준 - 실버4 - 요요 시뮬레이션 - 19636 - 구현 문제
"""
구현 문제

[핵심 아이디어]
    1. 두 가지 시나리오를 각각 시뮬레이션 (기초 대사량 변화 고려 안함/고려함)
    2. 매일 체중과 기초 대사량의 변화를 계산하여 사망 조건을 체크
    3. 요요 현상은 다이어트 후 원래 생활로 돌아갔을 때 체중이 증가하는지로 판단

[풀이 과정]
    1. 첫 번째 시나리오: 기초 대사량을 고정하고 체중만 변화시킴
       - 매일 체중 변화량 계산: (일일 에너지 섭취량 - 일일 에너지 소비량)
       - 체중이 0 이하가 되면 "Danger Diet" 출력
    2. 두 번째 시나리오: 체중과 기초 대사량 모두 변화시킴
       - 매일 체중 변화 후 기초 대사량 변화 계산
       - 기초 대사량 변화 조건: |에너지 차이| > T이면 ⌊에너지 차이 / 2⌋만큼 변화
       - 체중 ≤ 0 또는 기초 대사량 ≤ 0이면 "Danger Diet" 출력
    3. 요요 현상 체크: 다이어트 후 원래 생활로 돌아갔을 때 체중 증가 여부
       - 원래 섭취량 - (변화된 기초 대사량 + 0) > 0이면 "YOYO", 아니면 "NO"
"""

w, l, t = map(int, input().split())
d, i, a = map(int, input().split())

# 테스트
# w, l, t = 100000, 1500, 500
# d, i, a = 5, 1000, 700 # 94000 1500  \  97300 600 YOYO
# w, l, t = 100000, 1500, 500
# d, i, a = 5, 1300, 300 # 97500 1500  \  97500 1500 NO
# w, l, t = 10000, 2000, 500
# d, i, a = 5, 500, 500 # Danger Diet  \  5500 500 YOYO
# w, l, t = 100000, 1500, 500
# d, i, a = 5, 0, 500 # 90000 1500  \  Danger Diet

# 첫 번째 시나리오: 기초 대사량 변화 고려하지 않음
weight1 = w
for day in range(d):
    energy_diff = i - (l + a)  # 일일 에너지 섭취량 - 일일 에너지 소비량
    weight1 += energy_diff

    if weight1 <= 0:
        print("Danger Diet")
        break
else:
    print(weight1, l)

# 두 번째 시나리오: 기초 대사량 변화 고려함
weight2 = w
bmr2 = l  # 기초 대사량
danger = False

for day in range(d):
    energy_diff = i - (bmr2 + a)
    weight2 += energy_diff

    # 체중 사망 조건 체크
    if weight2 <= 0:
        danger = True
        break

    # 기초 대사량 변화
    if abs(energy_diff) > t:
        bmr2 += energy_diff // 2

    # 기초 대사량 사망 조건 체크
    if bmr2 <= 0:
        danger = True
        break

if danger:
    print("Danger Diet")
else:
    yoyo = "YOYO" if l - bmr2 > 0 else "NO"
    print(weight2, bmr2, yoyo)
