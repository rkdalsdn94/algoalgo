# 프로그래머스 - Lv3 - 인사고과 - 정렬, 그리디 문제
"""
정렬, 그리디 문제

[핵심 아이디어]
    1. 파레토 프론티어 개념을 활용하여 인센티브 자격자를 효율적으로 찾는다.
    2. 근무 태도 점수로 내림차순, 동료 평가 점수로 오름차순 정렬한다.
    3. 정렬된 순서대로 처리하면서 동료 평가 점수의 최댓값을 추적한다.
    4. 현재 사원의 동료 평가 점수가 지금까지의 최댓값보다 낮으면 인센티브 받지 못함.

[풀이 과정]
    1. 완호의 점수를 미리 저장하고, 모든 사원을 근무태도(내림차순), 동료평가(오름차순) 기준 정렬
    2. 정렬된 순서대로 처리하면서 동료 평가 점수의 최댓값을 추적:
       - 현재 사원의 동료 평가가 최댓값 이상이면 인센티브 자격 획득
       - 완호가 자격을 못 얻으면 즉시 -1 반환
    3. 자격을 얻은 사원들을 점수 합으로 내림차순 정렬
    4. 완호의 석차를 계산하여 반환 (동점자는 같은 석차, 다음 석차는 건너뜀)
"""

def solution(scores):
    wanho_score = scores[0]  # 완호의 점수

    # 근무 태도 점수는 내림차순, 동료 평가 점수는 오름차순 정렬
    indexed_scores = [(score, i) for i, score in enumerate(scores)]
    indexed_scores.sort(key=lambda x: (-x[0][0], x[0][1]))

    # 인센티브를 받을 수 있는 사원들 찾기 (파레토 프론티어)
    incentive_eligible = []
    max_colleague_score = 0

    for score, original_idx in indexed_scores:
        work_attitude, colleague_eval = score

        # 현재 사원이 인센티브를 받을 수 있는지 확인
        if colleague_eval >= max_colleague_score:
            incentive_eligible.append((sum(score), original_idx))
            max_colleague_score = max(max_colleague_score, colleague_eval)
        elif original_idx == 0:  # 완호가 인센티브를 받지 못하는 경우
            return -1

    # 완호가 인센티브를 받을 수 있는지 최종 확인
    wanho_eligible = any(idx == 0 for _, idx in incentive_eligible)
    if not wanho_eligible:
        return -1

    # 점수 합으로 내림차순 정렬하여 석차 계산
    incentive_eligible.sort(key=lambda x: x[0], reverse=True)

    # 완호의 석차 찾기
    rank = 1
    for i, (total, idx) in enumerate(incentive_eligible):
        if i > 0 and incentive_eligible[i-1][0] > total:
            rank = i + 1
        if idx == 0:  # 완호를 찾았을 때
            return rank

    return -1

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))  # 4
