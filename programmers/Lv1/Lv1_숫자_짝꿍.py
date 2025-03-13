# 프로그래머스 - Lv1 - 숫자 짝꿍 - 문자열, 구현 문제
"""
문자열, 구현 문제

핵심 아이디어
    - 두 문자열 X, Y에서 각 숫자의 등장 횟수 카운트
    - 두 문자열에 공통으로 나타나는 숫자를 찾되, 가장 큰 정수를 만들기 위해 큰 숫자부터 확인
    - 공통으로 나타나는 각 숫자에 대해, 최소 등장 횟수 결과를 추가
    - 공통 숫자가 없으면 '-1', 공통 숫자가 "0"으로만 구성되어 있으면 '0' 반환

풀이 과정
    - Counter 객체를 사용하여 X와 Y 각각의 문자열에서 각 숫자의 등장 횟수를 계산한다.
    - 9부터 0까지 내림차순으로 숫자를 확인하여 가장 큰 정수를 구성한다.
    - 특정 숫자가 X와 Y 모두에 존재하는 경우, 두 문자열에서의 최소 등장 횟수만큼 결과 문자열에 추가한다.
    - 결과 문자열이 비어있으면 공통 숫자가 없으므로 "-1"을 반환한다.
    - 결과 문자열이 '0'으로 시작한다면, 이는 0만 공통으로 있다는 의미이므로 "0"을 반환한다.
    - 그 외의 경우 결과 문자열을 그대로 반환한다.
"""

from collections import Counter


def solution(X, Y):
    answer = ''
    x_counter = Counter(X)
    y_counter = Counter(Y)

    # 공통으로 나타나는 숫자들을 내림차순으로 확인
    for digit in range(9, -1, -1):
        digit_str = str(digit)

        if digit_str in x_counter and digit_str in y_counter:
            # 공통으로 나타나는 숫자 중 최소 개수만큼 추가
            count = min(x_counter[digit_str], y_counter[digit_str])
            answer += digit_str * count

    # 공통 숫자가 없는 경우
    if not answer:
        return '-1'

    # 결과가 0으로만 구성된 경우
    if answer[0] == '0':
        return '0'

    return answer


print(solution("100", "2345") == "-1")
print(solution("100", "203045") == "0")
print(solution("100", "123450") == "10")
print(solution("12321", "42531") == "321")
print(solution("5525", "1255") == "552")
