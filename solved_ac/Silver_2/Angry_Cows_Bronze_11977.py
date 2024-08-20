# 백준 - 실버2 - Angry Cows Bronze - 11977 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

풀이 과정
    1. 입력을 받는다.
    2. n_list를 정렬한다.
    3. res를 0으로 초기화한다.
    4. n만큼 반복문을 돌면서 current, radius, cnt를 초기화한다.
    5. temp를 만들어 왼쪽 계산을 한다.
        5.1. temp가 0보다 작거나 n_list[current] - n_list[temp]가 radius보다 크면 break한다.
        5.2. temp가 0보다 크고 n_list[current] - n_list[temp]가 radius보다 작거나 같을 때까지 반복한다.
        5.3. current를 temp + 1로 초기화하고, cnt에 1을 더한다.
    6. current, radius를 초기화한다.
    7. temp를 만들어 오른쪽 계산을 한다.
        7.1. temp가 n보다 크거나 n_list[temp] - n_list[current]가 radius보다 크면 break한다.
        7.2. temp가 n보다 작고 n_list[temp] - n_list[current]가 radius보다 작거나 같을 때까지 반복한다.
        7.3. current를 temp - 1로 초기화하고, cnt에 1을 더한다.
    8. res와 cnt 중 큰 값을 res에 저장한다.
'''

n = int(input())
n_list = sorted([int(input()) for _ in range(n)])

# 테스트
# n = 6
# n_list = sorted([8, 5, 6, 13, 3, 4]) # 5

res = 0

for i in range(n):
    current, radius, cnt = i, 1, 1
    temp = current - 1

    # 왼쪽 계산
    while 1:
        if temp < 0 or n_list[current] - n_list[temp] > radius:
            break

        while temp >= 0 and n_list[current] - n_list[temp] <= radius:
            temp -= 1
            cnt += 1

        current = temp + 1
        radius += 1

    current, radius = i, 1
    temp = current + 1

    # 오른쪽 계산
    while 1:
        if temp >= n or n_list[temp] - n_list[current] > radius:
            break

        while temp < n and n_list[temp] - n_list[current] <= radius:
            temp += 1
            cnt += 1

        current = temp - 1
        radius += 1

    res = max(res, cnt)

print(res)
