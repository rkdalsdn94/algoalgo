# 백준 - 브론즈2 - Egg Drop - 11606 - 구현, 시뮬레이션 문제
"""
구현, 시뮬레이션 문제

[핵심 아이디어]
    1. 계란의 깨짐/안전 패턴은 연속적 - 임계점 아래는 모두 안전, 위는 모두 위험
    2. SAFE 결과 중 최고층과 BROKEN 결과 중 최저층을 찾아 경계 범위 결정
    3. 경계값 계산으로 가능한 최소/최대 임계점 도출

[풀이 과정]
    1. 실험 결과를 분석하여 SAFE인 최고층(max_safe)과 BROKEN인 최저층(min_broken) 찾기
    2. 예외 상황 처리
       - SAFE 결과가 없으면 max_safe = 1 (1층은 항상 안전)
       - BROKEN 결과가 없으면 min_broken = k (k층은 항상 위험)
    3. 출력
       - 깨질 수 있는 최저층 = min(max_safe + 1, min_broken)
       - 안전할 수 있는 최고층 = max(max_safe, min_broken - 1)
"""

n, k = map(int, input().split())
n_list = [input().split() for _ in range(n)]

# 테스트
# n, k = 2, 10
# n_list = ['4 SAFE'.split(), '7 BROKEN'.split()] # 5 6
# n, k = 3, 5
# n_list = ['2 SAFE'.split(), '4 SAFE'.split(), '3 SAFE'.split()] # 5 4
# n, k = 4, 3
# n_list = [
#     '2 BROKEN'.split(), '2 BROKEN'.split(),
#     '1 SAFE'.split(), '3 BROKEN'.split()
# ] # 2 1

max_safe = 1  # SAFE 결과 중 최고층 (기본값: 1층은 항상 안전)
min_broken = k  # BROKEN 결과 중 최저층 (기본값: k층은 항상 위험)

for floor, res in n_list:
    floor = int(floor)

    if res == "SAFE":
        max_safe = max(max_safe, floor)
    else:  # result == "BROKEN"
        min_broken = min(min_broken, floor)

lowest_break = min(max_safe + 1, min_broken)
highest_safe = max(max_safe, min_broken - 1)

print(lowest_break, highest_safe)
