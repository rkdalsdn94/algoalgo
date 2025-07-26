# 백준 - 실버5 - Reverse - 26587 - 구현, 문자열 문제
"""
구현, 문자열 문제

[핵심 아이디어]
    1. 각 라인을 단어로 분할하여 모음으로 시작하는 단어들을 별도로 추출
    2. 모음으로 시작하는 단어들의 순서를 뒤집어서 스택처럼 활용
    3. 원본 문장을 순회하며 모음 단어는 뒤집어진 순서로, 자음 단어는 원래 위치 유지

[풀이 과정]
    1. 입력이 끝날 때까지 다음의 과정을 반복한다.
       - 라인을 단어들로 분할
       - 모음(a, e, i, o, u)으로 시작하는 단어들을 찾아 별도 리스트에 저장
       - 모음 단어 리스트를 뒤집기 (reverse)
    2. 원본 단어 순서를 유지하면서 결과 구성한다.
       - 각 단어가 모음으로 시작하면 뒤집어진 모음 단어 리스트에서 순서대로 가져오기
       - 자음으로 시작하면 원래 단어 그대로 사용
    3. 완성된 결과 라인을 출력한다.

in
    apple
    Eat apples
    snakes are coming into Your house
    Axe hat bat other toy octagon me I love oranges
out
    apple
    apples Eat
    snakes into coming are Your house
    oranges hat bat I toy octagon me other love Axe
"""

def is_vowel(char):
    """첫 글자가 모음인지 확인하는 함수"""
    return char.lower() in 'aeiou'

def solve_line(line):
    """한 라인을 처리하는 함수"""
    words = line.strip().split()
    if not words:
        return ""

    # 모음으로 시작하는 단어들을 찾아서 저장
    vowel_words = []
    for word in words:
        if is_vowel(word[0]):
            vowel_words.append(word)

    # 모음 단어들의 순서를 뒤집기
    vowel_words.reverse()
    res = []
    vowel_index = 0

    for word in words:
        if is_vowel(word[0]):
            res.append(vowel_words[vowel_index])
            vowel_index += 1
        else:
            res.append(word)

    return ' '.join(res)

while True:
    try:
        line = input()
        print(solve_line(line))
    except EOFError:
        break
