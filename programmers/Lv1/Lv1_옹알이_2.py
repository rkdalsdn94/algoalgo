# 프로그래머스 - Lv1 - 옹알이 - 문자열, 정규 표현식(패턴 매칭) 문제
'''
문자열, 정규 표현식(패턴 매칭) 문제

[핵심 아이디어]
    1. 주어진 단어가 'aya', 'ye', 'woo', 'ma'의 조합으로만 구성되어 있는지 확인
    2. 같은 발음이 연속해서 나오는 경우(예: 'yeye') 발음할 수 없음을 처리
    3. 조건을 만족하는 단어 수 계산

[풀이 과정]
    1. 각 단어를 순회하며 검사
    2. 각 발음 패턴('aya', 'ye', 'woo', 'ma')에 대해:
       - 해당 패턴이 연속해서 두 번 이상 나타나지 않는지 확인(j*2 not in i)
       - 연속하지 않는 경우에만 해당 패턴을 공백으로 대체
    3. 모든 검사 후 단어가 전부 공백으로만 이루어져 있다면 발음 가능한 단어로 판단
    4. 발음 가능한 단어의 총 개수 반환
'''

def solution(babbling):
    answer = 0
    meosseuk = ['aya', 'ye', 'woo', 'ma']

    for i in babbling:
        for j in meosseuk:
            if j * 2 not in i:
                i = i.replace(j, ' ')

        if i.isspace():
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa"]) == 1)
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]) == 2)

'''
정규 표현식 풀이

import re
def regular_expression_solution(babbling):
    answer = 0

    for word in babbling:
        # 연속된 같은 발음이 있는지 확인
        if re.search(r'(aya|ye|woo|ma)\1+', word):
            continue

        # 발음할 수 있는 모든 소리를 제거
        word = re.sub(r'aya|ye|woo|ma', '', word)

        # 남은 문자열이 없다면 발음 가능
        if word == '':
            answer += 1

    return answer
print(regular_expression_solution(["aya", "yee", "u", "maa"]) == 1)
print(regular_expression_solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]) == 2)
'''
