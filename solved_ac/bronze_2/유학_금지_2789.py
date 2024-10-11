# 백준 - 브론즈2 - 유학 금지 - 2789 - 문자열, 구현 문제
'''
문자열, 구현 문제

단순한 구현, 문자열 문제이다.
 - 유학 금지 단어를 입력받고, 문자열을 입력받는다.
 - 유학 금지 단어를 제외한 문자열을 출력하는 문제이다.

풀이 과정
    1. word를 입력받는다.
    2. word에서 'CAMBRIDGE'에 있는 문자를 제거한다.
    3. word를 출력한다.
'''

word = input()

# 테스트
# word = 'LOVA' # LOV
# word = 'KARIJERA' # KJ

for i in 'CAMBRIDGE':
    word = word.replace(i, '')

print(word)
