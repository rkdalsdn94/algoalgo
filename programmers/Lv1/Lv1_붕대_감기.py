# 프로그래머스 - Lv1 - 붕대 감기 - 구현, 시뮬레이션 문제
"""
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 시간순으로 캐릭터의 상태를 시뮬레이션하여 체력 변화를 추적
    2. 붕대 감기 연속 성공 시간을 카운트하여 추가 회복 조건 확인
    3. 공격 시간을 딕셔너리로 변환하여 빠르게 검색 가능하도록 함
    4. 모든 시간에 대해 공격 여부를 확인하고 체력 변화를 적용

[풀이 과정]
    1. 붕대 감기 정보(시전 시간, 초당 회복량, 추가 회복량)와 최대 체력을 변수에 저장
    2. 마지막 공격 시간까지 시뮬레이션을 진행
    3. 각 시간마다:
       - 공격이 없는 경우: 연속 성공 시간 증가, 체력 회복
       - 연속 성공 시간이 시전 시간에 도달하면 추가 회복 적용 후 초기화
       - 공격이 있는 경우: 피해량만큼 체력 감소, 연속 성공 시간 초기화
    4. 매 순간 체력이 최대 체력을 넘지 않도록 조정하고, 0 이하가 되면 -1 반환
    5. 모든 공격이 끝난 후 남은 체력 반환
"""

def solution(bandage, health, attacks):
    max_health = health  # 최대 체력
    current_health = health  # 현재 체력
    cast_time, heal_per_sec, bonus_heal = bandage  # 붕대 감기 정보

    # 공격 시간을 키로, 피해량을 값으로 하는 딕셔너리 생성
    attack_dict = {time: damage for time, damage in attacks}

    # 마지막 공격 시간
    last_attack_time = attacks[-1][0]

    # 연속 성공 시간
    consecutive_success = 0

    # 시뮬레이션 시작
    for current_time in range(1, last_attack_time + 1):
        # 현재 시간에 공격이 있는지 확인
        if current_time in attack_dict:
            # 공격 받음: 체력 감소, 연속 성공 초기화
            current_health -= attack_dict[current_time]
            consecutive_success = 0

            # 체력이 0 이하면 캐릭터 사망
            if current_health <= 0:
                return -1
        else:
            # 공격 없음: 체력 회복, 연속 성공 증가
            consecutive_success += 1
            current_health += heal_per_sec

            # 연속 성공 시간이 시전 시간에 도달하면 추가 회복
            if consecutive_success == cast_time:
                current_health += bonus_heal
                consecutive_success = 0  # 연속 성공 초기화

            # 최대 체력 제한
            if current_health > max_health:
                current_health = max_health

    return current_health
