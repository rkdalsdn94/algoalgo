# 백준 - 브론즈2 - 거울상 - 4583 - 문자열, 구현 문제
"""
문자열, 구현 문제

[핵심 아이디어]
    1. 거울상 관계인 문자들의 매핑 테이블을 생성한다.
    2. 거울에 비친 단어는 원래 단어가 뒤집히고 각 문자가 거울상 문자로 변환된 것이다.
    3. 따라서 입력 단어를 뒤집고, 각 문자를 대응하는 거울상 문자로 변환하면 원래 단어를 복원할 수 있다.
    4. 거울상 관계가 없는 문자가 포함되면 "INVALID"를 출력한다.

[풀이 과정]
    1. 거울상 관계 딕셔너리를 생성한다. (b <-> d, p <-> q, i,o,v,w,x는 자기 자신과 대칭)
    2. 입력으로 주어진 각 단어에 대해:
       a. 모든 문자가 거울상 관계 딕셔너리에 포함되는지 확인
       b. 포함되지 않는 문자가 있으면 "INVALID" 출력
       c. 모든 문자가 유효하면 단어를 뒤집고 각 문자를 거울상 문자로 변환
    3. "#"이 입력되면 프로그램 종료
"""

# 거울상 관계 매핑 딕셔너리
mirror_map = {
    'b': 'd', 'd': 'b',
    'p': 'q', 'q': 'p',
    'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'
}

while True:
    word = input().strip()

    # 종료 조건
    if word == '#':
        break

    # 거울상 복원이 가능한지 확인
    valid = True
    for char in word:
        if char not in mirror_map:
            valid = False
            break

    if not valid:
        print("INVALID")
    else:
        # 단어를 뒤집고 각 문자를 거울상 문자로 변환
        original_word = ""
        for char in reversed(word):
            original_word += mirror_map[char]
        print(original_word)
