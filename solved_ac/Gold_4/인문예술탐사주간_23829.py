# 백준 - 골드4 - 인문예술탐사주간 - 23829 - 이진 탐색, 누적 합 문제
'''
이진 탐색, 누적 합 문제

핵심 아이디어
    - 나무의 위치를 정렬하여 이진 탐색을 수행
    - 사진 위치에 대해 점수를 계산

풀이 과정
    1. N, Q를 입력받는다.
    2. 나무 위치를 입력받는다.
    3. 사진 위치를 입력받는다.
    4. 누적합을 계산한다.
    5. 사진 위치에 대해 점수를 계산한다.
    6. 결과 출력
'''

from bisect import bisect_right

def calculate_score(trees, prefix_sum, photo_pos, N):
    # photo_pos보다 작거나 같은 값의 위치를 찾음
    idx = bisect_right(trees, photo_pos)

    # 왼쪽 나무들까지의 거리 합: (개수 * 현재위치) - (왼쪽 나무들의 위치 합)
    left_sum = idx * photo_pos - prefix_sum[idx]

    # 오른쪽 나무들까지의 거리 합: (오른쪽 나무들의 위치 합) - (개수 * 현재위치)
    right_sum = (prefix_sum[N] - prefix_sum[idx]) - (N - idx) * photo_pos

    return left_sum + right_sum

N, Q = map(int, input().split())
trees = sorted(list(map(int, input().split()))) # 이진 탐색을 위해 정렬
q_list = [int(input()) for _ in range(Q)]

# 테스트
# N, Q = 5, 2
# trees = sorted([1, 3, 7, 9, 10])
# q_list = [4, 12] # 18  \  30

# 누적합 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + trees[i - 1]

# 각 사진 위치에 대해 점수 계산
for photo_pos in q_list:
    score = calculate_score(trees, prefix_sum, photo_pos, N)
    print(score)
