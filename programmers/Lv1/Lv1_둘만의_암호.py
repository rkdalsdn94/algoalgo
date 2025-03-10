# 프로그래머스 - Lv1 - 둘만의 암호 - 문자열, 구현 문제
"""
문자열, 구현 문제

[핵심 아이디어]
    1. 유효한 알파벳(skip에 포함되지 않은) 리스트를 미리 생성한다.
    2. 각 문자에 대해 유효한 알파벳 리스트에서의 위치를 찾고, index만큼 이동한 새 위치의 문자로 치환한다.
    3. 알파벳 순환을 모듈로 연산(%)으로 처리하여 z 이후에 a로 돌아가게 한다.

[풀이 과정]
    1. a부터 z까지의 알파벳 중 skip에 포함되지 않은 문자들만으로 알파벳 리스트를 생성한다.
    2. 입력 문자열 s의 각 문자에 대해:
      a. 해당 문자가 알파벳 리스트에서 위치한 인덱스를 찾는다.
      b. 찾은 인덱스에 index를 더한 후, 알파벳 리스트 길이로 나머지 연산을 수행하여 순환을 처리한다.
      c. 계산된 새 인덱스에 해당하는 문자를 결과 문자열에 추가한다.
    3. 완성된 결과 문자열을 반환한다.
"""

def solution(s, skip, index):
    answer = ''

    # 알파벳 문자들을 포함하는 집합 생성 (skip에 포함된 문자들 제외)
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]

    for char in s:
        current_index = alphabet.index(char)
        new_index = (current_index + index) % len(alphabet)
        answer += alphabet[new_index]

    return answer

print(solution("aukks", "wbqd", 5) == "happy")
