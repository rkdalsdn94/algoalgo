# 백준 - 골드3 - 공주님의 정원 - 2457 - 그리디, 정렬 문제
'''
그리디, 정렬 문제

[핵심 아이디어]
    - 3월 1일부터 11월 30일까지 꽃이 피어있어야 함
    - 시작일을 기준으로 정렬하여 가장 늦게 지는 꽃을 선택
    - 선택한 꽃으로 커버되지 않는 날짜가 발생하면 0 출력
    - 목표 기간을 모두 커버하면 선택한 꽃의 개수 출력

[풀이 과정]
    1. 입력받은 날짜를 일수로 변환하여 저장
    2. 시작일을 기준으로 정렬
    3. 3월 1일부터 11월 30일까지 커버해야 함
    4. 현재 날짜에 피어있을 수 있는 꽃들 중 가장 늦게 지는 꽃 선택
    5. 더 이상 선택할 꽃이 없는 경우 0 출력
    6. 목표 기간을 모두 커버한 경우 선택한 꽃의 개수 출력

in
    4
    1 1 5 31
    1 1 6 30
    5 15 8 31
    6 10 12 10
out
    2

in
    10
    2 15 3 23
    4 12 6 5
    5 2 5 31
    9 14 12 24
    6 15 9 3
    6 3 6 15
    2 28 4 25
    6 15 9 27
    10 5 12 31
    7 14 9 1
out
    5
'''

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 월의 일수를 저장
def date_to_days(month, day):
    total_days = sum(days_in_month[:month]) + day # 해당 날짜까지의 총 일수 계산

    return total_days

n = int(input())
flowers = []

# 입력받은 날짜를 일수로 변환하여 저장
for _ in range(n):
    start_month, start_day, end_month, end_day = map(int, input().split())
    start_days = date_to_days(start_month, start_day)
    end_days = date_to_days(end_month, end_day)
    flowers.append((start_days, end_days))

flowers.sort() # 시작일을 기준으로 정렬

# 3월 1일부터 11월 30일까지 커버해야 함
target_start = date_to_days(3, 1)
target_end = date_to_days(11, 30)

current_day = target_start  # 현재 커버해야 하는 시작일
count = 0  # 선택한 꽃의 개수
idx = 0  # 현재 확인 중인 꽃의 인덱스

while current_day <= target_end:
    next_day = current_day

    # 현재 날짜에 피어있을 수 있는 꽃들 중 가장 늦게 지는 꽃 선택
    while idx < n and flowers[idx][0] <= current_day:
        next_day = max(next_day, flowers[idx][1])
        idx += 1

    # 더 이상 선택할 꽃이 없는 경우
    if next_day == current_day:
        print(0)
        break

    count += 1
    current_day = next_day

    # 목표 기간을 모두 커버한 경우
    if current_day > target_end:
        print(count)
        break
