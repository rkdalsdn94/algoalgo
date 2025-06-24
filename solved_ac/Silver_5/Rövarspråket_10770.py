# 백준 - 실버5 - Rövarspråket - 10770 - 구현, 문자열 문제
"""
구현, 문자열 문제

[핵심 아이디어]
    1. 모음(a, e, i, o, u)은 그대로 유지
    2. 자음은 3개의 글자로 변환:
       - 원래 자음
       - 가장 가까운 모음 (거리가 같으면 알파벳 순서가 앞선 것)
       - 다음 자음 (z인 경우는 z)
    3. 각 문자의 알파벳 위치를 이용해 거리 계산

[풀이 과정]
    1. 모음의 위치를 미리 정의 (a=1, e=5, i=9, o=15, u=21)
    2. 각 문자를 순회하며 모음이면 그대로 추가하고, 자음이면 다음의 변환 규칙 적용한다.
        a. 모든 모음과의 거리를 계산하여 가장 가까운 모음 찾기
        b. 현재 자음 다음에 오는 자음 찾기 (모음 건너뛰기)
        c. 원래자음 + 가장가까운모음 + 다음자음 순서로 추가
"""

word = input()

# 테스트
# word = "joy"  # jikoyuz
# word = "ham"  # hijamon

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_positions = [1, 5, 9, 15, 21]  # a=1, e=5, i=9, o=15, u=21

def get_closest_vowel(consonant):
    """자음에 가장 가까운 모음을 찾는 함수"""
    pos = ord(consonant) - ord('a') + 1  # 자음의 알파벳 위치 (1-based)
    min_distance = float('inf')
    closest_vowel = 'a'

    for i, vowel_pos in enumerate(vowel_positions):
        distance = abs(pos - vowel_pos)
        if distance < min_distance:
            min_distance = distance
            closest_vowel = vowels[i]
        elif distance == min_distance and vowels[i] < closest_vowel:
            # 거리가 같으면 알파벳 순서가 앞선 것 선택
            closest_vowel = vowels[i]

    return closest_vowel


def get_next_consonant(consonant):
    """다음 자음을 찾는 함수"""
    if consonant == 'z':
        return 'z'

    # 현재 자음 다음 문자부터 시작
    next_char = chr(ord(consonant) + 1)

    # 모음이 아닌 문자(자음)를 찾을 때까지 반복
    while next_char <= 'z' and next_char in vowels:
        next_char = chr(ord(next_char) + 1)

    return next_char if next_char <= 'z' else 'z'


res = ""
for char in word:
    if char in vowels:
        # 모음은 그대로 추가
        res += char
    else:
        # 자음은 3글자로 변환
        closest_vowel = get_closest_vowel(char)
        next_consonant = get_next_consonant(char)
        res += char + closest_vowel + next_consonant

print(res)
