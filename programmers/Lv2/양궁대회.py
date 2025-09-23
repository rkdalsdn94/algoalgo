# 프로그래머스 - Lv2 - 양궁대회 - 백트래킹 문제
"""
백트래킹 문제

[핵심 아이디어]
    1. 각 점수마다 2가지 선택: 가져가기(어피치+1발) vs 포기하기(0발)
    2. 백트래킹으로 모든 선택 조합 탐색 (2^10 = 1024가지)
    3. 실시간 비교 대신 모든 경우를 저장한 후 정렬로 최적해 선택
    4. 파이썬 정렬 특성 활용: (점수차, 배열[::-1])로 복합 조건 한 번에 처리

[풀이 과정]
    1. 백트래킹으로 10점부터 0점까지 순차적으로 결정
       - 가져간다면: 어피치 화살 수 + 1발 할당
       - 포기한다면: 0발 할당
    2. 모든 결정 완료 시 점수 계산하여 라이언이 이기는 경우만 저장
    3. 남은 화살은 반드시 0점에 모두 배치 (n발 모두 사용)
    4. 정렬 조건: 1순위(점수차 최대), 2순위(낮은 점수를 더 많이)
    5. 정렬된 첫 번째 결과가 답
"""

def solution(n, info):
    answer = []

    def backtrack(idx, arrows, ryan):
        # 모든 점수 결정 완료
        if idx == 11:
            ryan[10] += arrows  # 남은 화살은 0점에

            # 점수 계산
            apeach = ryan_score = 0
            for i in range(11):
                score = 10 - i
                if info[i] >= ryan[i]:
                    apeach += score if info[i] > 0 else 0
                else:
                    ryan_score += score

            # 라이언이 이기면 저장
            if ryan_score > apeach:
                answer.append((ryan_score - apeach, ryan[:]))

            ryan[10] -= arrows  # 백트래킹
            return

        # 안 쏘는 경우
        backtrack(idx + 1, arrows, ryan)

        # 쏘는 경우 (어피치보다 1발 더)
        need = info[idx] + 1
        if arrows >= need:
            ryan[idx] = need
            backtrack(idx + 1, arrows - need, ryan)
            ryan[idx] = 0

    ryan = [0] * 11
    backtrack(0, n, ryan)

    if not answer:
        return [-1]

    # 점수차 최대, 낮은 점수 우선으로 정렬
    answer.sort(key=lambda x: (x[0], x[1][::-1]), reverse=True)
    return answer[0][1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]) == [0,2,2,0,1,0,0,0,0,0,0])
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]) == [-1])
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]) == [1,1,2,0,1,2,2,0,0,0,0])
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]) == [1,1,1,1,1,1,1,1,0,0,2])
