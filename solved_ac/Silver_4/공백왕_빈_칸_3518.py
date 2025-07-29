# 백준 - 실버4 - 공백왕 빈-칸 - 3518 - 구현, 문자열, 파싱 문제
"""
구현, 문자열, 파싱 문제

[핵심 아이디어]
    1. 각 줄의 단어들을 분리하여 2차원 리스트로 저장
    2. 각 열(동일한 위치의 단어들)에서 최대 길이를 계산
    3. 각 단어 뒤에 (최대길이 - 현재길이)만큼 공백을 추가하여 정렬
    4. 마지막 단어는 뒤에 공백을 추가하지 않음

[풀이 과정]
    1. 모든 입력 줄을 읽어서 각 줄의 단어들을 분리하여 저장
    2. 각 열에서 가장 긴 단어의 길이를 구함
    3. 출력 시 각 단어 뒤에 다음의 과정으로 적절한 공백을 추가
       - 마지막 단어가 아닌 경우: (열의최대길이 - 현재단어길이 + 1)만큼 공백 추가
       - 마지막 단어인 경우: 공백 추가하지 않음
    4. 각 줄의 끝에서 불필요한 공백 제거
"""

import sys

# 모든 줄을 읽어서 저장
lines = []
for line in sys.stdin:
    line = line.rstrip('\n')  # 줄바꿈 문자만 제거

    if line or lines:  # 빈 줄이어도 이미 입력이 시작됐으면 저장
        lines.append(line)

# 각 줄의 단어들을 분리하여 저장
words_in_lines = []
max_words = 0

for line in lines:
    words = line.split()
    words_in_lines.append(words)
    max_words = max(max_words, len(words))

# 각 열의 최대 길이 계산
max_lengths = [0] * max_words
for words in words_in_lines:
    for i, word in enumerate(words):
        max_lengths[i] = max(max_lengths[i], len(word))

for words in words_in_lines:
    res = []

    for i, word in enumerate(words):
        if i == len(words) - 1:  # 마지막 단어
            res.append(word)
        else:  # 마지막 단어가 아님
            spaces_needed = max_lengths[i] - len(word) + 1
            res.append(word + ' ' * spaces_needed)

    print(''.join(res).rstrip())
