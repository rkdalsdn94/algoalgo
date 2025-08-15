# 백준 - 실버4 - Pair Sum - 9728 - 자료 구조(해시), 투 포인터 문제
"""
자료 구조(해시), 투 포인터 문제

[핵심 아이디어]
    정렬된 배열에서 두 포인터(left, right)를 양 끝에서 시작하여 합이 목표값과 같으면 카운트, 작으면 left를 증가, 크면 right를 감소

[풀이 과정]
    1. 각 테스트 케이스마다 N과 M을 입력받는다
    2. 정렬된 배열을 입력받는다
    3. left 포인터는 0, right 포인터는 n - 1에서 시작한다
    4. arr[left] + arr[right]의 값에 따라 다음과 같이 처리
       - 합이 M과 같을 때: 카운트 증가하고 left++, right--
       - 합이 M보다 작을 때: left++ (더 큰 값이 필요)
       - 합이 M보다 클 때: right-- (더 작은 값이 필요)
    5. left < right 조건까지 반복하여 모든 쌍 확인
    6. 결과를 지정된 형식으로 출력

in
    5
    8 100
    19 25 32 48 52 68 75 81
    8 100
    19 28 31 49 51 61 72 81
    8 100
    16 22 38 46 58 62 73 81
    8 100
    13 21 32 48 52 67 78 87
    8 100
    13 24 34 43 57 61 76 81
out
    Case #1: 4
    Case #2: 3
    Case #3: 1
    Case #4: 2
    Case #5: 2
"""

t = int(input())

for case in range(1, t + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    left = 0
    right = n - 1
    count = 0

    # 투 포인터로 쌍의 개수 찾기
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == m:
            count += 1
            left += 1
            right -= 1
        elif current_sum < m:
            left += 1  # 더 큰 값이 필요하므로 왼쪽 포인터 이동
        else:
            right -= 1  # 더 작은 값이 필요하므로 오른쪽 포인터 이동

    print(f"Case #{case}: {count}")
