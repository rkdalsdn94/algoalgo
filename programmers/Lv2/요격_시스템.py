# 프로그래머스 - Lv2 - 요격 시스템 - 그리디 문제
"""
그리디 문제

[핵심 아이디어]
    구간들을 끝점 기준으로 정렬한 후, 가장 빨리 끝나는 구간부터 처리하여 하나의 요격 미사일로 최대한 많은 구간을 커버하는 그리디 전략 사용

[풀이 과정]
    1. targets를 끝점(e) 기준으로 오름차순 정렬
    2. 첫 번째 구간의 끝점 직전(e - 0.5)에서 요격 미사일 발사
    3. 현재 요격 위치로 처리할 수 없는 구간 중 가장 빨리 끝나는 구간 찾기
    4. 새로운 요격 미사일을 해당 구간의 끝점 직전에서 발사
    5. 모든 구간을 처리할 때까지 반복
"""

def solution(targets):
    # 끝점 기준으로 정렬
    targets.sort(key=lambda x: x[1])

    missile_count = 0
    intercept_position = 0  # 현재 요격 미사일 위치

    for start, end in targets:
        # 현재 구간이 이전 요격 미사일로 처리되지 않는 경우
        if start >= intercept_position:
            missile_count += 1
            # 구간의 끝점 직전에서 요격 (개구간이므로 end는 포함되지 않음)
            intercept_position = end

    return missile_count

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	) == 3)
