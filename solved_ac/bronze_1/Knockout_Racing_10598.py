# 백준 - 브론즈1 - Knockout Racing - 10598 - 수학, 구현 문제
"""
수학, 구현 문제

[핵심 아이디어]
    1. 차량은 a -> b -> a 순서로 왕복 운동 (거리 1/초)
    2. 왕복 주기 = 2 × |b - a| 초
    3. 시간 t를 주기로 나눈 나머지로 현재 위치 계산
    4. 나머지 <= 거리면 전진, 나머지 > 거리면 후진

[풀이 과정]
    1. 각 차량의 시간 t에서 위치 계산:
       - 거리 d = |b - a|
       - 나머지 r = t % (2d)
       - r <= d이면 시작점에서 r만큼 이동
       - r > d이면 끝점에서 (r-d)만큼 되돌아옴
    2. 범위 [x, y] 내 차량 개수 카운트
"""

def get_position(a, b, t):
    """시간 t에서 차량 위치 계산"""
    if a == b:
        return a

    dist = abs(b - a)
    remainder = t % (2 * dist)

    if remainder <= dist:
        # 전진: a에서 b 방향으로
        return a + remainder if a < b else a - remainder
    else:
        # 후진: b에서 a 방향으로
        back = remainder - dist
        return b - back if a < b else b + back

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
m_list = [list(map(int, input().split())) for _ in range(m)]

# 테스트
# n, m = 5, 5
# n_list = [[0, 1], [0, 2], [2, 3], [3, 5], [4, 5]]
# m_list = [[0, 5, 0], [0, 1, 2], [0, 2, 1], [2, 5, 2], [2, 5, 3]] # 5  \  1  \  2  \  4  \  3

for x, y, t in m_list:
    count = 0

    for a, b in n_list:
        pos = get_position(a, b, t)

        if x <= pos <= y:
            count += 1

    print(count)
