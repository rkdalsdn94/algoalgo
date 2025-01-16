# 백준 - 브론즈2 - 집에선 안돼잉 - 29734 - 수학, 구현, 사칙연산 문제
'''
수학, 구현, 사칙연산 문제

핵심 아이디어
    - 집에서 공부하는 경우와 독서실에서 공부하는 경우를 비교하여 최소 시간을 출력한다.
    - 집에서 공부하는 경우: N + (N // 8) * S
    - 독서실에서 공부하는 경우: T + M + (M // 8) * (2 * T + S)

풀이 과정
    1. N, M, T, S를 입력받는다.
    2. 집에서 공부하는 경우와 독서실에서 공부하는 경우를 계산한다.
    3. 최소 시간을 출력한다.
'''

N, M = map(int, input().split())  # N: 집에서 걸리는 시간, M: 독서실에서 걸리는 시간
T, S = map(int, input().split())  # T: 이동 시간, S: 수면 시간

# 테스트
# N, M = 35, 24
# T, S = 4, 8 # Dok  \  60
# N, M = 24, 20
# T, S = 4, 8 # Zip  \  40

# 집에서 공부하는 경우 총 소요 시간 계산
home_sleep_count = (N - 1) // 8  # 8시간마다 필요한 수면 횟수
home_total = N + (home_sleep_count * S)

# 독서실에서 공부하는 경우 총 소요 시간 계산
study_segments = (M - 1) // 8  # 8시간 단위로 나누기
library_total = T + M + (study_segments * (2 * T + S))  # 첫 이동 + 공부 시간 + (세그먼트당 왕복 이동 및 수면)

if library_total < home_total:
    print("Dok")
    print(library_total)
else:
    print("Zip")
    print(home_total)
