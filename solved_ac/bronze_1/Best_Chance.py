# 백준 - 브론즈1 - Best Chance - 31800 - 구현 문제
"""
구현 문제

[핵심 아이디어]
    1. 각 물건의 기회비용을 구하려면 "자신을 제외한 최대 이익"이 필요
    2. 효율적으로 구하기 위해 전체에서 최댓값과 두 번째 최댓값을 미리 찾음
    3. 현재 물건의 이익이 최댓값이면 두 번째 최댓값을 사용하고, 아니면 최댓값을 사용
    4. 순수익 = 이익 - 기회비용 - 가격 = 이익 - (다른 최대이익 - 가격) - 가격 = 이익 - 다른 최대이익

[풀이 과정]
    1. 이익 배열에서 최댓값과 두 번째 최댓값을 찾는다
    2. 각 물건에 대해 다음 과정을 수행한다
       - 해당 물건의 이익이 최댓값인 경우: 두 번째 최댓값 사용
       - 그렇지 않은 경우: 최댓값 사용
    3. 순수익 = 현재 이익 - 사용할 최댓값
"""

n = int(input())
profits = list(map(int, input().split()))  # 각 물건의 이익
prices = list(map(int, input().split()))   # 각 물건의 가격

# 테스트
# n = 3
# profits = [280, 270, 240]
# prices = [100, 100, 100] # 10 -10 -40

# 최댓값과 두 번째 최댓값 찾기
max_profit = max(profits)
second_max_profit = -1

for profit in profits:
    if profit != max_profit and profit > second_max_profit:
        second_max_profit = profit

# 최댓값이 여러 개인 경우를 처리
if second_max_profit == -1:
    second_max_profit = max_profit

# 각 물건의 순수익 계산
result = []
for i in range(n):
    # 현재 물건을 제외한 최대 이익 선택
    if profits[i] == max_profit and profits.count(max_profit) == 1:
        # 현재 물건이 유일한 최댓값이면 두 번째 최댓값 사용
        other_max = second_max_profit
    else:
        # 그 외의 경우 최댓값 사용
        other_max = max_profit

    # 순수익 = 이익 - 다른 최대이익
    net_profit = profits[i] - other_max
    result.append(net_profit)

print(' '.join(map(str, result)))
