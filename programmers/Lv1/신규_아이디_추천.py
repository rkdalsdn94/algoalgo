# 프로그래머스 - Lv1 - 신규 아이디 추천 - 문자열, 정규식, 구현
"""
문자열, 정규식, 구현 문제

[핵심 아이디어]
    1. 7단계의 순차적 처리 과정을 단계별로 구현
    2. 정규식을 활용하여 연속된 마침표 처리를 효율적으로 수행
    3. 문자열을 리스트로 변환하여 문자 단위 조작을 용이하게 처리
    4. 각 단계에서 카카오 아이디 규칙에 맞게 문자열을 변환

[풀이 과정]
    1단계: 모든 대문자를 소문자로 변환 (lower() 사용)
    2단계: 허용된 문자(소문자, 숫자, -, _, .)만 남기고 나머지 제거
    3단계: 연속된 마침표를 하나로 치환 (정규식 re.sub 사용)
    4단계: 처음과 끝의 마침표 제거 (while문으로 반복 처리)
    5단계: 빈 문자열인 경우 'a' 추가
    6단계: 길이가 16자 이상인 경우 첫 15자만 남기고, 끝의 마침표 제거
    7단계: 길이가 2자 이하인 경우 마지막 문자를 반복하여 3자까지 확장
"""

import re

def solution(new_id):
    # 1단계: 대문자 → 소문자 변환, 2단계: 허용된 문자만 필터링
    answer = [char for char in new_id.lower() if char.isalnum() or char in '-_.']

    # 3단계: 연속된 마침표를 하나의 마침표로 치환
    answer = list(re.sub('[.]+', '.', ''.join(answer)))

    # 4단계: 처음과 끝의 마침표 제거
    while answer and (answer[0] == '.' or answer[-1] == '.'):
        if answer[0] == '.':
            answer = answer[1:]
        if answer and answer[-1] == '.':  # answer가 비어있을 수 있으므로 다시 체크
            answer = answer[:-1]

    # 5단계: 빈 문자열인 경우 'a' 추가
    if not answer:
        answer = ['a']

    # 6단계: 길이가 16자 이상인 경우 첫 15자만 남기기
    if len(answer) > 15:
        answer = answer[:15]
        # 15자로 자른 후 끝에 마침표가 있다면 제거
        while answer and answer[-1] == '.':
            answer = answer[:-1]

    # 7단계: 길이가 2자 이하인 경우 마지막 문자 반복
    while len(answer) <= 2:
        answer.append(answer[-1])

    return ''.join(answer)

print(solution("...!@BaT#*..y.abcdefghijklm") == 'bat.y.abcdefghi')
print(solution("z-+.^.") == 'z--')
print(solution("=.=") == 'aaa')
print(solution("123_.def") == '123_.def')
print(solution("abcdefghijklmn.p") == 'abcdefghijklmn')
