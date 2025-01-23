# 백준 - 골드5 - Lecture Halls Reservation - 8098 - dp, 정렬 문제
'''
dp, 정렬 문제

핵심 아이디어
    - 강의를 종료 시간을 기준으로 정렬합니다.
    - dp[i]는 lectures[0...i]까지 고려했을 때 가능한 최대 강의 시간을 의미합니다.
    - 각 강의에 대해 두 가지 선택지가 있습니다:
        1. 현재 강의를 포함하고 겹치지 않는 이전 강의들과 결합
        2. 현재 강의를 제외하고 이전까지의 최대값 사용
    - dp[i] = max(include_current, exclude_current)로 갱신합니다.

풀이 과정
    1. 테스트 케이스의 수 T를 입력받습니다.
    2. 각 테스트 케이스에 대해:
        2.1. 강의 수 N을 입력받습니다.
        2.2. 각 강의의 시작 시간과 종료 시간을 입력받습니다.
        2.3. 강의를 종료 시간을 기준으로 정렬합니다.
        2.4. dp[i]는 lectures[0...i]까지 고려했을 때 가능한 최대 강의 시간을 의미합니다.
        2.5. dp[i] = max(include_current, exclude_current)로 갱신합니다.
    3. 결과를 출력합니다.
'''

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 12
# lectures = [
#     [1, 2], [3, 5], [0, 4], [6, 8], [7, 13],
#     [4, 6], [9, 10], [9, 12], [11, 14], [15, 19],
#     [14, 16], [18, 20]
# ] # 16

def find_max_lecture_time(lectures):
    # 강의를 종료 시간을 기준으로 정렬
    lectures.sort(key=lambda x: x[1])
    n = len(lectures)

    # dp[i]는 lectures[0...i]까지 고려했을 때 가능한 최대 강의 시간을 의미
    dp = [0] * n

    # 기본 케이스: 첫 번째 강의 시간
    dp[0] = lectures[0][1] - lectures[0][0]

    # 각 강의에 대해 두 가지 선택지가 있음:
    # 1. 현재 강의를 포함하고 겹치지 않는 이전 강의들과 결합
    # 2. 현재 강의를 제외하고 이전까지의 최대값 사용
    for i in range(1, n):
        # 현재 강의 시간
        duration = lectures[i][1] - lectures[i][0]

        # 겹치지 않는 가장 최근의 강의 찾기
        last_valid = -1
        for j in range(i-1, -1, -1):
            if lectures[j][1] <= lectures[i][0]:
                last_valid = j
                break

        # 현재 강의 포함하기
        if last_valid != -1:
            include_current = dp[last_valid] + duration
        else:
            include_current = duration

        # 현재 강의 제외하기
        exclude_current = dp[i-1]

        # 현재 강의를 포함하는 경우와 제외하는 경우 중 최대값 선택
        dp[i] = max(include_current, exclude_current)

    return dp[n-1]


res = find_max_lecture_time(lectures)
print(res)
