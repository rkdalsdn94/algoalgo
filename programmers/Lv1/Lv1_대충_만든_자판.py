# 프로그래머스 - Lv1 - 대충 만든 자판 - 자료 구조(해시), 그리디 문제
"""
[문제 분류]
자료 구조(해시), 그리디 문제

[핵심 아이디어]
    - 각 문자를 입력하는 데 필요한 최소 키 입력 횟수를 해시맵(딕셔너리)에 저장
    - 여러 키에 같은 문자가 할당된 경우, 가장 적은 클릭으로 입력할 수 있는 방법 선택
    - 각 타겟 문자열에 대해 문자별 키 입력 횟수의 총합 계산

[풀이 과정]
    1. 각 문자를 입력하는 데 필요한 최소 키 입력 횟수를 저장할 해시맵(딕셔너리) 생성
    2. 각 키맵을 순회하며, 문자별로 최소 입력 횟수 계산
       - 이미 해시맵에 있는 문자라면, 기존 값과 현재 값 중 최소값 선택
       - 해시맵에 없는 문자라면, 현재 값으로 저장
    3. 각 타겟 문자열에 대해:
       - 문자열의 각 문자를 순회하며 필요한 키 입력 횟수의 합 계산
       - 작성할 수 없는 문자가 있으면 -1 반환
    4. 각 타겟 문자열별 결과를 배열에 저장하여 반환
"""

def solution(keymap, targets):
    answer = []
    min_key_presses = dict()  # 각 문자를 입력하는 데 필요한 최소 키 입력 횟수

    # 각 키맵을 순회하며 문자별 최소 입력 횟수 계산
    for key_characters in keymap:
        for position, character in enumerate(key_characters):
            # 이미 해시맵에 있는 문자는 최소값으로 갱신, 없으면 현재 값으로 저장
            if character in min_key_presses:
                min_key_presses[character] = min(min_key_presses[character], position + 1)
            else:
                min_key_presses[character] = position + 1

    # 각 타겟 문자열에 대해 필요한 총 키 입력 횟수 계산
    for target in targets:
        total_key_presses = 0

        for character in target:
            # 작성할 수 없는 문자가 있으면 -1 반환
            if character not in min_key_presses:
                total_key_presses = -1
                break
            total_key_presses += min_key_presses[character]

        answer.append(total_key_presses)

    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]) == [9, 4])
print(solution(["AA"], ["B"]) == [-1])
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]) == [4, 6])
