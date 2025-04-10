# 프로그래머스 - 연속된 부분 수열의 합 - 투 포인터, 슬라이딩 윈도우 문제
"""
투 포인터, 슬라이딩 윈도우 문제

[핵심 아이디어]
    1. 두 개의 포인터(left, right)를 사용해 연속된 부분 수열을 표현
    2. 현재 부분 수열의 합이 k보다 작으면 right를 증가시켜 윈도우 확장
    3. 현재 부분 수열의 합이 k보다 크거나 같으면 left를 증가시켜 윈도우 축소
    4. 합이 k인 모든 부분 수열을 찾아서 길이가 짧고 시작 인덱스가 작은 것을 선택

[풀이 과정]
    1. left와 right 포인터를 0으로 초기화하고 현재 합(current_sum)을 sequence[0]으로 설정
    2. right 포인터를 오른쪽으로 이동시키며 합이 k 이상이 될 때까지 윈도우 확장
    3. 합이 k와 같으면 현재 부분 수열 [left, right]를 정답 후보로 저장
    4. left 포인터를 오른쪽으로 이동시키며 합이 k 미만이 될 때까지 윈도우 축소
    5. 이 과정을 반복하여 모든 가능한 부분 수열 중 길이가 가장 짧고 시작 인덱스가 가장 작은 것 선택
"""

def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    min_length = float('inf')
    result = []

    while True:
        if current_sum == k:
            # 합이 k인 부분 수열을 찾았을 때
            length = right - left + 1
            if length < min_length:
                min_length = length
                result = [left, right]

        if current_sum <= k:
            # 합이 k보다 작거나 같으면 right 포인터 이동
            right += 1
            if right >= len(sequence):
                break
            current_sum += sequence[right]
        else:
            # 합이 k보다 크면 left 포인터 이동
            current_sum -= sequence[left]
            left += 1
            if left > right:
                # left가 right를 넘어서면 right도 함께 이동
                right = left
                if right >= len(sequence):
                    break
                current_sum = sequence[right]

    return result

print(solution([1, 2, 3, 4, 5], 7) == [2, 3])
print(solution([1, 1, 1, 2, 3, 4, 5], 5) == [6, 6])
print(solution([2, 2, 2, 2, 2], 6) == [0, 2])
