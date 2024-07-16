# 백준 - 브론즈1 - 단어 퍼즐 - 9946 - 구현, 문자열, 정렬 문제
'''
구현, 문자열, 정렬 문제

단순한 구현, 문자열 문제이다.
정렬로 풀어도 되고, Counter를 import해서 풀어도 된다.

풀이 과정
    1. 두 문자열을 입력받는다.
    2. 만약 두 문자열이 'END'라면 종료한다.
    3. 만약 두 문자열을 정렬한 결과가 같다면 'same'을 출력한다.
    4. 아니라면 'different'를 출력한다.

in
    Testing
    intestg
    abc
    aabbbcccc
    abcabcbcc
    aabbbcccc
    abc
    xyz
    END
    END
out
    Case 1: same
    Case 2: different
    Case 3: same
    Case 4: different
'''

i = 1

while 1:
    a, b = input(), input()

    if a == 'END' and b == 'END':
        break

    if sorted(a) == sorted(b):
        print('Case {}: same'.format(i))
    else:
        print('Case {}: different'.format(i))
    i += 1
