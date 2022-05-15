'''
in
    2
    3 ABC
    5 /HTP
out
    AAABBBCCC
    /////HHHHHTTTTTPPPPP

단순 구현, 문자열 문제이다

글자(s)의 최대 길이가 20이라 문자열을 반복하면서 r을 곱했다.
'''

T = int(input())

for _ in range(T):
    r, s = input().split()
    r = int(r)
    res = ''

    for i in s:
        res += r * i

    print(res)
