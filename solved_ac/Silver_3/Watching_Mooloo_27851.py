# 백준 - 실버3 - Watching Mooloo - 27851 - 그리디 문제
"""
그리디 문제

[핵심 아이디어]
    1. 두 연속된 시청 날짜 사이의 간격이 K 이상이면 구독을 분리
    2. 간격이 K 미만이면 구독을 연결하여 하나로 처리
    3. 각 구독 그룹의 비용 = (마지막 날 - 첫 날 + 1) + K

[풀이 과정]
    1. 첫 번째 날부터 시작하여 연속된 날짜들을 그룹으로 묶음
    2. 다음 날과의 간격이 K 이상이면 현재 그룹을 종료하고 새 그룹 시작
    3. 각 그룹의 구독 비용을 계산하여 총합 구하기
"""

n, k = map(int, input().split())
days = list(map(int, input().split()))

# 테스트
# n, k = 2, 4
# days = [7, 9] # 7
# n, k = 2, 3
# days = [1, 10] # 8

total_cost = 0
start = 0  # 현재 구독 그룹의 시작 인덱스

for i in range(n):
    # 마지막 날이거나, 다음 날과의 간격이 K 이상인 경우
    if i == n - 1 or days[i + 1] - days[i] - 1 >= k:
        # 현재 그룹의 구독 비용 계산
        duration = days[i] - days[start] + 1
        total_cost += duration + k
        start = i + 1  # 다음 그룹 시작

print(total_cost)
