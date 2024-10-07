# 백준 - 브론즈1 - PlayStation이 아니에요 - 321132 - 구현, 문자열 문제
'''
구현, 문자열 문제

PS4, PS5를 PS로 바꾸는 문제이다.

풀이 과정
    1. n을 입력받는다.
    2. word를 입력받는다.
    3. word에서 PS4, PS5를 PS로 바꾼다.
    4. word를 출력한다.
'''

n = int(input())
word = input()

# 테스트
# n = 14
# word = 'ILOVEPS5PSPS4A' # ILOVEPSPSPSA
# n = 6
# word = 'PS4564' # PS64

while ('PS4' in word) or ('PS5' in word):
    word = word.replace('PS4', 'PS')
    word = word.replace('PS5', 'PS')

print(word)
