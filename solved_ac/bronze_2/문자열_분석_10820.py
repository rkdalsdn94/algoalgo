# 백준 - 브론즈2 - 문자열 분석 - 10820 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

input 값의 길이가 총 100자 이므로 한 글자씩 소문자, 대문자, 숫자, 공백을 검사한 후 각 부분의 값을 1씩 더하면 된다.
'''

while 1:
    try:
        word = input()
        small_letter, capital_letter, number, space_bar = 0, 0, 0, 0

        for i in word:
            if i.islower():
                small_letter += 1
            elif i.isupper():
                capital_letter += 1
            elif i.isnumeric():
                number += 1
            elif i == ' ':
                space_bar += 1
        
        print(small_letter, capital_letter, number, space_bar)
    except:
        break
