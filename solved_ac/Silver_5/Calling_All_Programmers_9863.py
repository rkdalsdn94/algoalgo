# 백준 - 실버5 - Calling All Programmers - 9863 - 구현, 시뮬레이션, 자료 구조(큐) 문제
"""
구현, 시뮬레이션, 자료 구조(큐) 문제

[핵심 아이디어]
    - 원형 배치된 n명의 발신자에서 m개씩 건너뛰며 제거하는 시뮬레이션
    - 리스트를 사용하여 원형 순환 구조를 모듈로 연산으로 구현
    - 현재 위치에서 (current_idx + m - 1) % len(list)로 다음 제거 위치 계산

[풀이 과정]
    1. 1부터 n까지의 발신자를 리스트로 생성
    2. 현재 인덱스를 0으로 초기화
    3. k번 반복하며 다음 작업 수행
       - 현재 위치에서 m개를 세어 제거할 인덱스 계산 (원형 순환 고려)
       - 해당 위치의 발신자를 제거하고 값을 저장
       - 제거 후 인덱스가 리스트 범위를 벗어나면 0으로 조정
    4. k번째로 제거된 발신자의 번호 출력

in
    10 7 5
    20 1 20
    0 0 0
out
    3
    20
"""

while True:
    n, m, k = map(int, input().split())

    # 종료 조건
    if n == 0 and m == 0 and k == 0:
        break

    # 1부터 n까지의 발신자 리스트 생성
    callers = list(range(1, n + 1))
    current_idx = 0  # 현재 위치 인덱스

    # k번째 발신자를 찾을 때까지 반복
    for i in range(k):
        # m개 위치를 건너뛰어 제거할 인덱스 계산 (원형 순환)
        # (현재 위치 + m - 1)을 리스트 크기로 나눈 나머지
        current_idx = (current_idx + m - 1) % len(callers)

        # 해당 위치의 발신자 제거
        res = callers.pop(current_idx)

        # 제거 후 현재 인덱스가 리스트 범위를 벗어나면 처음으로
        if current_idx >= len(callers) and len(callers) > 0:
            current_idx = 0

    # k번째로 제거된 발신자 출력
    print(res)
