# 프로그래머스 - Lv2 - 비밀 코드 해독 - 완전 탐색 문제
"""
완전 탐색 문제

[핵심 아이디어]
    - 1부터 n까지의 숫자 중에서 5개를 선택하는 모든 조합 C(n,5)을 생성
    - 각 조합이 모든 시도 결과와 일치하는지 검증
    - 조건을 만족하는 조합의 개수 반환

[풀이 과정]
    1. itertools.combinations를 사용하여 1~n 범위에서 5개를 선택하는 모든 조합 생성
    2. 각 조합을 비밀 코드 후보로 설정
    3. 모든 시도(query)에 대해 교집합 개수를 계산하여 예상 답과 일치하는지 확인
    4. 모든 시도를 통과하는 조합의 개수를 카운트
"""

from itertools import combinations

def solution(n, q, ans):
    count = 0

    # 1부터 n까지의 숫자 중에서 5개를 선택하는 모든 조합 생성
    # C(n,5) 개의 조합이 생성됨
    for secret_code in combinations(range(1, n+1), 5):
        # 비교를 위해 집합으로 변환
        secret_set = set(secret_code)

        # 모든 시도에 대해 검증
        valid = True
        for i in range(len(q)):
            # 현재 시도를 집합으로 변환
            query_set = set(q[i])

            # 교집합의 크기 = 일치하는 숫자의 개수
            intersection_count = len(secret_set & query_set)

            # 예상 답과 일치하지 않으면 이 조합은 불가능
            if intersection_count != ans[i]:
                valid = False
                break

        # 모든 시도를 통과했다면 가능한 비밀 코드
        if valid:
            count += 1

    return count

n1 = 10
q1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
ans1 = [2, 3, 4, 3, 3]
print(f"결과: {solution(n1, q1, ans1)}")  # 예상: 3

n2 = 15
q2 = [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]]
ans2 = [2, 1, 3, 0, 1]
print(f"결과: {solution(n2, q2, ans2)}")  # 예상: 5
