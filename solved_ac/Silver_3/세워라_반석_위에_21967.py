# 백준 - 실버3 - 세워라 반석 위에 - 21967 - 완전 탐색, 투 포인터 문제
'''
완전 탐색, 투 포인터 문제

[핵심 아이디어]
    슬라이딩 윈도우 기법을 사용하여 시간 복잡도를 개선한다.
    각 숫자의 빈도수를 카운트하여 최댓값과 최솟값을 O(1)로 찾을 수 있게 한다.
    현재 윈도우에 존재하는 숫자들 중 최댓값과 최솟값의 차이가 2를 초과하면
    left 포인터를 이동시켜 윈도우를 조절한다.

[풀이 과정]
    1. 숫자의 빈도수를 저장할 배열(count)을 생성한다.
    2. right 포인터를 이동하면서:
       - 현재 숫자의 빈도수를 증가시킨다
       - 빈도수가 있는 숫자들 중 최댓값과 최솟값을 확인한다
       - 차이가 2를 초과하면 left 포인터를 이동하며 빈도수를 감소시킨다
    3. 조건을 만족하는 구간의 길이를 갱신한다
'''

N = int(input())
A = list(map(int, input().split()))

# 테스트
# N = 5
# A = [1, 2, 1, 3, 1] # 5
# N = 7
# A = [1, 2, 3, 4, 2, 5, 7] # 4

left = 0
right = 0
count = [0] * 11  # 숫자의 범위가 1 ~ 10이므로
max_length = 0

while right < N:
    count[A[right]] += 1

    # 현재 윈도우에서 최소/최대값 찾기
    min_val = 1
    while min_val <= 10 and count[min_val] == 0:
        min_val += 1

    max_val = 10
    while max_val >= 1 and count[max_val] == 0:
        max_val -= 1

    # 조건을 만족하지 않으면 left 포인터 이동
    while max_val - min_val > 2:
        count[A[left]] -= 1
        left += 1

        min_val = 1
        while min_val <= 10 and count[min_val] == 0:
            min_val += 1

        max_val = 10
        while max_val >= 1 and count[max_val] == 0:
            max_val -= 1

    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)
