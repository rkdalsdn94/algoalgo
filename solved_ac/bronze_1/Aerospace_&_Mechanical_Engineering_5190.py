# 백준 - 브론즈1 - Aerospace & Mechanical Engineering - 5190 - 수학, 구현 문제
"""
수학, 구현 문제

[핵심 아이디어]
    1. 로켓은 여러 단계(stage)로 구성되어 있으며, 각 단계마다 무게, 지속 시간, 추력이 다름
    2. 단계가 끝날 때마다 해당 단계의 무게가 버려지므로 로켓이 가벼워짐
    3. 로켓의 가속도는 (추력/질량) - 중력가속도로 계산
    4. 각 단계마다 속도와 높이의 변화를 계산하여 최종 높이를 구함

[풀이 과정]
    1. 각 로켓 단계를 순서대로 처리
    2. 각 단계에서:
       - 현재 질량(로켓 + 남은 단계들의 무게) 계산
       - 순 가속도(추력/질량 - 중력가속도) 계산
       - 이 단계 동안의 속도와 높이 변화 계산
       - 다음 단계를 위해 속도와 높이 갱신
    3. 마지막 단계가 끝날 때의 높이 반환
"""

def solve_rocket(n, M, stages):
    g = 9.81  # 중력 가속도 (m/s^2)

    # 초기값 설정
    height = 0.0  # 초기 높이
    velocity = 0.0  # 초기 속도

    # 각 단계 처리
    for i in range(n):
        m_i, t_i, F_i = stages[i]

        # 현재 단계에서의 로켓 총 질량 계산
        current_mass = M
        # i번째 단계와 그 이후의 단계들의 질량을 추가
        for j in range(i, n):
            current_mass += stages[j][0]

        # 순 가속도 계산 (추력/질량 - 중력가속도)
        acceleration = F_i / current_mass - g

        # 이 단계 동안의 높이 변화 계산: v*t + 0.5*a*t^2
        height_change = velocity * t_i + 0.5 * acceleration * t_i * t_i

        # 높이 갱신
        height += height_change

        # 속도 갱신: v + a*t
        velocity += acceleration * t_i

    # 최종 높이 반환 (소수점 둘째 자리까지 반올림)
    return round(height, 2)

T = int(input())
for case in range(1, T + 1):
    line = input().split()
    n = int(line[0])  # 단계 수
    M = float(line[1])  # 로켓 본체 무게

    stages = []
    for _ in range(n):
        m_i, t_i, F_i = map(float, input().split())
        stages.append((m_i, t_i, F_i))

    result = solve_rocket(n, M, stages)
    print(f"Data Set {case}:")
    print(f"{result:.2f}")
