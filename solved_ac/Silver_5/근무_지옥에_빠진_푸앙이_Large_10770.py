# 백준 - 실버5 - 근무 지옥에 빠진 푸앙이 Large - 25584 - 구현, 자료구조(해시), 문자열 문제
"""
구현, 자료구조(해시), 문자열 문제

[핵심 아이디어]
    1. 각 사람별로 총 근무 시간을 계산하기 위해 딕셔너리(해시맵) 사용
    2. 4개 시간대별로 다른 근무 시간(4, 6, 4, 10시간)을 적용하여 누적
    3. 최대 근무 시간과 최소 근무 시간의 차이가 12시간 이하인지 확인

[풀이 과정]
    1. 각 주마다 4개의 시간대(08:00~12:00, 12:00~18:00, 18:00~22:00, 22:00~08:00)에 대해 근무자를 확인
    2. 각 근무자별로 해당 시간대의 근무 시간(4, 6, 4, 10시간)을 딕셔너리에 누적
    3. 모든 근무자의 근무 시간 중 최대값과 최소값을 구함
    4. 차이가 12시간 이하면 공평("Yes"), 초과하면 불공평("No")
    5. 아무도 근무하지 않으면 공평한 것으로 간주("Yes")

in
    4
    - - - - - pangyo puang
    - - - - - sally boss
    - - - - - leonard brown
    - - - - - edward edward
    puang pangyo choco leonard cony leonard choco
    cony edward cony leonard moon puang edward
    choco boss puang brown brown pangyo cony
    choco edward puang cony moon choco boss
    brown moon moon sally pangyo puang choco
    pangyo edward boss sally moon cony pangyo
    brown puang james moon cony choco choco
    sally brown sally puang james moon sally
    leonard pangyo - - - - -
    boss choco - - - - -
    moon edward - - - - -
    moon sally - - - - -
out
    No

in
    4
    - - - - - sally boss
    - - - - - brown boss
    - - - - - moon sally
    - - - - - leonard edward
    pangyo moon cony boss james sally brown
    moon brown sally cony brown choco edward
    moon leonard pangyo moon edward puang puang
    leonard sally boss choco cony boss edward
    brown sally jessica leonard moon jessica james
    jessica brown leonard puang james pangyo puang
    puang choco james cony jessica pangyo jessica
    pangyo jessica choco james puang cony pangyo
    moon moon james choco edward - -
    jessica brown james sally puang - -
    cony leonard moon boss choco - -
    edward jessica cony brown leonard - -
out
    Yes
"""

n = int(input())
work_hours = {}  # 각 사람별 총 근무 시간을 저장할 딕셔너리
time_slots = [4, 6, 4, 10]  # 각 시간대별 근무 시간

for week in range(n):
    for time_slot in range(4):
        line = input().split()
        for person in line:
            if person != '-':  # 근무자가 있는 경우
                if person not in work_hours:
                    work_hours[person] = 0
                work_hours[person] += time_slots[time_slot]

# 아무도 근무하지 않는 경우
if not work_hours:
    print("Yes")
else:
    max_hours = max(work_hours.values())
    min_hours = min(work_hours.values())

    # 최대 근무 시간과 최소 근무 시간의 차이가 12시간 이하인지 확인
    if max_hours - min_hours <= 12:
        print("Yes")
    else:
        print("No")
