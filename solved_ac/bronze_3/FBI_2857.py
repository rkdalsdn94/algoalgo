# 백준 - 브론즈3 - FBI - 2857 - 단순 구현, 문자열 문제
'''
단순 구현, 문자열 문제

입력받은 문자열 중에 'FBI'가 있다면 해당 인덱스를 출력하면 되고, 없다면 'HE GOT AWAY!'를 출력하면 되는 단순한 문제이다.

in
    N-FBI1
    9A-USKOK
    I-NTERPOL
    G-MI6
    RF-KGB1
out
    1

in
    N321-CIA
    F3-B12I
    F-BI-12
    OVO-JE-CIA
    KRIJUMCAR1
out
    HE GOT AWAY!

in
    47-FBI
    BOND-007
    RF-FBI18
    MARICA-13
    13A-FBILL
out
    1 3 5
'''

res = []
for i in range(1, 6):
    word = input()

    if 'FBI' in word:
        res.append(i)

if res:
    print(*res)
else:
    print('HE GOT AWAY!')
