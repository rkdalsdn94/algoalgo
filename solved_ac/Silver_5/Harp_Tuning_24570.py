# 백준 - 실버5 - Harp Tuning - 24570 - 구현, 문자열, 파싱 문제
"""
구현, 문자열, 파싱 문제

[핵심 아이디어]
    정규표현식을 사용하여 "문자들+부호+숫자" 패턴을 찾아 파싱

[풀이 과정]
    1. 정규표현식 패턴 '[A-Z]+[+-]\d+' 으로 각 명령어를 추출
    2. 각 명령어에서 문자, 부호, 숫자 부분을 분리
    3. 부호가 '+'면 "tighten", '-'면 "loosen"으로 변환하여 출력
"""

import re

instructions = input().strip()

# 테스트
# instructions = 'AFB+8HC-4' # AFB tighten 8 \ HC loosen 4
# instructions = 'AFB+8SC-4H-2GDPE+9' # AFB tighten 8 \ SC loosen 4 \ H loosen 2 \ GDPE tighten 9

# 정규표현식으로 각 명령어 패턴 찾기 (문자들 + 부호 + 숫자)
pattern = r'[A-Z]+[+-]\d+'
matches = re.findall(pattern, instructions)

for match in matches:
    # 부호의 위치 찾기
    plus_pos = match.find('+')
    minus_pos = match.find('-')

    if plus_pos != -1:
        strings = match[:plus_pos]
        operation = "tighten"
        turns = match[plus_pos+1:]
    else:
        strings = match[:minus_pos]
        operation = "loosen"
        turns = match[minus_pos+1:]

    print(f"{strings} {operation} {turns}")
