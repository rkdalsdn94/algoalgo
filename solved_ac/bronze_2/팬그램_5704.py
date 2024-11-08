# 백준 - 브론즈2 - 팬그램 - 5704 - 구현, 문자열 문제
'''
구현, 문자열 문제

단순한 구현 문제이다.

풀이 과정
    1. 입력을 받는다.
    2. 입력이 *이면 종료한다.
    3. 입력이 공백이면 삭제한다.
    4. 입력이 26개 이상이면 Y를 출력한다.
    5. 입력이 26개 미만이면 N을 출력한다.

in
    jackdawf loves my big quartz sphinx
    abcdefghijklmnopqrstuvwxyz
    hello world
    *
out
    Y
    Y
    N
'''

from collections import Counter

while 1:
    s = Counter(input())

    if s['*']  == 1:
        break
    if s[' '] >= 1:
        del s[' ']
    if len(s) >= 26:
        print('Y')
    else:
        print('N')
