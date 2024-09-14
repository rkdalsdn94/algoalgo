# 백준 - 브론즈2 - Cryptoquote - 2703 - 구현, 문자열 문제
'''
구현, 문자열 문제

단순한 구현 문제이다.
두 문자를 입력받고, 첫 번째 문자를 두 번째 문자열 기준으로 바꾸는 문제이다.

풀이 과정
    1. t를 입력받는다.
    2. t만큼 반복한다.
        2.1. encrypted_word, substitution_rule를 입력받는다.
        2.2. res를 만들어 빈 문자열로 초기화한다.
        2.3. encrypted_word를 돌면서 공백이면 res에 추가하고, 아니면 substitution_rule을 이용하여 바꾼다.
            2.3.1. ord(i) - ord('A')를 이용하여 substitution_rule의 인덱스를 구해서 res에 추가해야 한다.
        2.4. res를 출력한다.
'''

t = int(input())
for _ in range(t):
    encrypted_word, substitution_rule = input(), input()
    res = ''

    for i in encrypted_word:
        if i == ' ':
            res += ' '
        else:
            res += substitution_rule[ord(i) - ord('A')]

    print(res)
