# 백준 - 브론즈2 - Cooking Water - 17924 - 구현, 완전 탐색 문제
'''
구현, 완전 탐색 문제

[핵심 아이디어]
    1. 모든 관찰 구간에 공통으로 포함되는 시간이 존재하는지를 확인하는 것이 핵심
    2. 각 구간 [a,b]는 Edward가 물이 끓는 것을 보지 못한 시간을 의미
    3. 만약 물이 항상 같은 시간에 끓기 시작한다면, 그 시간은 반드시 모든 관찰 구간에 포함되어야 함
    4. 이를 판단하기 위해 가장 늦은 시작점과 가장 이른 끝점을 비교

[풀이 과정]
    1. 입력 처리
      - 관찰 횟수 n을 입력받습니다.
      - n개의 구간을 입력받아 리스트로 저장합니다.
    2. 구간 분석
      - 모든 구간의 시작점 중 가장 늦은 시작점(latest_start)을 찾습니다.
      - 모든 구간의 끝점 중 가장 이른 끝점(earliest_end)을 찾습니다.
    3. 결과 판단
      - latest_start ≤ earliest_end이면 모든 구간에 공통 시간이 존재하므로 "gunilla has a point" 출력
      - latest_start > earliest_end이면 공통 시간이 존재하지 않으므로 "edward is right" 출력
'''

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

# 테스트
# n = 2
# n_list = [[1, 7], [5, 5]] # gunilla has a point
# n = 3
# n_list = [[4, 6], [4, 8], [7, 8]] # edward is right

# 가장 늦은 시작 시간과 가장 이른 종료 시간 찾기
latest_start = max(interval[0] for interval in n_list)
earliest_end = min(interval[1] for interval in n_list)

# 모든 구간에 공통으로 포함되는 시간이 존재하는지 확인
# 존재한다면 latest_start가 earliest_end보다 작거나 같아야 함
if latest_start <= earliest_end:
    print("gunilla has a point")  # 구닐라의 가설이 맞을 수 있음
else:
    print("edward is right")      # 에드워드가 맞음
