# 백준 - 브론즈1 - Is the Name of This Problem - 4566 - 문자열, 파싱 문제
"""
문자열, 파싱 문제

[핵심 아이디어]
    1. Quine 패턴을 정확히 이해: "A" A 형태 (따옴표 안의 구문이 따옴표 밖에서 정확히 반복)
    2. 문자열을 순차적으로 파싱하여 패턴 매칭 검사
    3. 따옴표의 위치와 구문의 일치 여부를 단계별로 검증

[풀이 과정]
    1. 각 입력 문장에 대해 다음 조건들을 순차적으로 확인:
       a. 첫 번째 문자가 따옴표(")인지 확인
       b. 두 번째 따옴표의 위치를 찾고, 그 사이의 구문 A를 추출
       c. 구문 A가 비어있지 않은지 확인
       d. 두 번째 따옴표 바로 다음이 스페이스인지 확인
       e. 스페이스 다음부터 끝까지의 문자열이 구문 A와 정확히 일치하는지 확인
    2. 모든 조건을 만족하면 "Quine(A)" 출력, 하나라도 불만족하면 "not a quine" 출력
    3. "END"가 입력될 때까지 반복
"""

while True:
    line = input().strip()
    if line == "END":
        break

    # 1단계: 따옴표로 시작하는지 확인
    if len(line) == 0 or line[0] != '"':
        print("not a quine")
        continue

    # 2단계: 두 번째 따옴표 찾기
    second_quote_pos = -1
    for i in range(1, len(line)):
        if line[i] == '"':
            second_quote_pos = i
            break

    # 두 번째 따옴표가 없는 경우
    if second_quote_pos == -1:
        print("not a quine")
        continue

    # 3단계: 구문 A 추출 (첫 번째와 두 번째 따옴표 사이)
    phrase_a = line[1:second_quote_pos]

    # 구문 A가 비어있는 경우 (문제 조건: nonempty sequence)
    if len(phrase_a) == 0:
        print("not a quine")
        continue

    # 4단계: 두 번째 따옴표 다음이 스페이스인지 확인
    if second_quote_pos + 1 >= len(line) or line[second_quote_pos + 1] != ' ':
        print("not a quine")
        continue

    # 5단계: 스페이스 다음부터 끝까지가 구문 A와 정확히 일치하는지 확인
    remaining_part = line[second_quote_pos + 2:]
    if remaining_part == phrase_a:
        print(f"Quine({phrase_a})")
    else:
        print("not a quine")
