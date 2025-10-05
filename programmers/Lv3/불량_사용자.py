# 프로그래머스 - Lv3 - 불량 사용자 - 백 트래킹, 자료구조(Set), 패턴 매칭 문제
"""
백 트래킹, 자료구조(Set), 패턴 매칭 문제

[핵심 아이디어]
    1. 패턴 매칭: banned_id의 '*'를 고려하여 user_id와 매칭 확인
    2. 백트래킹: 각 banned_id에 매칭되는 user_id를 중복 없이 선택
    3. 중복 제거: frozenset으로 순서 무관하게 같은 조합 제거

[풀이 과정]
    1. 패턴 매칭 함수로 각 banned_id에 매칭되는 user_id 찾기
       - is_match 함수로 길이와 문자 패턴 확인
    2. 각 banned_id별 후보 리스트 생성
       - candidates[i]: banned_id[i]에 매칭 가능한 user_id 목록
    3. 백트래킹으로 모든 가능한 조합 생성
       - 첫 번째 banned_id부터 순차적으로 처리
       - 각 단계에서 후보 중 하나 선택 (중복 사용 금지)
       - 모든 banned_id 처리 완료 시 결과에 추가
    4. frozenset을 사용해 순서와 무관한 중복 제거
       - set에 frozenset 저장으로 자동 중복 제거
    5. 최종 조합의 개수 반환
"""

def is_match(user, banned):
    """
    패턴 매칭 함수: banned_id 패턴과 user_id가 매칭되는지 확인

    예시:
        is_match("frodo", "fr*d*") → True
        is_match("frodo", "abc1**") → False (길이 다름)
    """
    if len(user) != len(banned):
        return False

    for u, b in zip(user, banned):
        if b != '*' and u != b:
            return False
    return True


def backtrack(index, selected, candidates, banned_id, answer):
    """
    백트래킹 함수: 모든 가능한 제재 아이디 조합 탐색

    매개변수:
        index: 현재 처리 중인 banned_id의 인덱스
        selected: 현재까지 선택된 user_id 리스트
        candidates: 각 banned_id에 매칭되는 user_id 목록
        banned_id: 불량 사용자 아이디 목록 (길이 확인용)
        answer: 결과를 저장할 set (frozenset들의 집합)

    동작 원리:
        1. 모든 banned_id 처리 완료 시 → 결과에 추가
        2. 현재 banned_id의 후보 중 하나를 선택
        3. 이미 선택되지 않은 user_id만 선택 (중복 방지)
        4. 다음 banned_id로 재귀 호출
    """
    # 기저 조건: 모든 banned_id에 user_id 할당 완료
    if index == len(banned_id):
        # frozenset으로 변환하여 순서 무관하게 저장
        answer.add(frozenset(selected))
        return

    # 현재 banned_id에 매칭되는 user_id들 탐색
    for user in candidates[index]:
        # 중복 사용 방지: 이미 선택된 user_id는 제외
        if user not in selected:
            # 현재 user_id를 선택하고 다음 단계로
            backtrack(index + 1, selected + [user], candidates, banned_id, answer)


def solution(user_id, banned_id):
    # 각 banned_id에 매칭 가능한 user_id 목록 생성
    candidates = []
    for banned in banned_id:
        matched = [user for user in user_id if is_match(user, banned)]
        candidates.append(matched)

    # 결과 저장용 set (frozenset들의 집합으로 중복 자동 제거)
    answer = set()

    # 백트래킹 시작: index=0, selected=[], 필요한 정보 모두 전달
    backtrack(0, [], candidates, banned_id, answer)

    # 고유한 조합의 개수 반환
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))  # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))  # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))  # 3
