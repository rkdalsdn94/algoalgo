# 백준 - 브론즈1 - Take Your Vitamins - 4749 - 구현, 문자열, 파싱, 수학 문제
"""
구현, 문자열, 파싱, 수학 문제

[핵심 아이디어]
    1. 입력 문자열을 적절히 파싱하여 양(A), 단위(U), 권장량(R), 비타민명(V) 추출
    2. 백분율 계산: (A / R) × 100
    3. 1% 이상인 것과 미만인 것을 구분하여 저장
    4. 지정된 형식에 맞춰 출력 (A는 소수점 1자리, P는 정수)

[풀이 과정]
    1단계: 입력 파싱
      - 한 줄을 공백으로 분리 (split)
      - 첫 3개 토큰은 A, U, R이고, 나머지 전체가 비타민명 V
      - V는 공백을 포함할 수 있으므로 join으로 결합
    2단계: 백분율 계산 및 분류
      - percentage = (A / R) * 100 계산
      - 1% 이상이면 significant 리스트에 추가
      - 1% 미만이면 insignificant 리스트에 추가
    3단계: 결과 출력
      - significant 리스트: "비타민명 양 단위 백분율%" 형식으로 출력
      - "Provides no significant amount of:" 출력
      - insignificant 리스트: 비타민명을 한 줄씩 출력

in
    3500.0 iu 5000.0 Vitamin A
    60.0 mg 60.0 Vitamin C
    0.15 g 25.0 Fiber
    109. mg 990. Phosphorus
    0.0 mg 1000.0 Calcium
    25.0 mg 20.0 Niacin
    -1.0 x 0.0 x
out
    Vitamin A 3500.0 iu 70%
    Vitamin C 60.0 mg 100%
    Phosphorus 109.0 mg 11%
    Niacin 25.0 mg 125%
    Provides no significant amount of:
    Fiber
    Calcium
"""

# 1% 이상인 비타민/미네랄 정보 저장
significant = []
# 1% 미만인 비타민/미네랄 이름 저장
insignificant = []

while True:
    line = input().split()

    # A가 음수이면 종료
    A = float(line[0])
    if A < 0:
        break

    # 파싱: A U R V
    U = line[1]
    R = float(line[2])
    V = ' '.join(line[3:])  # 비타민명은 공백을 포함할 수 있음

    # 백분율 계산
    percentage = (A / R) * 100

    # 1% 이상인지 확인
    if percentage >= 1.0:
        significant.append((V, A, U, percentage))
    else:
        insignificant.append(V)

# 1% 이상인 항목 출력
for v, a, u, p in significant:
    print(f"{v} {a:.1f} {u} {p:.0f}%")

# 1% 미만인 항목 출력
print("Provides no significant amount of:")
for v in insignificant:
    print(v)
