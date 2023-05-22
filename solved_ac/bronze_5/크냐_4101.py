# 백준 - 브론즈5 - 크냐? - 4101 - 단순 구현 문제
'''
단순 구현 문제

두 수의 값이 0, 0이 아닐 때까지 a, b를 입력받고 a의 값이 더 크면 Yes 아니면 No를 출력하는 단순 구현 문제이다.

in
    1 19
    4 4
    23 14
    0 0
out
    No
    No
    Yes
'''

while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    if a > b:
        print('Yes')
    else:
        print('No')
