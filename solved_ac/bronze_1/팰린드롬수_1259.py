'''
단순 구현, 문자열 문제

문자열을 뒤집고 원래 입력받은 문자열이랑 같은지 확인하고 출력하면 된다.
in
    121
    1231
    12421
    0
out
    yes
    no
    yes
'''

while 1:
    x = input()

    if x == '0':
        break

    if x == x[::-1]: print('yes')
    else: print('no')
