# 프로그래머스 - Lv1 - 동영상 재생기 - 구현, 시뮬레이션, 문자열 문제
'''
구현, 시뮬레이션, 문자열 문제

[핵심 아이디어]
    1. 시간 형식("mm:ss")을 초 단위로 변환하여 계산을 단순화
    2. 각 명령어에 따른 위치 이동 처리
    3. 매 명령어 실행 후 오프닝 구간 체크
    4. 최종 위치를 다시 "mm:ss" 형식으로 변환

[풀이 과정]
    1. 입력받은 모든 시간 문자열을 초 단위로 변환
    2. 현재 위치가 오프닝 구간인지 확인하고, 맞다면 오프닝 종료 위치로 이동
    3. 각 명령어 처리:
       - prev: 10초 이전으로 이동 (0초 미만이면 0초로)
       - next: 10초 이후로 이동 (영상 길이 초과시 마지막으로)
    4. 명령어 실행 후 오프닝 구간 체크
    5. 최종 위치를 "mm:ss" 형식으로 변환하여 반환
'''

def solution(video_len, pos, op_start, op_end, commands):
    def time_to_seconds(time_str):
        """시간 문자열을 초 단위로 변환"""
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds

    def seconds_to_time(seconds):
        """초 단위를 시간 문자열로 변환"""
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    # 모든 시간을 초 단위로 변환
    video_len = time_to_seconds(video_len)
    pos = time_to_seconds(pos)
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)

    # 초기 위치가 오프닝 구간인 경우 처리
    if op_start <= pos <= op_end:
        pos = op_end

    # 명령어 처리
    for command in commands:
        if command == 'prev':
            pos = max(0, pos - 10)
        else:  # command == 'next'
            pos = min(video_len, pos + 10)

        # 오프닝 구간 체크
        if op_start <= pos <= op_end:
            pos = op_end

    return seconds_to_time(pos)

print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"])) # "13:00"
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"])) # "06:55"
print(solution("07:22", "04:05", "00:15", "04:07", ["next"])) # "04:17"
