# 백준 - 브론즈1 - Average Speed - 4366 - 수학, 구현, 문자열, 사칙연산, 파싱 문제
'''
수학, 구현, 문자열, 사칙연산, 파싱 문제

[문제 해석]
1. 시간과 속도를 입력받아 이동 거리를 계산하는 문제
2. 시간은 시:분:초로 주어지며, 속도는 km/h로 주어진다.
3. 이동 거리는 시간과 속도를 곱한 값으로 계산한다.

[해결 방법]
1. 시간을 초 단위로 변환하는 함수를 작성한다.
2. 이동 거리를 소수점 2자리까지 출력하는 함수를 작성한다.
3. 입력을 받아 이동 거리를 계산하고 출력한다.
'''

def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def format_distance(distance):
    return f"{distance:.2f} km"

total_distance = 0
prev_time = 0
current_speed = 0

while True:
    try:
        data = input().split()
        current_time = time_to_seconds(data[0])

        # 이동 거리 계산
        time_diff = current_time - prev_time
        distance = (time_diff / 3600) * current_speed
        total_distance += distance

        if len(data) == 2:  # 속도 변경
            current_speed = int(data[1])
        else:  # 쿼리
            print(f"{data[0]} {format_distance(total_distance)}")

        prev_time = current_time

    except EOFError:
        break
