# 프로그래머스 - Lv2 - 택배 배달과 수거하기 - 그리디, 투 포인터 문제
"""
그리디, 투 포인터 문제

이해가 잘 안된다면 다음의 영상을 참고하자. (설명이 엄청 좋음)
    - https://www.youtube.com/watch?v=Ie3lvbTylJo

[핵심 아이디어]
    1. 가장 먼 집부터 배달과 수거를 동시에 고려
    2. 각 집에서 필요한 배달과 수거량을 누적
    3. 누적된 배달 또는 수거량이 용량(cap)을 초과할 때마다 왕복 거리 추가
    4. 모든 집을 처리할 때까지 반복

[풀이 과정]
    1. 가장 먼 집부터 시작하여 배달과 수거량을 누적
    2. 누적된 배달 또는 수거량이 용량(cap)을 초과하면 현재 집까지의 왕복 거리(2 * (i + 1))를 답에 추가하고 누적량 초기화
    3. 모든 집을 처리할 때까지 반복
"""

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_cap = 0
    p_cap = 0

    for i in range(n-1, -1, -1):
        d_cap += deliveries[i]
        p_cap += pickups[i]

        while d_cap > 0 or p_cap > 0:
            answer += (i + 1) * 2
            d_cap -= cap
            p_cap -= cap

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]) == 16)
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]) == 30)
