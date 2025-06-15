# 프로그래머스 - Lv2 - 퍼즐 게임 챌린지 - 이분 탐색, 시뮬레이션 문제
"""
이분 탐색, 시뮬레이션 문제

[핵심 아이디어]
    1. 숙련도가 높아질수록 총 소요 시간은 단조 감소하는 특성을 이용해 이분 탐색 적용
    2. 숙련도 범위는 1부터 max(diffs)까지로 설정 (그보다 높으면 모든 퍼즐을 한 번에 해결 가능)
    3. 각 숙련도에 대해 총 소요 시간을 계산하여 제한 시간과 비교

[풀이 과정]
    1. 이분 탐색의 left=1, right=max(diffs)로 초기화
    2. mid 숙련도에 대해 총 소요 시간을 계산하는 함수 작성:
       - diff ≤ level이면 time_cur만 소요
       - diff > level이면 (time_cur + time_prev) × (diff - level) + time_cur 소요
    3. 총 소요 시간이 limit 이하이면 right = mid, 초과하면 left = mid + 1
    4. left == right가 될 때까지 반복하여 최소 숙련도 반환
"""

def solution(diffs, times, limit):
    def calculate_time(level):
        """주어진 숙련도로 모든 퍼즐을 푸는데 걸리는 총 시간 계산"""
        total_time = 0

        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1] if i > 0 else 0

            if diff <= level:
                # 틀리지 않고 한 번에 해결
                total_time += time_cur
            else:
                # (diff - level)번 틀림
                mistakes = diff - level
                # 틀릴 때마다 time_cur + time_prev, 마지막에 time_cur
                total_time += (time_cur + time_prev) * mistakes + time_cur

        return total_time

    left, right = 1, max(diffs)
    answer = right  # 최악의 경우를 초기값으로 설정
    while left <= right:
        mid = (left + right) // 2

        if calculate_time(mid) <= limit:
            # 제한 시간 내에 해결 가능하므로 답을 갱신하고 더 낮은 숙련도 탐색
            answer = mid
            right = mid - 1
        else:
            # 제한 시간 초과하므로 더 높은 숙련도 필요
            left = mid + 1

    return answer

print(solution([1, 5, 3], [2, 4, 7], 30))  # 3
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))  # 2
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))  # 294
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))  # 39354
