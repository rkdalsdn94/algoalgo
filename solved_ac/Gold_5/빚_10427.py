# 백준 - 골드5 - 빚 - 10427 - 그리디, 정렬, 누적 합 문제
'''
그리디, 정렬, 누적 합 문제

핵심 아이디어
  - M개의 빚을 선택할 때, 연속된 M개를 선택하는 것이 최적해이다.
  - 정렬을 하면 각 구간의 최대값 × M에서 구간합을 뺀 값이 추가로 갚아야 할 금액이다.

풀이 과정
    1. T를 입력받는다.
    2. T만큼 반복하며 N, M, money를 입력받는다.
    3. money를 정렬한다.
    4. M=2부터 N까지 반복하며
        4.1. prefix_sum을 0으로 초기화한다.
        4.2. 첫 구간(0~i)의 합을 계산한다.
        4.3. 첫 구간의 추가 금액을 계산한다.
        4.4. 구간을 이동하며 최소 추가 금액을 찾는다.
        4.5. S(i)를 더한다.
    5. 결과를 출력한다.

in
    3
    5 1 5 4 3 8
    3 1 2 3
    6 3 4 1 6 8 1
out
    30
    4
    51
'''

t = int(input())
for _ in range(t):
    n, *money = map(int, input().split())
    money.sort()  # 정렬하여 연속된 구간 처리
    res = 0  # S(M)의 합을 저장할 변수

    # M=2부터 N까지 반복 (M=1은 항상 0)
    for i in range(2, n+1):
        prefix_sum = 0
        # 첫 구간(0~i)의 합 계산
        for j in range(i):
            prefix_sum += money[j]
        # 첫 구간의 추가 금액 계산
        min_value = money[i-1] * i - prefix_sum

        # 구간을 이동하며 최소 추가 금액 찾기
        for j in range(i, n):
            # 구간 합 갱신
            prefix_sum = prefix_sum + money[j] - money[j-i]
            # 현재 구간의 추가 금액 계산 및 최소값 갱신
            new_value = (money[j] * i) - prefix_sum
            min_value = min(min_value, new_value)

        res += min_value  # S(i) 더하기

    print(res)
