# 백준 - 실버3 - 염색체 - 9342 - 문자열, 정규표현식 문제
'''
문자열, 정규표현식 문제

규칙
 - 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
 - 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
 - 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
 - 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
 - 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

풀이 과정
1. 입력 값을 입력 받는다.
2. 정규표현식을 사용하여 위 규칙을 만족하는 패턴을 만든다.
3. 패턴을 사용하여 문자열을 검사한다.
4. 만약 패턴이 일치하면 'Infected!' 출력하고, 그렇지 않으면 'Good'를 출력한다.
'''

import re

n = int(input())
word_list = [input() for _ in range(n)]

# n = 15
# word_list = [
#     'AFC', 'AAFC', 'AAAFFCC', 'AAFCC',
#     'BAFC', 'QWEDFGHJMNB', 'DFAFCB',
#     'ABCDEFC', 'DADC', 'SDFGHJKLQWERTYU',
#     'AAAAAAAAAAAAABBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCDDDDDDDDDDDEEEEEEEEEEEEEEEFFFFFFFFC',
#     'AAAFFFFFBBBBCCCAAAFFFF', 'ABCDEFAAAFFFCCCABCDEF', 'AFCP', 'AAFFCPP'
# ]
# '''
#     Infected!
#     Infected!
#     Infected!
#     Infected!
#     Infected!
#     Good
#     Good
#     Good
#     Good
#     Good
#     Good
#     Good
#     Good
#     Good
#     Good
# '''

pattern = re.compile('^[A-F]?A+F+C+[A-F]?$')

for word in word_list:
    if pattern.match(word):
        print('Infected!')
    else:
        print('Good')
