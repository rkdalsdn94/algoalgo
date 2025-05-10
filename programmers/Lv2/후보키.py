# 프로그래머스 - Lv2 - 후보키 - 조합, 집합, 완전 탐색 문제
"""
조합, 집합, 완전 탐색 문제

[핵심 아이디어]
    1. 후보키의 두 가지 조건인 '유일성'과 '최소성'을 별도로 검사한다.
    2. 유일성은 해당 속성 조합으로 모든 튜플을 구분할 수 있는지 확인하는 것이다.
    3. 최소성은 이미 찾은 후보키가 현재 조합의 부분집합인지 확인하는 것이다.
    4. combinations를 사용해 모든 가능한 속성 조합을 생성한 후 각각을 검사한다.

[풀이 과정]
    1. 가능한 모든 속성 조합 생성:
       - itertools.combinations를 사용하여 1개부터 전체 열 개수까지의 모든 조합을 생성한다.
    2. 유일성 검사:
       - 각 속성 조합에 대해, 모든 행의 해당 속성 값들을 튜플로 만든다.
       - 이 튜플들을 집합으로 변환하여 중복을 제거한다.
       - 변환된 집합의 크기가 원래 행 개수와 같다면 유일성을 만족한다.
    3. 최소성 검사:
       - 유일성을 만족하는 조합들에 대해, 이미 발견한 후보키가 현재 조합의 부분집합인지 확인한다.
       - 만약 부분집합인 후보키가 있다면, 현재 조합은 최소성을 만족하지 않는다.
       - 모든 기존 후보키에 대해 부분집합 관계가 없다면, 현재 조합도 후보키로 추가한다.
    4. 최종적으로 후보키의 개수를 반환한다.
"""

from itertools import combinations

def solution(relation):
    answer = 0
    row_cnt, col_cnt = len(relation), len(relation[0])

    # 가능한 모든 열 조합
    all_cols = list(range(col_cnt))
    all_combinations = []
    for i in range(1, col_cnt + 1):
        all_combinations.extend(combinations(all_cols, i))

    # 유일성 검사
    unique_combinations = []
    for combo in all_combinations:
        # 해당 열 조합으로 모든 행이 구분되는지 확인
        values = [tuple(row[col] for col in combo) for row in relation]
        if len(set(values)) == row_cnt: # 중복 없이 모든 행이 구분되는 경우
            unique_combinations.append(combo)

    # 최소성 검사
    candidate_keys = []
    for i, combo in enumerate(unique_combinations):
        is_candidate = True

        for j, candidate in enumerate(candidate_keys):
            # 이미 찾은 후보키가 현재 조합의 부분집합인지 확인
            if set(candidate).issubset(set(combo)):
                is_candidate = False
                break

        if is_candidate:
            candidate_keys.append(combo)

    return len(candidate_keys)

relation = [
    ["100","ryan","music","2"], ["200","apeach","math","2"],
    ["300","tube","computer","3"], ["400","con","computer","4"],
    ["500","muzi","music","3"], ["600","apeach","music","2"]
]
print(solution(relation))
