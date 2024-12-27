# 백준 - 브론즈1 - Countdown - 5122 - 구현 문제
'''
구현 문제

단순하게 MLC 날짜를 일수로 변환하여 계산하는 문제

풀이 과정
  1. mlc_to_days(): MLC 날짜를 일수로 변환
    - 각 자릿수를 해당하는 단위(144000, 7200, 360, 20, 1)와 곱하여 합산
  2. solve_case(): 각 테스트 케이스 해결
    - MLC 날짜를 일수로 변환
    - 세계 종말일(13.0.0.0.0 MLC)까지의 일수 계산
    - 주어진 astronomical event의 JDN을 기준으로 세계 종말일의 JDN 계산
    - 현재 날짜(2456054 JDN)와의 차이를 계산하여 결과 출력
  3. 메인 로직
    - 테스트 케이스 수 입력
    - 각 케이스마다 MLC 날짜와 JDN 입력받아 처리
'''

def mlc_to_days(mlc):
    # MLC를 일수로 변환 (base-20, 두 번째 자리는 base-18)
    days = mlc[0] * 144000  # 20*18*20*20
    days += mlc[1] * 7200   # 18*20*20
    days += mlc[2] * 360    # 20*18
    days += mlc[3] * 20     # 20
    days += mlc[4]          # 1
    return days

def solve_case(case_num, mlc_date, jdn):
    # MLC 날짜를 일수로 변환
    mlc_days = mlc_to_days(mlc_date)

    # 세계 종말일(13.0.0.0.0 MLC)까지의 일수 계산
    end_days = mlc_to_days([13, 0, 0, 0, 0])

    # 현재 JDN과 세계 종말 JDN 계산
    current_jdn = 2456054  # 5/6/2012 G
    end_jdn = jdn + (end_days - mlc_days)

    # 남은 일수 계산
    days_left = end_jdn - current_jdn

    print(f"Data Set {case_num}:")
    if days_left < 0:
        print("It's a hoax!")
    elif days_left == 0:
        print("Panic!")
    else:
        print(days_left)
    print()

K = int(input())
for i in range(K):
    mlc = list(map(int, input().split()))
    jdn = int(input())
    solve_case(i + 1, mlc, jdn)
