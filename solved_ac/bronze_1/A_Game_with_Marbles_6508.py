# 백준 - 브론즈1 - A Game with Marbles - 6508 - 구현, 사칙연산, 시뮬레이션 문제
"""
구현, 사칙연산, 시뮬레이션 문제

[핵심 아이디어]
    1. 가장 큰 번호의 그릇부터 처리하는 것이 최적 전략임
    2. i번 그릇에서 구슬을 제거할 때마다 1~(i-1)번 그릇에 구슬이 하나씩 추가됨
    3. 그릇에 있는 모든 구슬을 제거할 때까지 게임이 진행됨
    4. 각 그릇의 구슬 제거가 이전 그릇들에 미치는 영향을 누적해서 계산

[풀이 과정]
    1. 큰 번호의 그릇(n)부터 작은 번호(1)까지 순차적으로 처리
    2. 각 그릇에서 구슬을 제거할 때마다 필요한 단계(steps) 카운트
    3. 구슬 제거 후 이전 그릇들에 추가되는 구슬 수를 업데이트
    4. 모든 그릇을 처리한 후 총 단계 수 출력

in
    10
    3 3 3 3 3 3 3 3 3 3
    5
    1 2 3 4 5
    0
out
    3069
    129
"""

while True:
    n = int(input())
    if n == 0:
        break

    marbles = list(map(int, input().split()))
    steps = 0

    # n번 그릇부터 1번 그릇까지 처리
    for i in range(n-1, -1, -1):
        current_marbles = marbles[i]
        steps += current_marbles  # 현재 그릇의 구슬을 모두 제거하는 단계 수

        # 1번보다 큰 그릇이면 이전 그릇에 구슬 추가
        if i > 0:
            for j in range(i):
                marbles[j] += current_marbles

    print(steps)
