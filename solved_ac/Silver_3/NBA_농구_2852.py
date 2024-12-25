# 백준 - 실버3 - NBA 농구 - 2852 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
1. 시간의 표현과 초기화
   - 모든 시간을 초 단위로 변환 (MM:SS → 초)
   - 각 팀의 리드 시간을 0으로 초기화
2. 득점 상황 분석
   - 각 득점마다 팀의 누적 득점 기록
   - 이전 시간부터 현재 시간까지:
     * 한 팀이 이기고 있었다면 해당 팀의 리드 시간에 추가
     * 동점이었다면 어느 팀의 시간에도 추가하지 않음
3. 시간 계산의 주요 시점
   - 경기 시작(0:00)부터 첫 득점까지
   - 각 득점 사이의 시간
   - 마지막 득점부터 경기 종료(48:00)까지
4. 결과 출력
   - 각 팀의 리드 시간을 MM:SS 형식으로 변환
   - 분과 초가 한 자리 수인 경우 앞에 0을 붙여 출력 (zfill 사용)

in
    1
    1 20:00
out
    28:00
    00:00

in
    3
    1 01:10
    2 21:10
    2 31:30
out
    20:00
    16:30

in
    5
    1 01:10
    1 02:20
    2 45:30
    2 46:30
    2 47:50
out
    45:30
    00:10
'''

n = int(input())
scores = []
for _ in range(n):
    team, time = input().split()
    m, s = map(int, time.split(':'))
    scores.append((int(team), m * 60 + s))  # 시간을 초 단위로 변환

team1_time = 0  # 1번 팀이 이기고 있던 시간 (초)
team2_time = 0  # 2번 팀이 이기고 있던 시간 (초)
team1_score = 0  # 1번 팀의 득점 수
team2_score = 0  # 2번 팀의 득점 수
prev_time = 0    # 이전 시점 (초)

# 각 득점 시점마다 처리
for curr_team, curr_time in scores:
    # 이전 시간부터 현재 시간까지의 간격 계산
    time_diff = curr_time - prev_time

    # 이전 구간의 점수 차이에 따라 시간 할당
    if team1_score > team2_score:
        team1_time += time_diff
    elif team2_score > team1_score:
        team2_time += time_diff

    # 현재 득점 반영
    if curr_team == 1:
        team1_score += 1
    else:
        team2_score += 1

    prev_time = curr_time

# 마지막 득점부터 경기 종료(48분 = 2880초)까지 처리
final_time_diff = 48 * 60 - prev_time
if team1_score > team2_score:
    team1_time += final_time_diff
elif team2_score > team1_score:
    team2_time += final_time_diff

# MM:SS 형식으로 변환하여 출력
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f'{str(minutes).zfill(2)}:{str(seconds).zfill(2)}'

print(format_time(team1_time))
print(format_time(team2_time))
