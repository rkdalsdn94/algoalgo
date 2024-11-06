# 백준 - 브론즈2 - !!초콜릿 중독 주의!! - 31458 - 구현, 문자열 문제
'''
구현, 문자열 문제

풀이 과정
  1. 입력을 받는다.
  2. 입력을 받은 후, '!'의 개수를 센다.
  3. '!'의 개수가 짝수이면 0, 홀수이면 1을 출력한다.

in
    6
    0!
    1!
    !0
    !1
    !!0!!
    !!1!!
out
    1
    1
    1
    0
    1
    1
'''

t = int(input())
for _ in range(t):
    operation = input().rstrip()
    flag = True
    l_cnt = 0
    res = 0

    for i in operation:
        if i == '!' and flag:
            l_cnt += 1
        elif i != '!':
            flag = False
            res = int(i)
        elif i == '!' and flag == False:
            res = 1

    if res == 0:
        if l_cnt % 2 == 0:
            res = 0
        else:
            res = 1
    else:
        if l_cnt % 2 == 0:
            res = 1
        else:
            res = 0

    print(res)
